# Multilingual Model Evaluations

A benchmarking harness comparing **Claude Sonnet 4.6**, **GPT-5.4 Mini**, and **Gemini 3.1 Flash-Lite Preview** across the top 20 global speaker languages using the [Belebele](https://huggingface.co/datasets/facebook/belebele) reading comprehension benchmark.

## Models

| Key | Model | MMMLU |
|-----|-------|-------|
| `claude` | Claude Sonnet 4.6 | 89.3% |
| `openai` | GPT-5.4 Mini | — |
| `gemini_flash_lite` | Gemini 3.1 Flash-Lite Preview | 88.9% |
| `gemini_flash` | Gemini 3 Flash | — |

`claude`, `openai`, and `gemini` are the primary comparison set. `gemini_flash` is the non-lite Gemini model, included for intra-family comparison on the MMLU-style benchmarks. All model IDs are overridable via `.env`.

## Project Structure

```
multilingual-model-evals/
├── run_eval.py                  # CLI entry point
├── requirements.txt
├── .env.example                 # API key template
├── harness/
│   ├── config.py                # Language mappings, model IDs, dataset configs
│   ├── scoring.py               # Automated metrics (exact match, ROUGE-L, chrF)
│   ├── judge.py                 # Multi-judge consensus scoring
│   ├── runner.py                # Async orchestrator
│   ├── clients/
│   │   ├── base.py
│   │   ├── claude_client.py
│   │   ├── openai_client.py
│   │   └── gemini_client.py
│   └── benchmarks/
│       ├── base.py
│       ├── belebele.py          # Reading comprehension MCQ (20 languages)
│       ├── global_mmlu.py       # Knowledge MCQ — CohereLabs (15 languages)
│       └── milu.py              # Knowledge MCQ — Indic languages (7 languages, gated)
├── docs/
│   └── architecture.md          # System architecture diagram
├── results/
│   ├── belebele/                # Active run outputs (JSONL per model)
│   ├── global_mmlu/             # Global MMLU outputs
│   ├── milu/                    # MILU outputs
│   └── archive/                 # Previous experimental runs
├── benchmarks/
│   ├── existing/                # Phase 2 benchmark audit
│   └── gap_analysis/            # Phase 3 gap analysis
└── literature/                  # Phase 1 literature review
```

## Benchmarks

| Benchmark | Task | Languages | Examples/lang | Scoring | Auth |
|-----------|------|-----------|---------------|---------|------|
| [Belebele](https://huggingface.co/datasets/facebook/belebele) | Reading comprehension MCQ | 20/20 | 900 (full set) | Exact match | Public |
| [Global MMLU](https://huggingface.co/datasets/CohereLabs/Global-MMLU) | Knowledge MCQ (57 subjects) | 15/20 | 1,000 (capped) | Exact match | Public |
| [MILU](https://huggingface.co/datasets/ai4bharat/MILU) | Knowledge MCQ — Indic languages | 7/20 | 1,000 (capped) | Exact match | Gated¹ |

**Language coverage gaps:**
- Global MMLU does not cover: Punjabi, Marathi, Tamil, Urdu (not in dataset)
- MILU covers only Indic languages: English, Hindi, Bengali, Punjabi, Marathi, Telugu, Tamil

¹ MILU requires accepting terms at huggingface.co/datasets/ai4bharat/MILU and setting `HF_TOKEN` in `.env`.

All three benchmarks use MCQ exact-match scoring — no judge pass needed.

## Target Languages

Top 20 by global speakers: Mandarin Chinese, Spanish, English, Hindi, Arabic, Bengali, Portuguese, Russian, Japanese, Punjabi, Marathi, Telugu, Turkish, Tamil, Vietnamese, Korean, French, German, Urdu, Indonesian.

## Running Experiments

### Full run (all models, all benchmarks)

```bash
python run_eval.py                                      # belebele, all 3 primary models
python run_eval.py --benchmarks global_mmlu milu        # new benchmarks, all models
python run_eval.py --models gemini_flash_lite_flash --benchmarks global_mmlu milu  # flash comparison
```

### Benchmark-specific

```bash
python run_eval.py --benchmarks belebele
python run_eval.py --benchmarks global_mmlu
python run_eval.py --benchmarks milu                    # requires HF_TOKEN
```

### Model-specific

```bash
python run_eval.py --models gemini_flash_lite
python run_eval.py --models gemini_flash_lite_flash
python run_eval.py --models claude --models openai
```

---

## Setup

### 1. Clone and install

```bash
git clone https://github.com/dyou3968/multilingual-model-evals.git
cd multilingual-model-evals
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API keys

```bash
cp .env.example .env
```

Open `.env` and fill in your keys:

```
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...          # used for both gemini and gemini_flash

# Required only for MILU (gated dataset):
# 1. Accept terms at https://huggingface.co/datasets/ai4bharat/MILU
# 2. Generate a token at https://huggingface.co/settings/tokens
HF_TOKEN=hf_...
```

Model IDs default to the values below. Override in `.env` to point at a different version:

```
CLAUDE_MODEL=claude-sonnet-4-6
OPENAI_MODEL=gpt-5.4-mini
GEMINI_MODEL=gemini-3.1-flash-lite-preview
GEMINI_FLASH_MODEL=gemini-3-flash-preview
```

### 3. Verify setup (optional smoke test)

Run one model on one language to confirm your keys and dependencies are working:

```bash
python run_eval.py --models claude --languages zho_Hans
```

You should see a progress bar and a new file at `results/belebele/claude.jsonl`.

### Specific languages (Belebele FLORES-200 codes)

```bash
python run_eval.py --languages zho_Hans hin_Deva arb_Arab
```

| Language | Code | Language | Code |
|----------|------|----------|------|
| Mandarin Chinese | `zho_Hans` | Punjabi | `pan_Guru` |
| Spanish | `spa_Latn` | Marathi | `mar_Deva` |
| English | `eng_Latn` | Telugu | `tel_Telu` |
| Hindi | `hin_Deva` | Turkish | `tur_Latn` |
| Arabic | `arb_Arab` | Tamil | `tam_Taml` |
| Bengali | `ben_Beng` | Vietnamese | `vie_Latn` |
| Portuguese | `por_Latn` | Korean | `kor_Hang` |
| Russian | `rus_Cyrl` | French | `fra_Latn` |
| Japanese | `jpn_Jpan` | German | `deu_Latn` |
| Urdu | `urd_Arab` | Indonesian | `ind_Latn` |

### Custom output directory / verbose logging

```bash
python run_eval.py --results-dir /path/to/output --verbose
```

## Resumability

Every run is resumable. If a run is interrupted, restart with the same command — the runner reads existing JSONL files and skips any example IDs already present. You will not be double-charged for completed examples.

## Output Format

Results are written as append-only JSONL files at `results/belebele/<model>.jsonl` — one record per example:

```json
{
  "id": "belebele_zho_Hans_0",
  "benchmark": "belebele",
  "language": "zho_Hans",
  "model": "claude",
  "prediction": "A",
  "reference": "A",
  "correct": true
}
```

## Cost Estimates

All three benchmarks use MCQ exact-match scoring — no judge pass needed. MCQ outputs are a single letter so output tokens are minimal.

**Belebele** — 900 examples × 20 languages = 18,000 examples per model:

| Model | Input (~7.2M tokens) | Output (~90K tokens) | Total |
|-------|---------------------|---------------------|-------|
| Claude Sonnet 4.6 | ~$21.6 | ~$1.4 | **~$23** |
| GPT-5.4 Mini | ~$5.4 | ~$0.4 | **~$6** |
| Gemini 3.1 Flash-Lite Preview | ~$0.7 | ~$0.1 | **~$1** |
| **All 3 models** | | | **~$30** |

**Global MMLU** — 1,000 examples × 15 languages = 15,000 examples per model (Urdu excluded — not available in dataset).

**MILU** — 1,000 examples × 7 languages = 7,000 examples per model (~40% of Belebele volume).

`gemini_flash` (Gemini 3.1 Flash Preview) costs slightly more than flash-lite but runs only on Global MMLU + MILU (~23,000 examples total).

## Architecture

See [docs/architecture.md](docs/architecture.md) for the full system diagram.

The high-level data flow:

```
run_eval.py
    └── runner.py (async orchestrator)
            ├── config.py          (language/model/dataset mappings)
            ├── benchmarks/        (HuggingFace loaders → uniform list[dict])
            ├── clients/           (async API wrappers with retry)
            ├── scoring.py         (automated metrics)
            └── judge.py           (multi-judge 1–5 rubric, self-bias tracking)
                    └── results/   (append-only JSONL, resumable)
```

## Research Context

This project spans four phases:

- **Phase 1** — Literature review of multilingual capabilities across frontier models
- **Phase 2** — Audit of 24 existing multilingual benchmarks with coverage matrix
- **Phase 3** — Gap analysis identifying 8 under-covered areas (low-resource languages, SEA, contamination risk, etc.)
- **Phase 4** — This harness: running Belebele across Claude Sonnet 4.6, GPT-5.4 Mini, and Gemini 3.1 Flash-Lite Preview across 20 languages

See the `literature/`, `benchmarks/existing/`, and `benchmarks/gap_analysis/` directories for Phase 1–3 documents.

## License

MIT
