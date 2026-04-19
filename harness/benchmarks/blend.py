from datasets import load_dataset
from harness.config import DATASET_IDS, BENCHMARK_CONFIGS
from harness.scoring import mcq_correct, exact_match
from .base import Benchmark

_SYSTEM_MCQ = (
    "You are answering a cultural knowledge question. "
    "Choose the best answer from the options. "
    "Respond with only the letter: A, B, C, or D."
)

_SYSTEM_SHORT = (
    "You are answering a cultural knowledge question. "
    "Give a short, direct answer — one word or a brief phrase."
)

_MCQ_TEMPLATE = """\
Question: {question}

A) {option_a}
B) {option_b}
C) {option_c}
D) {option_d}

Answer:"""

_SHORT_TEMPLATE = "Question: {question}\n\nAnswer:"


class BLEnDBenchmark(Benchmark):
    name = "blend"

    def load(self, language_code: str) -> list[dict]:
        """
        language_code for BLEnD is the language name string (e.g. 'Korean', 'Hindi').
        BLEnD contains both MCQ and short-answer formats.
        """
        cfg = BENCHMARK_CONFIGS["blend"]
        ds = load_dataset(DATASET_IDS["blend"], split="test")
        ds = ds.filter(lambda x: x.get("language", "") == language_code)

        if cfg["max_examples_per_language"]:
            ds = ds.select(range(min(cfg["max_examples_per_language"], len(ds))))

        examples = []
        for i, row in enumerate(ds):
            question_type = row.get("question_type", "short_answer")

            if question_type == "multiple_choice":
                examples.append({
                    "id": f"blend_{language_code}_mcq_{i}",
                    "language": language_code,
                    "prompt": _MCQ_TEMPLATE.format(
                        question=row["question"],
                        option_a=row.get("option_a", ""),
                        option_b=row.get("option_b", ""),
                        option_c=row.get("option_c", ""),
                        option_d=row.get("option_d", ""),
                    ),
                    "system": _SYSTEM_MCQ,
                    "reference": row["answer"].upper(),
                    "scoring_type": "mcq",
                    "raw": row,
                })
            else:
                examples.append({
                    "id": f"blend_{language_code}_short_{i}",
                    "language": language_code,
                    "prompt": _SHORT_TEMPLATE.format(question=row["question"]),
                    "system": _SYSTEM_SHORT,
                    "reference": row["answer"],
                    "scoring_type": "short_answer",
                    "raw": row,
                })
        return examples

    def score(self, prediction: str, example: dict) -> dict:
        if example["scoring_type"] == "mcq":
            return {"correct": mcq_correct(prediction, example["reference"])}
        # Short-answer: exact match + flag for optional judge scoring
        return {
            "correct": exact_match(prediction, example["reference"]),
            "needs_judge": True,
        }
