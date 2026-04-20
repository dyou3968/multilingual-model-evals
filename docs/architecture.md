# Evaluation Harness Architecture

```mermaid
flowchart TD
    CLI["🖥️  run_eval.py\n──────────────\nTyper CLI\n--models --languages\n--results-dir"]

    CLI -->|"model keys\nlanguage codes"| Runner

    subgraph Orchestration ["harness/runner.py  —  Async Orchestrator"]
        Runner["run_all()\n────────────\niterates languages\n→ run_benchmark()"]
        ResumeSem["Resumability\n────────────\nskip completed IDs\nfrom existing JSONL"]
        GenSem["asyncio.Semaphore\n────────────\nconcurrency cap\nfor API calls"]
        Runner --- ResumeSem
        Runner --- GenSem
    end

    subgraph Config ["harness/config.py  —  Central Configuration"]
        LangMap["TOP_20_LANGUAGES\n────────────────\nlanguage name ↔\nbenchmark-specific codes"]
        ModelMap["MODELS\n────────────────\nclaude → claude-sonnet-4-6\nopenai → gpt-5.4-mini\ngemini_flash_lite → gemini-3.1-flash-lite-preview\ngemini_flash → gemini-3-flash-preview"]
        BenchCfg["BENCHMARK_CONFIGS\n────────────────\nn_shots · max_examples\nscoring · dataset ID"]
    end

    subgraph DataLayer ["harness/benchmarks/  —  Benchmark Loader"]
        Belebele["belebele.py\n────────────────\nReading comprehension MCQ\n900 examples / language\nFLORES-200 language codes\nfacebook/belebele on HF"]
        GlobalMMLU["global_mmlu.py\n────────────────\nKnowledge MCQ · 57 subjects\n1,000 examples / language\nISO 639-1 codes · 16 languages\nCohereLabs/Global-MMLU on HF"]
        MILU["milu.py\n────────────────\nKnowledge MCQ · Indic languages\n1,000 examples / language\n7 languages · gated (HF_TOKEN)\nai4bharat/MILU on HF"]
    end

    HF[("🤗 HuggingFace\nDatasets")]

    subgraph ClientLayer ["harness/clients/  —  Async API Clients"]
        direction LR
        Claude["claude_client.py\nAsyncAnthropic\n+ tenacity retry\nCLAUDE_MIN_INTERVAL=2.5s"]
        OAI["openai_client.py\nAsyncOpenAI\n+ tenacity retry\nOPENAI_MIN_INTERVAL=1.0s"]
        Gem["gemini_client.py\nGenerativeAI · flash-lite\n+ tenacity retry\nGEMINI_MIN_INTERVAL=0s"]
        GemFlash["gemini_flash_client.py\nGenerativeAI · flash\n+ tenacity retry\nGEMINI_FLASH_MIN_INTERVAL=0.18s"]
    end

    subgraph ScoringLayer ["Scoring — harness/scoring.py"]
        AutoScore["mcq_correct()\n──────────────────\nextracts A/B/C/D from response\ncompares to reference letter\nreturns correct: true/false"]
    end

    subgraph Storage ["results/&lt;benchmark&gt;/  —  Output"]
        JSONL["&lt;model&gt;.jsonl\n──────────────────\nid · language · model\nprediction · reference · correct"]
    end

    HF -->|"load_dataset()\nsplit=test"| DataLayer
    Config -->|"FLORES-200 codes\nmax_examples cap"| DataLayer
    Config -->|"model IDs\nfrom env"| ClientLayer
    DataLayer -->|"list[dict]\nprompt · system\nreference"| Orchestration
    Orchestration -->|"prompt + system"| ClientLayer
    ClientLayer -->|"prediction text\n(single letter)"| Orchestration
    Orchestration -->|"prediction + reference"| AutoScore
    AutoScore -->|"correct: bool"| JSONL
    Orchestration --> JSONL
```

## Layer Descriptions

### Entry — `run_eval.py`
Typer CLI. Accepts `--benchmarks`, `--models`, and `--languages` flags (all optional — defaults to belebele and all primary models). Hands off to `run_all()`.

### Orchestration — `harness/runner.py`
Core async loop. For each benchmark × language × model:
1. Checks existing JSONL for completed IDs (resumability — safe to interrupt and restart)
2. Fires async API calls behind a concurrency semaphore (`GENERATION_CONCURRENCY`, default 3)
3. Scores each prediction immediately after receipt
4. Appends records to per-model JSONL

### Config — `harness/config.py`
Central config for the 20 target languages with per-benchmark code mappings, model IDs (overridable via `.env`), and per-benchmark settings (n_shots, max_examples, scoring type).

### Benchmark Loaders — `harness/benchmarks/`

**`belebele.py`** — Loads `facebook/belebele`. Each example has a passage, question, and four answer options (A–D). 900 examples per language across all 20 target languages.

**`global_mmlu.py`** — Loads `CohereLabs/Global-MMLU`. Knowledge MCQ covering 57 academic subjects, translated into 42 languages. Covers 16 of the 20 target languages (ISO 639-1 codes). Capped at 1,000 examples per language.

**`milu.py`** — Loads `ai4bharat/MILU` (gated — requires `HF_TOKEN`). Knowledge MCQ focused on Indic languages. Covers 7 of the 20 target languages. Capped at 1,000 examples per language. Options stored as `option1–4`, answer as the key name of the correct option (e.g. `"option2"`).

### API Clients — `harness/clients/`
Four thin async wrappers with an identical interface (`complete(prompt, system, max_tokens, temperature)`). All use `tenacity` for exponential-backoff retry on rate limits and transient errors. Each client includes a pre-request sleep (`*_MIN_INTERVAL`) tuned to its API tier's RPM limit:

| Client | Model | RPM limit | Interval |
|--------|-------|-----------|----------|
| `claude_client.py` | Claude Sonnet 4.6 | 50 (Tier 1) | 2.5s |
| `openai_client.py` | GPT-5.4 Mini | ~60 (Tier 1) | 1.0s |
| `gemini_client.py` | Gemini 3.1 Flash-Lite Preview | 4,000 | 0s |
| `gemini_flash_client.py` | Gemini 3 Flash | 1,000 | 0.18s |

### Scoring — `harness/scoring.py`
Single-pass, fully automated. `mcq_correct()` extracts the first A/B/C/D letter from the model response and compares it to the reference. No judge pass needed.

### Storage — `results/<benchmark>/`
Append-only JSONL, one directory per benchmark, one file per model (e.g. `results/belebele/claude.jsonl`). Each record contains the example ID, language code, model key, raw prediction, reference answer, and a boolean `correct` field.
