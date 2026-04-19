"""
Multi-judge consensus scoring for generation and short-answer tasks.

All three models score each other's outputs on identical rubrics.
Self-evaluation is tracked explicitly but included in the final score.
"""
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field

from harness.clients import get_all_clients
from harness.clients.base import BaseClient

logger = logging.getLogger(__name__)

_JUDGE_SYSTEM = (
    "You are an expert multilingual evaluator. "
    "Your job is to score a model-generated response against a reference answer. "
    "Be objective, consistent, and language-agnostic in your assessment."
)

_JUDGE_PROMPT = """\
Task: {task_description}
Language: {language}

Reference answer:
{reference}

Model response:
{prediction}

Score the response on a scale of 1–5:
  1 = Completely wrong or off-topic
  2 = Mostly wrong with some relevant content
  3 = Partially correct, missing key information
  4 = Mostly correct with minor errors or omissions
  5 = Fully correct and complete

Respond with ONLY a single integer (1, 2, 3, 4, or 5). No explanation."""

_TASK_DESCRIPTIONS = {
    "summarization": "Summarize a passage in the target language",
    "translation": "Translate text into the target language",
    "xling_qa": "Answer a question in the target language based on an English passage",
    "short_answer": "Answer a cultural knowledge question accurately",
    "generation": "Generate a response in the target language",
}


@dataclass
class JudgeScore:
    judge_model: str
    scored_model: str
    example_id: str
    score: int
    is_self_eval: bool = field(init=False)

    def __post_init__(self) -> None:
        self.is_self_eval = self.judge_model == self.scored_model


@dataclass
class ConsensusResult:
    example_id: str
    scored_model: str
    scores: list[JudgeScore]

    @property
    def mean_score(self) -> float:
        return sum(s.score for s in self.scores) / len(self.scores) if self.scores else 0.0

    @property
    def cross_judge_mean(self) -> float:
        cross = [s.score for s in self.scores if not s.is_self_eval]
        return sum(cross) / len(cross) if cross else 0.0

    @property
    def self_score(self) -> int | None:
        for s in self.scores:
            if s.is_self_eval:
                return s.score
        return None

    @property
    def self_bias(self) -> float | None:
        if self.self_score is None or not any(not s.is_self_eval for s in self.scores):
            return None
        return self.self_score - self.cross_judge_mean

    def to_dict(self) -> dict:
        return {
            "example_id": self.example_id,
            "scored_model": self.scored_model,
            "mean_score": round(self.mean_score, 3),
            "cross_judge_mean": round(self.cross_judge_mean, 3),
            "self_score": self.self_score,
            "self_bias": round(self.self_bias, 3) if self.self_bias is not None else None,
            "per_judge": {s.judge_model: s.score for s in self.scores},
        }


def _extract_score(text: str) -> int | None:
    for ch in text.strip():
        if ch.isdigit() and ch in "12345":
            return int(ch)
    return None


async def _judge_once(
    judge: BaseClient,
    prediction: str,
    example: dict,
) -> int | None:
    task_key = example.get("task", example.get("scoring_type", "generation"))
    task_desc = _TASK_DESCRIPTIONS.get(task_key, task_key)

    prompt = _JUDGE_PROMPT.format(
        task_description=task_desc,
        language=example.get("language", "unknown"),
        reference=example.get("reference", ""),
        prediction=prediction,
    )
    try:
        response = await judge.complete(
            prompt=prompt,
            system=_JUDGE_SYSTEM,
            max_tokens=8,
            temperature=0.0,
        )
        return _extract_score(response)
    except Exception as exc:
        logger.warning("Judge %s failed for %s: %s", judge.model_key, example.get("id"), exc)
        return None


async def judge_example(
    prediction: str,
    scored_model_key: str,
    example: dict,
    clients: dict[str, BaseClient] | None = None,
) -> ConsensusResult:
    """Run all judge models on one prediction and return a ConsensusResult."""
    if clients is None:
        clients = get_all_clients()

    judge_tasks = {
        model_key: _judge_once(client, prediction, example)
        for model_key, client in clients.items()
    }
    raw_scores = await asyncio.gather(*judge_tasks.values(), return_exceptions=True)

    scores: list[JudgeScore] = []
    for model_key, raw in zip(judge_tasks.keys(), raw_scores):
        if isinstance(raw, Exception) or raw is None:
            continue
        scores.append(
            JudgeScore(
                judge_model=model_key,
                scored_model=scored_model_key,
                example_id=example["id"],
                score=raw,
            )
        )

    return ConsensusResult(
        example_id=example["id"],
        scored_model=scored_model_key,
        scores=scores,
    )


async def judge_batch(
    predictions: list[tuple[str, str, dict]],
    clients: dict[str, BaseClient] | None = None,
    concurrency: int = 5,
) -> list[ConsensusResult]:
    """
    Judge a batch of (prediction, scored_model_key, example) tuples.
    concurrency caps simultaneous judge calls to avoid rate limits.
    """
    if clients is None:
        clients = get_all_clients()

    sem = asyncio.Semaphore(concurrency)

    async def _bounded(prediction: str, model_key: str, example: dict) -> ConsensusResult:
        async with sem:
            return await judge_example(prediction, model_key, example, clients)

    return await asyncio.gather(
        *[_bounded(pred, mk, ex) for pred, mk, ex in predictions]
    )
