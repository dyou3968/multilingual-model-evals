from datasets import load_dataset
from harness.config import DATASET_IDS, BENCHMARK_CONFIGS
from harness.scoring import numeric_correct
from .base import Benchmark

_SYSTEM = (
    "You are a math problem solver. "
    "Solve the problem step by step, then write your final answer on the last line as: Answer: <number>"
)

_PROMPT_TEMPLATE = "Problem: {question}\n\nSolve step by step:"

# 8-shot exemplars are provided in the original MGSM dataset per language
_EXEMPLAR_TEMPLATE = "Problem: {question}\nAnswer: {answer_number}"


class MGSMBenchmark(Benchmark):
    name = "mgsm"

    def load(self, language_code: str) -> list[dict]:
        cfg = BENCHMARK_CONFIGS["mgsm"]
        ds = load_dataset(DATASET_IDS["mgsm"], language_code, split="test")

        # Build 8-shot prefix from the train split (MGSM provides it)
        try:
            train_ds = load_dataset(DATASET_IDS["mgsm"], language_code, split="train")
            shots = list(train_ds.select(range(min(cfg["n_shots"], len(train_ds)))))
            shot_prefix = "\n\n".join(
                _EXEMPLAR_TEMPLATE.format(**s) for s in shots
            ) + "\n\n"
        except Exception:
            shot_prefix = ""

        examples = []
        for i, row in enumerate(ds):
            examples.append({
                "id": f"mgsm_{language_code}_{i}",
                "language": language_code,
                "prompt": shot_prefix + _PROMPT_TEMPLATE.format(**row),
                "system": _SYSTEM,
                "reference": str(row["answer_number"]),
                "scoring_type": "numeric",
                "raw": row,
            })
        return examples

    def score(self, prediction: str, example: dict) -> dict:
        correct = numeric_correct(prediction, example["reference"])
        return {"correct": correct}
