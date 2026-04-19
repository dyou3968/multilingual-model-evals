"""Automated scoring utilities for exact-match, ROUGE, and chrF."""

import re
import string
from rouge_score import rouge_scorer
import sacrebleu


# ── Exact Match ───────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text)
    return text


def exact_match(prediction: str, reference: str) -> bool:
    return normalize(prediction) == normalize(reference)


def extract_mcq_answer(text: str) -> str | None:
    """Pull the letter choice (A-D) out of a model response."""
    text = text.strip()
    # Explicit single-letter answer
    if re.match(r"^[A-Da-d][.):]?\s*$", text):
        return text[0].upper()
    # "The answer is A" or "Answer: B"
    m = re.search(r"\b(?:answer(?:\s+is)?|choice)[:\s]+([A-Da-d])\b", text, re.I)
    if m:
        return m.group(1).upper()
    # Letter at start of response
    m = re.match(r"^([A-Da-d])[.):\s]", text)
    if m:
        return m.group(1).upper()
    return None


def extract_numeric_answer(text: str) -> str | None:
    """Pull a final numeric answer from MGSM-style chain-of-thought response."""
    # Look for explicit "Answer: N" pattern first
    m = re.search(r"(?:answer|the answer is|=)\s*:?\s*(-?[\d,]+\.?\d*)", text, re.I)
    if m:
        return m.group(1).replace(",", "")
    # Fall back to last number in the response
    nums = re.findall(r"-?[\d,]+\.?\d*", text)
    if nums:
        return nums[-1].replace(",", "")
    return None


def mcq_correct(prediction: str, reference: str) -> bool:
    """Score a multiple-choice prediction (A/B/C/D) against a reference letter."""
    pred = extract_mcq_answer(prediction)
    ref = reference.strip().upper()
    if pred is None:
        return False
    return pred == ref


def numeric_correct(prediction: str, reference: str | int | float) -> bool:
    """Score a numeric answer (tolerates comma separators, float ~= int)."""
    pred = extract_numeric_answer(prediction)
    if pred is None:
        return False
    try:
        return float(pred) == float(str(reference).replace(",", ""))
    except ValueError:
        return False


# ── Generation Metrics ────────────────────────────────────────────────────────

_rouge = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)


def rouge_l(prediction: str, reference: str) -> float:
    scores = _rouge.score(reference, prediction)
    return round(scores["rougeL"].fmeasure, 4)


def chrf(prediction: str, reference: str) -> float:
    score = sacrebleu.corpus_chrf([prediction], [[reference]])
    return round(score.score / 100, 4)


def generation_scores(prediction: str, reference: str) -> dict[str, float]:
    return {
        "rouge_l": rouge_l(prediction, reference),
        "chrf": chrf(prediction, reference),
    }


# ── Aggregation ───────────────────────────────────────────────────────────────

def aggregate(results: list[dict]) -> dict:
    """Compute aggregate metrics from a list of per-example result dicts."""
    if not results:
        return {}

    keys = [k for k in results[0] if isinstance(results[0][k], (int, float, bool))]
    return {
        k: round(sum(r[k] for r in results) / len(results), 4)
        for k in keys
    }
