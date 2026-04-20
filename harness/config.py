import os
from dotenv import load_dotenv

load_dotenv()

# ── Model IDs ────────────────────────────────────────────────────────────────

MODELS = {
    "claude": os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6"),
    "openai": os.getenv("OPENAI_MODEL", "gpt-5.4-mini"),
    "gemini_flash_lite": os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview"),
    "gemini_flash": os.getenv("GEMINI_FLASH_MODEL", "gemini-3-flash-preview"),
}

MODEL_DISPLAY = {
    "claude": "Claude Sonnet 4.6",
    "openai": "GPT-5.4 Mini",
    "gemini_flash_lite": "Gemini 3.1 Flash-Lite Preview",
    "gemini_flash": "Gemini 3 Flash",
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
        "global_mmlu": "zh",
        "milu": None,
    },
    {
        "name": "Spanish",
        "belebele": "spa_Latn",
        "mgsm": "es",
        "include": "Spanish",
        "blend": "Spanish",
        "indicgenbench": None,
        "global_mmlu": "es",
        "milu": None,
    },
    {
        "name": "English",
        "belebele": "eng_Latn",
        "mgsm": "en",
        "include": "English",
        "blend": "English",
        "indicgenbench": None,
        "global_mmlu": "en",
        "milu": "English",
    },
    {
        "name": "Hindi",
        "belebele": "hin_Deva",
        "mgsm": None,
        "include": "Hindi",
        "blend": "Hindi",
        "indicgenbench": "hi",
        "global_mmlu": "hi",
        "milu": "Hindi",
    },
    {
        "name": "Arabic",
        "belebele": "arb_Arab",
        "mgsm": None,
        "include": "Arabic",
        "blend": "Arabic",
        "indicgenbench": None,
        "global_mmlu": "ar",
        "milu": None,
    },
    {
        "name": "Bengali",
        "belebele": "ben_Beng",
        "mgsm": "bn",
        "include": "Bengali",
        "blend": None,
        "indicgenbench": "bn",
        "global_mmlu": "bn",
        "milu": "Bengali",
    },
    {
        "name": "Portuguese",
        "belebele": "por_Latn",
        "mgsm": None,
        "include": "Portuguese",
        "blend": None,
        "indicgenbench": None,
        "global_mmlu": "pt",
        "milu": None,
    },
    {
        "name": "Russian",
        "belebele": "rus_Cyrl",
        "mgsm": "ru",
        "include": "Russian",
        "blend": None,
        "indicgenbench": None,
        "global_mmlu": "ru",
        "milu": None,
    },
    {
        "name": "Japanese",
        "belebele": "jpn_Jpan",
        "mgsm": "ja",
        "include": "Japanese",
        "blend": "Japanese",
        "indicgenbench": None,
        "global_mmlu": "ja",
        "milu": None,
    },
    {
        "name": "Punjabi",
        "belebele": "pan_Guru",
        "mgsm": None,
        "include": "Punjabi",
        "blend": None,
        "indicgenbench": "pa",
        "global_mmlu": None,
        "milu": "Punjabi",
    },
    {
        "name": "Marathi",
        "belebele": "mar_Deva",
        "mgsm": None,
        "include": "Marathi",
        "blend": None,
        "indicgenbench": "mr",
        "global_mmlu": None,
        "milu": "Marathi",
    },
    {
        "name": "Telugu",
        "belebele": "tel_Telu",
        "mgsm": None,
        "include": "Telugu",
        "blend": None,
        "indicgenbench": "te",
        "global_mmlu": None,
        "milu": "Telugu",
    },
    {
        "name": "Turkish",
        "belebele": "tur_Latn",
        "mgsm": None,
        "include": "Turkish",
        "blend": "Turkish",
        "indicgenbench": None,
        "global_mmlu": "tr",
        "milu": None,
    },
    {
        "name": "Tamil",
        "belebele": "tam_Taml",
        "mgsm": None,
        "include": "Tamil",
        "blend": None,
        "indicgenbench": "ta",
        "global_mmlu": None,
        "milu": "Tamil",
    },
    {
        "name": "Vietnamese",
        "belebele": "vie_Latn",
        "mgsm": None,
        "include": "Vietnamese",
        "blend": None,
        "indicgenbench": None,
        "global_mmlu": "vi",
        "milu": None,
    },
    {
        "name": "Korean",
        "belebele": "kor_Hang",
        "mgsm": None,
        "include": "Korean",
        "blend": "Korean",
        "indicgenbench": None,
        "global_mmlu": "ko",
        "milu": None,
    },
    {
        "name": "French",
        "belebele": "fra_Latn",
        "mgsm": "fr",
        "include": "French",
        "blend": "French",
        "indicgenbench": None,
        "global_mmlu": "fr",
        "milu": None,
    },
    {
        "name": "German",
        "belebele": "deu_Latn",
        "mgsm": "de",
        "include": "German",
        "blend": "German",
        "indicgenbench": None,
        "global_mmlu": "de",
        "milu": None,
    },
    {
        "name": "Urdu",
        "belebele": "urd_Arab",
        "mgsm": None,
        "include": "Urdu",
        "blend": None,
        "indicgenbench": "ur",
        "global_mmlu": "ur",
        "milu": None,
    },
    {
        "name": "Indonesian",
        "belebele": "ind_Latn",
        "mgsm": None,
        "include": "Indonesian",
        "blend": "Indonesian",
        "indicgenbench": None,
        "global_mmlu": "id",
        "milu": None,
    },
]

def languages_for(benchmark: str) -> list[dict]:
    """Return only languages that have a code for the given benchmark."""
    return [lang for lang in TOP_20_LANGUAGES if lang.get(benchmark) is not None]

# ── HuggingFace Dataset IDs ───────────────────────────────────────────────────

DATASET_IDS = {
    "belebele": "facebook/belebele",
    "mgsm": "juletxara/mgsm",
    "include": "Cohere/include-mit",
    "blend": "nyu-mll/blend",
    "indicgenbench": "ai4bharat/IndicGenBench",
    "global_mmlu": "CohereLabs/Global-MMLU",
    "milu": "ai4bharat/MILU",             # gated: requires HF_TOKEN + accepted terms
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
    "global_mmlu": {
        "n_shots": 0,
        "max_examples_per_language": 1000,  # 14,300 available; cap for cost control
        "scoring": "exact_match",
    },
    "milu": {
        "n_shots": 0,
        "max_examples_per_language": 1000,  # 4k-15k available; cap for cost control
        "scoring": "exact_match",
        "requires_hf_token": True,          # gated dataset
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
