# Multilingual Model Evaluations

A benchmarking harness comparing **Claude Sonnet 4.6**, **GPT-5.4 Mini**, **Gemini 3.1 Flash-Lite Preview**, and **Gemini 3 Flash** across the top 20 global speaker languages using three multilingual benchmarks: [Belebele](https://huggingface.co/datasets/facebook/belebele) (reading comprehension), [Global MMLU](https://huggingface.co/datasets/CohereLabs/Global-MMLU) (knowledge MCQ), and [MILU](https://huggingface.co/datasets/ai4bharat/MILU) (Indic language knowledge MCQ).

## Models

| Key | Model | MMMLU |
|-----|-------|-------|
| `claude` | Claude Sonnet 4.6 | 89.3% |
| `openai` | GPT-5.4 Mini | — |
| `gemini_flash_lite` | Gemini 3.1 Flash-Lite Preview | 88.9% |
| `gemini_flash` | Gemini 3 Flash | — |

`claude`, `openai`, and `gemini_flash_lite` are the primary comparison set. `gemini_flash` is the non-lite Gemini model, included for intra-family comparison on the MMLU-style benchmarks. All model IDs are overridable via `.env`.

## Results

### Belebele (Reading Comprehension MCQ — 20 languages, 900 examples each)

| Model | Overall Accuracy |
|-------|-----------------|
| Gemini 3.1 Flash-Lite Preview | **92.5%** (16,641 / 18,000) |
| GPT-5.4 Mini | **89.5%** (16,103 / 18,000) |
| Claude Sonnet 4.6 | **87.7%** (15,791 / 18,000) |

**Per-language breakdown:**

| Language | Code | Claude Sonnet 4.6 | GPT-5.4 Mini | Gemini 3.1 Flash-Lite |
|----------|------|:-----------------:|:------------:|:---------------------:|
| English | eng_Latn | 96.0% | 95.1% | 96.6% |
| Arabic | arb_Arab | 93.8% | 91.4% | 95.2% |
| French | fra_Latn | 92.6% | 93.4% | 95.6% |
| Portuguese | por_Latn | 92.6% | 92.1% | 94.6% |
| German | deu_Latn | 92.3% | 93.1% | 95.3% |
| Korean | kor_Hang | 91.9% | 91.1% | 92.8% |
| Mandarin Chinese | zho_Hans | 91.7% | 92.3% | 94.1% |
| Vietnamese | vie_Latn | 91.0% | 90.7% | 93.4% |
| Indonesian | ind_Latn | 90.8% | 89.9% | 94.1% |
| Russian | rus_Cyrl | 89.7% | 92.9% | 94.9% |
| Spanish | spa_Latn | 89.7% | 91.7% | 94.2% |
| Japanese | jpn_Jpan | 88.8% | 89.2% | 92.2% |
| Turkish | tur_Latn | 88.2% | 88.8% | 92.8% |
| Bengali | ben_Beng | 83.7% | 86.6% | 90.6% |
| Punjabi | pan_Guru | 82.9% | 86.4% | 89.1% |
| Marathi | mar_Deva | 80.7% | 86.8% | 90.9% |
| Telugu | tel_Telu | 80.8% | 82.8% | 85.9% |
| Urdu | urd_Arab | 80.2% | 86.0% | 90.9% |
| Hindi | hin_Deva | 79.6% | 84.6% | 88.8% |
| Tamil | tam_Taml | 77.9% | 84.3% | 87.1% |

Full per-language results and methodology: [results/belebele/README.md](results/belebele/README.md)

### Global MMLU (Knowledge MCQ — 15 languages, 1,000 examples each)

Our harness run: 0-shot, Gemini 3.1 Flash-Lite and Gemini 3 Flash. System card results for Claude and Gemini 3 Pro included for context (reasoning-enabled, 42 languages) — methodology differs, see [results/global_mmlu/README.md](results/global_mmlu/README.md).

| Model | Overall Accuracy | Notes |
|-------|-----------------|-------|
| Gemini 3 Pro | **91.8%** | System card — 42 langs, reasoning enabled |
| Claude Opus 4.6 | **90.1%** | System card — 42 langs, reasoning enabled |
| GPT-5.2 Pro | **90.1%** | System card — 42 langs, reasoning enabled |
| Claude Sonnet 4.6 | **88.7%** | System card — 42 langs, reasoning enabled |
| Claude Sonnet 4.5 | **87.9%** | System card — 42 langs, reasoning enabled |
| Gemini 3.1 Flash-Lite | **85.8%** | Our harness — 15 langs, 0-shot |
| Gemini 3 Flash | *(scheduled)* | Our harness — 15 langs, 0-shot |

**Per-language breakdown (our harness):**

| Language | Code | Gemini 3.1 Flash-Lite | Gemini 3 Flash |
|----------|------|:---------------------:|:--------------:|
| English | en | 88.0% | *(scheduled)* |
| German | de | 87.2% | *(scheduled)* |
| Spanish | es | 86.9% | *(scheduled)* |
| Portuguese | pt | 86.8% | *(scheduled)* |
| Russian | ru | 86.7% | *(scheduled)* |
| Japanese | ja | 86.0% | *(scheduled)* |
| Hindi | hi | 85.9% | *(scheduled)* |
| Mandarin Chinese | zh | 85.8% | *(scheduled)* |
| French | fr | 85.7% | *(scheduled)* |
| Indonesian | id | 85.5% | *(scheduled)* |
| Turkish | tr | 85.4% | *(scheduled)* |
| Arabic | ar | 85.3% | *(scheduled)* |
| Vietnamese | vi | 84.9% | *(scheduled)* |
| Bengali | bn | 83.3% | *(scheduled)* |
| Korean | ko | 83.1% | *(scheduled)* |

Full results, resource-tier breakdown, and system card comparison: [results/global_mmlu/README.md](results/global_mmlu/README.md)

### MILU (Knowledge MCQ — Indic languages, 7 languages, 1,000 examples each)

Our harness run: 0-shot, Gemini 3.1 Flash-Lite and Gemini 3 Flash. System card results for Claude and Gemini 3 Pro included for context (reasoning-enabled, 11 languages) — methodology differs, see [results/milu/README.md](results/milu/README.md).

| Model | Average Accuracy | Languages | Notes |
|-------|-----------------|-----------|-------|
| Gemini 3 Pro | **93.2%** | 11 (10 Indic + English) | System card, reasoning enabled |
| Claude Sonnet 4.6 | **89.6%** | 11 | System card, reasoning enabled |
| Claude Opus 4.6 | **89.6%** | 11 | System card, reasoning enabled |
| GPT-5.2 Pro | **89.2%** | 11 | System card, reasoning enabled |
| Claude Sonnet 4.5 | **87.6%** | 11 | System card, reasoning enabled |
| Gemini 3.1 Flash-Lite | **85.2%** | 7 | Our harness, 0-shot |
| Gemini 3 Flash | *(scheduled)* | 7 | Our harness, 0-shot |

**Per-language breakdown (our harness):**

| Language | Gemini 3.1 Flash-Lite | Gemini 3 Flash |
|----------|:---------------------:|:--------------:|
| Bengali | 88.8% | *(scheduled)* |
| Marathi | 88.7% | *(scheduled)* |
| English | 86.2% | *(scheduled)* |
| Telugu | 84.7% | *(scheduled)* |
| Tamil | 84.1% | *(scheduled)* |
| Hindi | 83.7% | *(scheduled)* |
| Punjabi | 80.0% | *(scheduled)* |

Full results and system card comparison: [results/milu/README.md](results/milu/README.md)

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
python run_eval.py                                                                    # belebele, all 3 primary models
python run_eval.py --benchmarks global_mmlu --benchmarks milu                        # new benchmarks, all models
python run_eval.py --models gemini_flash_lite --models gemini_flash \
    --benchmarks global_mmlu --benchmarks milu                                       # flash comparison
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
python run_eval.py --models gemini_flash_lite --models gemini_flash
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
