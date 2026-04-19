from datasets import load_dataset
from harness.config import DATASET_IDS, BENCHMARK_CONFIGS
from harness.scoring import mcq_correct
from .base import Benchmark

_SYSTEM = (
    "You are answering a knowledge and reasoning question from a regional exam. "
    "Choose the best answer from the options. "
    "Respond with only the letter: A, B, C, or D."
)

_PROMPT_TEMPLATE = """\
Question: {question}

A) {option_a}
B) {option_b}
C) {option_c}
D) {option_d}

Answer:"""


class INCLUDEBenchmark(Benchmark):
    name = "include"

    def load(self, language_code: str) -> list[dict]:
        """
        INCLUDE is keyed by language name string (e.g. 'Hindi', 'Arabic').
        The language_code passed in from config is the language name for this benchmark.
        """
        cfg = BENCHMARK_CONFIGS["include"]
        ds = load_dataset(DATASET_IDS["include"], split="test")

        # Filter to the target language
        ds = ds.filter(lambda x: x.get("language", "") == language_code)

        if cfg["max_examples_per_language"]:
            ds = ds.select(range(min(cfg["max_examples_per_language"], len(ds))))

        examples = []
        for i, row in enumerate(ds):
            # INCLUDE uses 'answer' field: 'A', 'B', 'C', or 'D'
            examples.append({
                "id": f"include_{language_code}_{i}",
                "language": language_code,
                "prompt": _PROMPT_TEMPLATE.format(
                    question=row["question"],
                    option_a=row["option_a"],
                    option_b=row["option_b"],
                    option_c=row["option_c"],
                    option_d=row["option_d"],
                ),
                "system": _SYSTEM,
                "reference": row["answer"].upper(),
                "scoring_type": "mcq",
                "raw": row,
            })
        return examples

    def score(self, prediction: str, example: dict) -> dict:
        correct = mcq_correct(prediction, example["reference"])
        return {"correct": correct}
