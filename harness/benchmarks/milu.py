from __future__ import annotations

import os

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

A) {a}
B) {b}
C) {c}
D) {d}

Answer:"""

# MILU target field is the option key name, e.g. "option2" → "B"
_OPTION_KEY_TO_LETTER = {
    "option1": "A", "option2": "B", "option3": "C", "option4": "D",
}


def _parse_answer(raw: object) -> str:
    s = str(raw).strip()
    if s in _OPTION_KEY_TO_LETTER:
        return _OPTION_KEY_TO_LETTER[s]
    if s.upper() in ("A", "B", "C", "D"):
        return s.upper()
    return "A"


class MILUBenchmark(Benchmark):
    name = "milu"

    def load(self, language_code: str) -> list[dict]:
        """language_code here is the full language name used by MILU (e.g. 'Hindi')."""
        cfg = BENCHMARK_CONFIGS["milu"]
        token = os.environ.get("HF_TOKEN")
        if not token:
            raise EnvironmentError(
                "MILU is a gated dataset. Set HF_TOKEN in your .env after accepting "
                "the terms at https://huggingface.co/datasets/ai4bharat/MILU"
            )
        ds = load_dataset(
            DATASET_IDS["milu"],
            data_dir=language_code,
            split="test",
            token=token,
        )

        if cfg["max_examples_per_language"]:
            ds = ds.select(range(min(cfg["max_examples_per_language"], len(ds))))

        examples = []
        for i, row in enumerate(ds):
            examples.append({
                "id": f"milu_{language_code}_{i}",
                "language": language_code,
                "prompt": _PROMPT_TEMPLATE.format(
                    question=row["question"],
                    a=row["option1"],
                    b=row["option2"],
                    c=row["option3"],
                    d=row["option4"],
                ),
                "system": _SYSTEM,
                "reference": _parse_answer(row["target"]),
                "scoring_type": "mcq",
                "raw": row,
            })
        return examples

    def score(self, prediction: str, example: dict) -> dict:
        return {"correct": mcq_correct(prediction, example["reference"])}
