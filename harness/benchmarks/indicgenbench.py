from datasets import load_dataset
from harness.config import DATASET_IDS, BENCHMARK_CONFIGS
from harness.scoring import generation_scores
from .base import Benchmark

# Task-specific system prompts
_SYSTEMS = {
    "summarization": (
        "You are a summarization assistant. "
        "Summarize the provided passage in the target language. "
        "Be concise and accurate."
    ),
    "translation": (
        "You are a translation assistant. "
        "Translate the provided text accurately into the target language."
    ),
    "xling_qa": (
        "You are a question answering assistant. "
        "Answer the question based on the provided passage. "
        "Give a concise, accurate answer."
    ),
}

_PROMPTS = {
    "summarization": (
        "Passage ({source_lang}):\n{source}\n\n"
        "Summarize the above passage in {target_lang}:"
    ),
    "translation": (
        "Translate the following text from {source_lang} to {target_lang}:\n\n"
        "{source}\n\nTranslation:"
    ),
    "xling_qa": (
        "Passage ({source_lang}):\n{passage}\n\n"
        "Question: {question}\n\n"
        "Answer in {target_lang}:"
    ),
}


class IndicGenBenchBenchmark(Benchmark):
    name = "indicgenbench"

    def load(self, language_code: str) -> list[dict]:
        """
        language_code is the ISO 639-1 code (e.g. 'hi', 'bn', 'mr').
        IndicGenBench covers three tasks; we load all three and tag each example.
        """
        cfg = BENCHMARK_CONFIGS["indicgenbench"]
        cap = cfg["max_examples_per_language"]
        examples = []

        for task in ["summarization", "translation", "xling_qa"]:
            try:
                ds = load_dataset(
                    DATASET_IDS["indicgenbench"],
                    f"{task}_{language_code}",
                    split="test",
                )
            except Exception:
                # Not all languages have all tasks; skip gracefully
                continue

            if cap:
                ds = ds.select(range(min(cap, len(ds))))

            for i, row in enumerate(ds):
                if task == "xling_qa":
                    prompt = _PROMPTS["xling_qa"].format(
                        source_lang="English",
                        passage=row.get("passage", row.get("context", "")),
                        question=row["question"],
                        target_lang=language_code,
                    )
                elif task == "summarization":
                    prompt = _PROMPTS["summarization"].format(
                        source_lang="English",
                        source=row["document"],
                        target_lang=language_code,
                    )
                else:  # translation
                    prompt = _PROMPTS["translation"].format(
                        source_lang="English",
                        source=row["source"],
                        target_lang=language_code,
                    )

                examples.append({
                    "id": f"indicgenbench_{language_code}_{task}_{i}",
                    "language": language_code,
                    "task": task,
                    "prompt": prompt,
                    "system": _SYSTEMS[task],
                    "reference": row.get("target", row.get("answer", row.get("summary", ""))),
                    "scoring_type": "generation",
                    "needs_judge": True,
                    "raw": row,
                })

        return examples

    def score(self, prediction: str, example: dict) -> dict:
        scores = generation_scores(prediction, example["reference"])
        scores["needs_judge"] = True
        return scores
