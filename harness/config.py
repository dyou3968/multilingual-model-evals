import os
from dotenv import load_dotenv

load_dotenv()

# ── Model IDs ────────────────────────────────────────────────────────────────

MODELS = {
    "claude": os.getenv("CLAUDE_MODEL", "claude-opus-4-7"),
    "openai": os.getenv("OPENAI_MODEL", "gpt-5.4"),
    "gemini": os.getenv("GEMINI_MODEL", "gemini-3.1-pro"),
}

MODEL_DISPLAY = {
    "claude": "Claude Opus 4.7",
    "openai": "GPT-5.4",
    "gemini": "Gemini 3.1 Pro",
}

# ── Top-20 Languages ─────────────────────────────────────────────────────────

# Canonical language list with per-benchmark code mappings
TOP_20_LANGUAGES = [
    {
        "name": "Mandarin Chinese",
        "belebele": "zho_Hans",
        "mgsm": "zh",
        "include": "Chinese",
        "blend": "Chinese",
        "indicgenbench": None,
    },
    {
        "name": "Spanish",
        "belebele": "spa_Latn",
        "mgsm": "es",
        "include": "Spanish",
        "blend": "Spanish",
        "indicgenbench": None,
    },
    {
        "name": "English",
        "belebele": "eng_Latn",
        "mgsm": "en",
        "include": "English",
        "blend": "English",
        "indicgenbench": None,
    },
    {
        "name": "Hindi",
        "belebele": "hin_Deva",
        "mgsm": None,
        "include": "Hindi",
        "blend": "Hindi",
        "indicgenbench": "hi",
    },
    {
        "name": "Arabic",
        "belebele": "arb_Arab",
        "mgsm": None,
        "include": "Arabic",
        "blend": "Arabic",
        "indicgenbench": None,
    },
    {
        "name": "Bengali",
        "belebele": "ben_Beng",
        "mgsm": "bn",
        "include": "Bengali",
        "blend": None,
        "indicgenbench": "bn",
    },
    {
        "name": "Portuguese",
        "belebele": "por_Latn",
        "mgsm": None,
        "include": "Portuguese",
        "blend": None,
        "indicgenbench": None,
    },
    {
        "name": "Russian",
        "belebele": "rus_Cyrl",
        "mgsm": "ru",
        "include": "Russian",
        "blend": None,
        "indicgenbench": None,
    },
    {
        "name": "Japanese",
        "belebele": "jpn_Jpan",
        "mgsm": "ja",
        "include": "Japanese",
        "blend": "Japanese",
        "indicgenbench": None,
    },
    {
        "name": "Punjabi",
        "belebele": "pan_Guru",
        "mgsm": None,
        "include": "Punjabi",
        "blend": None,
        "indicgenbench": "pa",
    },
    {
        "name": "Marathi",
        "belebele": "mar_Deva",
        "mgsm": None,
        "include": "Marathi",
        "blend": None,
        "indicgenbench": "mr",
    },
    {
        "name": "Telugu",
        "belebele": "tel_Telu",
        "mgsm": None,
        "include": "Telugu",
        "blend": None,
        "indicgenbench": "te",
    },
    {
        "name": "Turkish",
        "belebele": "tur_Latn",
        "mgsm": None,
        "include": "Turkish",
        "blend": "Turkish",
        "indicgenbench": None,
    },
    {
        "name": "Tamil",
        "belebele": "tam_Taml",
        "mgsm": None,
        "include": "Tamil",
        "blend": None,
        "indicgenbench": "ta",
    },
    {
        "name": "Vietnamese",
        "belebele": "vie_Latn",
        "mgsm": None,
        "include": "Vietnamese",
        "blend": None,
        "indicgenbench": None,
    },
    {
        "name": "Korean",
        "belebele": "kor_Hang",
        "mgsm": None,
        "include": "Korean",
        "blend": "Korean",
        "indicgenbench": None,
    },
    {
        "name": "French",
        "belebele": "fra_Latn",
        "mgsm": "fr",
        "include": "French",
        "blend": "French",
        "indicgenbench": None,
    },
    {
        "name": "German",
        "belebele": "deu_Latn",
        "mgsm": "de",
        "include": "German",
        "blend": "German",
        "indicgenbench": None,
    },
    {
        "name": "Urdu",
        "belebele": "urd_Arab",
        "mgsm": None,
        "include": "Urdu",
        "blend": None,
        "indicgenbench": "ur",
    },
    {
        "name": "Indonesian",
        "belebele": "ind_Latn",
        "mgsm": None,
        "include": "Indonesian",
        "blend": "Indonesian",
        "indicgenbench": None,
    },
]

def languages_for(benchmark: str) -> list[dict]:
    """Return only languages that have a code for the given benchmark."""
    return [lang for lang in TOP_20_LANGUAGES if lang.get(benchmark) is not None]

# ── HuggingFace Dataset IDs ───────────────────────────────────────────────────

DATASET_IDS = {
    "belebele": "facebook/belebele",
    "mgsm": "juletxara/mgsm",
    "include": "Cohere/include-mit",      # verify: https://huggingface.co/datasets/Cohere/include-mit
    "blend": "nyu-mll/blend",             # verify: may be under a different org
    "indicgenbench": "ai4bharat/IndicGenBench",  # verify on HF
}

# ── Benchmark Defaults ────────────────────────────────────────────────────────

BENCHMARK_CONFIGS = {
    "belebele": {
        "n_shots": 0,
        "max_examples_per_language": None,  # None = use full test set (~900)
        "scoring": "exact_match",
    },
    "mgsm": {
        "n_shots": 8,
        "max_examples_per_language": None,  # 250 per language
        "scoring": "exact_match",
    },
    "include": {
        "n_shots": 5,
        "max_examples_per_language": 500,   # cap for cost control; full = ~4k/lang
        "scoring": "exact_match",
    },
    "blend": {
        "n_shots": 0,
        "max_examples_per_language": None,
        "scoring": "exact_match",           # MCQ portion; short-answer uses judge
    },
    "indicgenbench": {
        "n_shots": 0,
        "max_examples_per_language": 200,   # generation is expensive; cap per lang
        "scoring": "rouge_chrf",
        "judge_subset": 100,               # examples per language sent to multi-judge
    },
}

# ── Rate Limiting ─────────────────────────────────────────────────────────────

RATE_LIMITS = {
    "claude": int(os.getenv("CLAUDE_RPM", 50)),
    "openai": int(os.getenv("OPENAI_RPM", 60)),
    "gemini": int(os.getenv("GEMINI_RPM", 60)),
}

# ── Paths ─────────────────────────────────────────────────────────────────────

RESULTS_DIR = os.getenv("RESULTS_DIR", "results")
