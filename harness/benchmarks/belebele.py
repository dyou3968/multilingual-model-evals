from datasets import load_dataset
from harness.config import DATASET_IDS, BENCHMARK_CONFIGS
from harness.scoring import mcq_correct
from .base import Benchmark

_SYSTEM = (
    "You are answering a reading comprehension question. "
    "Read the passage, then choose the best answer from the four options. "
    "Respond with only the letter of the correct answer: A, B, C, or D."
)

_PROMPT_TEMPLATE = """\
Passage:
{flores_passage}

Question: {question}

A) {mc_answer1}
B) {mc_answer2}
C) {mc_answer3}
D) {mc_answer4}

Answer:"""

_ANSWER_MAP = {"1": "A", "2": "B", "3": "C", "4": "D"}


class BelebeleBenchmark(Benchmark):
    name = "belebele"

    def load(self, language_code: str) -> list[dict]:
        cfg = BENCHMARK_CONFIGS["belebele"]
        ds = load_dataset(DATASET_IDS["belebele"], language_code, split="test")

        if cfg["max_examples_per_language"]:
            ds = ds.select(range(min(cfg["max_examples_per_language"], len(ds))))

        examples = []
        for i, row in enumerate(ds):
            examples.append({
                "id": f"belebele_{language_code}_{i}",
                "language": language_code,
                "prompt": _PROMPT_TEMPLATE.format(**row),
                "system": _SYSTEM,
                "reference": _ANSWER_MAP[str(row["correct_answer_num"])],
                "scoring_type": "mcq",
                "raw": row,
            })
        return examples

    def score(self, prediction: str, example: dict) -> dict:
        correct = mcq_correct(prediction, example["reference"])
        return {"correct": correct}
