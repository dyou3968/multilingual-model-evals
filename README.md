# Multilingual Model Evaluations

A benchmarking harness comparing **Claude Opus 4.7**, **GPT-5.4**, and **Gemini 3.1 Pro** across the top 20 global speaker languages on the Tier 1 benchmark suite.

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
│       ├── belebele.py          # Reading comprehension MCQ
│       ├── mgsm.py              # Math (8-shot chain-of-thought)
│       ├── include.py           # Regional exam MCQ
│       ├── blend.py             # Cultural knowledge (MCQ + short-answer)
│       └── indicgenbench.py     # Summarization, translation, cross-lingual QA
├── docs/
│   └── architecture.md          # System architecture diagram
├── benchmarks/
│   ├── existing/                # Phase 2 benchmark audit
│   └── gap_analysis/            # Phase 3 gap analysis
└── literature/                  # Phase 1 literature review
```

## Benchmark Suite (Tier 1)

| Benchmark | Task | Languages | Scoring |
|-----------|------|-----------|---------|
| [Belebele](https://huggingface.co/datasets/facebook/belebele) | Reading comprehension MCQ | 20 | Exact match |
| [MGSM](https://huggingface.co/datasets/juletxara/mgsm) | Math word problems (8-shot) | 10 | Numeric extraction |
| [INCLUDE](https://huggingface.co/datasets/Cohere/include-mit) | Regional exam MCQ | ~15 | Exact match |
| [BLEnD](https://huggingface.co/datasets/nyu-mll/blend) | Cultural knowledge MCQ + short-answer | 16 | Exact match + judge |
| [IndicGenBench](https://huggingface.co/datasets/ai4bharat/IndicGenBench) | Summarization / Translation / QA | ~9 | ROUGE-L + chrF + judge |

## Target Languages

Top 20 by global speakers: Mandarin Chinese, Spanish, English, Hindi, Arabic, Bengali, Portuguese, Russian, Japanese, Punjabi, Marathi, Telugu, Turkish, Tamil, Vietnamese, Korean, French, German, Urdu, Indonesian.

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
GOOGLE_API_KEY=...
```

The model IDs default to `claude-opus-4-7`, `gpt-5.4`, and `gemini-3.1-pro`. Override them in `.env` if needed (e.g. to point at a different model version during testing):

```
CLAUDE_MODEL=claude-opus-4-7
OPENAI_MODEL=gpt-5.4
GEMINI_MODEL=gemini-3.1-pro
```

### 3. Verify setup (optional smoke test)

Run a single benchmark on one model and one language to confirm your keys and dependencies are working:

```bash
python run_eval.py \
  --benchmarks belebele \
  --models claude \
  --languages zho_Hans
```

You should see a progress bar and a new file at `results/belebele/claude.jsonl`.

## Running Experiments

### Full Tier 1 suite (all models, all languages)

```bash
python run_eval.py
```

Estimated cost: **~$1,000–1,500** across all three models. See [Cost Estimates](#cost-estimates) below.

### Specific benchmarks

```bash
python run_eval.py --benchmarks belebele mgsm
```

### Specific models

```bash
python run_eval.py --models claude openai
```

Model key → model ID mapping (set in `harness/config.py` and overridable via `.env`):

| Key | Default model |
|-----|---------------|
| `claude` | claude-opus-4-7 |
| `openai` | gpt-5.4 |
| `gemini` | gemini-3.1-pro |

### Specific languages

Language codes are benchmark-specific. Pass the code for the benchmark you're running:

```bash
# Belebele uses FLORES-200 codes
python run_eval.py --benchmarks belebele --languages zho_Hans hin_Deva arb_Arab

# MGSM uses ISO 639-1 codes
python run_eval.py --benchmarks mgsm --languages zh hi ar

# INCLUDE and BLEnD use language name strings
python run_eval.py --benchmarks include --languages Hindi Arabic Korean
```

### Custom output directory

```bash
python run_eval.py --results-dir /path/to/output
```

### Verbose logging

```bash
python run_eval.py --verbose
```

## Resumability

Every run is resumable. If a run is interrupted, restart with the same command — the runner reads existing JSONL files and skips any example IDs already present. You will not be double-charged for completed examples.

## Output Format

Results are written as append-only JSONL files:

**`results/<benchmark>/<model>.jsonl`** — one record per example:
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

**`results/<benchmark>/judge_scores.jsonl`** — multi-judge consensus for generation tasks:
```json
{
  "example_id": "indicgenbench_hi_summarization_0",
  "scored_model": "claude",
  "mean_score": 4.333,
  "cross_judge_mean": 4.5,
  "self_score": 4,
  "self_bias": -0.5,
  "per_judge": {"claude": 4, "openai": 5, "gemini": 4}
}
```

`self_bias = self_score − cross_judge_mean`. A positive value means a model scores its own output higher than peers do; negative means it is self-critical.

## Multi-Judge Scoring

For generation tasks (IndicGenBench summarization/translation/QA and BLEnD short-answer), automated metrics alone are insufficient. The harness runs a **multi-judge consensus** pass:

- All three models score each other's outputs on a 1–5 rubric
- Scores are aggregated into `mean_score` (all judges) and `cross_judge_mean` (excluding self)
- Self-evaluation bias is tracked explicitly and reported separately

This design means no single model controls its own evaluation score, while still preserving self-scores for analysis.

## Cost Estimates

Rough estimates at current API pricing (April 2026):

| Benchmark | Examples | Claude Opus 4.7 | GPT-5.4 | Gemini 3.1 Pro | All 3 |
|-----------|----------|----------------|---------|----------------|-------|
| Belebele | ~18,000 | ~$115 | ~$75 | ~$37 | **~$227** |
| MGSM | ~5,000 | ~$85 | ~$55 | ~$20 | **~$160** |
| INCLUDE | ~7,500 | ~$100 | ~$65 | ~$25 | **~$190** |
| BLEnD | ~8,000 | ~$90 | ~$60 | ~$22 | **~$172** |
| IndicGenBench + judge | ~2,700 | ~$135 | ~$55 | ~$40 | **~$230** |
| **Total** | | **~$525** | **~$310** | **~$144** | **~$979** |

To reduce costs during development:
- Lower `max_examples_per_language` in `harness/config.py`
- Run `--models claude` only first to validate correctness
- Use `--languages` to target a small subset before scaling up

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

- **Phase 1** — Literature review of Claude Opus 4.7, GPT-5.4, and Gemini 3.1 Pro multilingual capabilities
- **Phase 2** — Audit of 24 existing multilingual benchmarks with coverage matrix
- **Phase 3** — Gap analysis identifying 8 under-covered areas (low-resource languages, SEA, contamination risk, etc.)
- **Phase 4** — This harness: running Tier 1 benchmarks and (forthcoming) synthetic benchmark generation

See the `literature/`, `benchmarks/existing/`, and `benchmarks/gap_analysis/` directories for Phase 1–3 documents.

## License

MIT
