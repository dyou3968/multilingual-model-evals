"""
Async evaluation runner.

Iterates over benchmarks × languages × models, stores raw outputs as JSONL,
and supports resumability by skipping already-completed example IDs.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
from pathlib import Path

import jsonlines
from tqdm.asyncio import tqdm as async_tqdm

from harness.benchmarks import BENCHMARKS
from harness.clients import get_all_clients
from harness.clients.base import BaseClient
from harness.config import BENCHMARK_CONFIGS, languages_for
from harness.judge import judge_batch

logger = logging.getLogger(__name__)

_DEFAULT_RESULTS_DIR = Path(os.getenv("RESULTS_DIR", "results"))
_GENERATION_CONCURRENCY = int(os.getenv("GENERATION_CONCURRENCY", "8"))
_JUDGE_CONCURRENCY = int(os.getenv("JUDGE_CONCURRENCY", "5"))


def _results_path(results_dir: Path, benchmark: str, model_key: str) -> Path:
    path = results_dir / benchmark / f"{model_key}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _load_completed_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    completed: set[str] = set()
    with jsonlines.open(path) as reader:
        for record in reader:
            completed.add(record["id"])
    return completed


async def _run_example(
    client: BaseClient,
    example: dict,
    sem: asyncio.Semaphore,
) -> tuple[str, dict]:
    """Return (prediction_text, score_dict)."""
    async with sem:
        try:
            prediction = await client.complete(
                prompt=example["prompt"],
                system=example.get("system", ""),
                max_tokens=512,
                temperature=0.0,
            )
        except Exception as exc:
            logger.warning("Model %s failed on %s: %s", client.model_key, example["id"], exc)
            prediction = ""

        benchmark_cls = BENCHMARKS[example["benchmark"]]
        bench = benchmark_cls()
        scores = bench.score(prediction, example)
        return prediction, scores


async def run_benchmark(
    benchmark_name: str,
    model_keys: list[str],
    language_codes: list[str] | None = None,
    results_dir: Path = _DEFAULT_RESULTS_DIR,
    clients: dict[str, BaseClient] | None = None,
) -> None:
    """Run one benchmark for the specified models and languages."""
    if clients is None:
        clients = get_all_clients()

    bench_cls = BENCHMARKS[benchmark_name]
    cfg = BENCHMARK_CONFIGS[benchmark_name]
    bench_languages = languages_for(benchmark_name)

    # Filter to requested languages if specified
    if language_codes:
        bench_languages = [l for l in bench_languages if l.get(benchmark_name) in language_codes]

    if not bench_languages:
        logger.warning("No matching languages for benchmark %s", benchmark_name)
        return

    logger.info("Loading %s examples for %d languages...", benchmark_name, len(bench_languages))
    all_examples: list[dict] = []
    for lang in bench_languages:
        lang_code = lang[benchmark_name]
        bench_obj = bench_cls()
        try:
            examples = bench_obj.load(lang_code)
        except Exception as exc:
            logger.warning("Failed to load %s/%s: %s", benchmark_name, lang_code, exc)
            continue
        for ex in examples:
            ex["benchmark"] = benchmark_name
        all_examples.extend(examples)

    if not all_examples:
        logger.warning("No examples loaded for %s", benchmark_name)
        return

    sem = asyncio.Semaphore(_GENERATION_CONCURRENCY)
    judge_queue: list[tuple[str, str, dict]] = []

    for model_key in model_keys:
        client = clients[model_key]
        out_path = _results_path(results_dir, benchmark_name, model_key)
        completed = _load_completed_ids(out_path)

        pending = [ex for ex in all_examples if ex["id"] not in completed]
        if not pending:
            logger.info("All %s examples already complete for %s", benchmark_name, model_key)
            continue

        logger.info(
            "Running %s: %d examples for model %s (%d already done)",
            benchmark_name, len(pending), model_key, len(completed)
        )

        tasks = [_run_example(client, ex, sem) for ex in pending]

        with jsonlines.open(out_path, mode="a") as writer:
            for example, (prediction, scores) in zip(
                pending,
                await async_tqdm.gather(*tasks, desc=f"{benchmark_name}/{model_key}"),
            ):
                record = {
                    "id": example["id"],
                    "benchmark": benchmark_name,
                    "language": example["language"],
                    "model": model_key,
                    "prediction": prediction,
                    "reference": example.get("reference", ""),
                    **scores,
                }
                writer.write(record)

                if scores.get("needs_judge"):
                    judge_queue.append((prediction, model_key, example))

    # Run multi-judge consensus on flagged examples
    if judge_queue:
        logger.info("Running multi-judge on %d examples...", len(judge_queue))
        judge_results = await judge_batch(judge_queue, clients, concurrency=_JUDGE_CONCURRENCY)

        judge_path = results_dir / benchmark_name / "judge_scores.jsonl"
        judge_path.parent.mkdir(parents=True, exist_ok=True)
        with jsonlines.open(judge_path, mode="a") as writer:
            for result in judge_results:
                writer.write(result.to_dict())


async def run_all(
    benchmark_names: list[str],
    model_keys: list[str],
    language_codes: list[str] | None = None,
    results_dir: Path = _DEFAULT_RESULTS_DIR,
) -> None:
    """Run multiple benchmarks sequentially (each benchmark may parallelize internally)."""
    clients = get_all_clients()
    for benchmark_name in benchmark_names:
        await run_benchmark(
            benchmark_name=benchmark_name,
            model_keys=model_keys,
            language_codes=language_codes,
            results_dir=results_dir,
            clients=clients,
        )
