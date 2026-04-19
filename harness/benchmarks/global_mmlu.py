from __future__ import annotations

from datasets import load_dataset
from harness.config import DATASET_IDS, BENCHMARK_CONFIGS
from harness.scoring import mcq_correct
from .base import Benchmark

_SYSTEM = (
    "You are answering a multiple-choice question. "
    "Choose the best answer from the four options. "
    "Respond with only the letter of the correct answer: A, B, C, or D."
)

_PROMPT_TEMPLATE = """\
Question: {question}

A) {option_a}
B) {option_b}
C) {option_c}
D) {option_d}

Answer:"""


class GlobalMMLUBenchmark(Benchmark):
    name = "global_mmlu"

    def load(self, language_code: str) -> list[dict]:
        cfg = BENCHMARK_CONFIGS["global_mmlu"]
        ds = load_dataset(DATASET_IDS["global_mmlu"], language_code, split="test")

        if cfg["max_examples_per_language"]:
            ds = ds.select(range(min(cfg["max_examples_per_language"], len(ds))))

        examples = []
        for i, row in enumerate(ds):
            examples.append({
                "id": f"global_mmlu_{language_code}_{i}",
                "language": language_code,
                "prompt": _PROMPT_TEMPLATE.format(
                    question=row["question"],
                    option_a=row["option_a"],
                    option_b=row["option_b"],
                    option_c=row["option_c"],
                    option_d=row["option_d"],
                ),
                "system": _SYSTEM,
                "reference": str(row["answer"]).strip().upper(),
                "scoring_type": "mcq",
                "raw": row,
            })
        return examples

    def score(self, prediction: str, example: dict) -> dict:
        return {"correct": mcq_correct(prediction, example["reference"])}
