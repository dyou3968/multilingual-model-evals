# Evaluation Harness Architecture

```mermaid
flowchart TD
    CLI["🖥️  run_eval.py\n──────────────\nTyper CLI\n--benchmarks --models\n--languages --results-dir"]

    CLI -->|"benchmark names\nmodel keys\nlanguage codes"| Runner

    subgraph Orchestration ["harness/runner.py  —  Async Orchestrator"]
        Runner["run_all()\n────────────\niterates benchmarks\n→ run_benchmark()"]
        ResumeSem["Resumability\n────────────\nskip completed IDs\nfrom existing JSONL"]
        GenSem["asyncio.Semaphore\n────────────\nconcurrency cap\nfor API calls"]
        Runner --- ResumeSem
        Runner --- GenSem
    end

    subgraph Config ["harness/config.py  —  Central Configuration"]
        LangMap["TOP_20_LANGUAGES\n────────────────\nlanguage ↔ per-benchmark\ncode mappings"]
        ModelMap["MODELS\n────────────────\nclaude → claude-opus-4-7\nopenai → gpt-5.4\ngemini → gemini-3.1-pro"]
        BenchCfg["BENCHMARK_CONFIGS\n────────────────\nn_shots / max_examples\njudge_subset"]
    end

    subgraph DataLayer ["harness/benchmarks/  —  Benchmark Loaders"]
        direction LR
        Belebele["belebele.py\nRC + MCQ\n900 ex / lang"]
        MGSM["mgsm.py\n8-shot math\n250 ex / lang"]
        INCLUDE["include.py\nRegional MCQ\n≤500 ex / lang"]
        BLEnD["blend.py\nCultural MCQ\n+ short-answer"]
        IGB["indicgenbench.py\nSumm / Trans / QA\n3 tasks / lang"]
    end

    HF[("🤗 HuggingFace\nDatasets")]

    subgraph ClientLayer ["harness/clients/  —  Async API Clients"]
        direction LR
        Claude["claude_client.py\nAsyncAnthropic\n+ tenacity retry"]
        OAI["openai_client.py\nAsyncOpenAI\n+ tenacity retry"]
        Gem["gemini_client.py\nGenerativeAI\n+ tenacity retry"]
    end

    subgraph ScoringLayer ["Scoring"]
        AutoScore["harness/scoring.py\n──────────────────\nexact_match  mcq_correct\nnumeric_correct\nrouge_l  chrf"]
        Judge["harness/judge.py\n──────────────────\nMulti-Judge Consensus\n1–5 rubric per output\ntracks self-eval bias"]
    end

    subgraph Storage ["results/  —  Output"]
        JSONL["&lt;benchmark&gt;/&lt;model&gt;.jsonl\n──────────────────\nid · prediction · reference\nautomated scores"]
        JudgeOut["&lt;benchmark&gt;/judge_scores.jsonl\n──────────────────\nmean_score · cross_judge_mean\nself_score · self_bias · per_judge"]
    end

    HF -->|"load_dataset()"| DataLayer
    Config -->|"language codes\ndataset IDs\nexample caps"| Orchestration
    Config -->|"model IDs\nfrom env"| ClientLayer
    DataLayer -->|"list[dict]\nprompt · reference\nscoring_type"| Orchestration
    Orchestration -->|"prompt + system"| ClientLayer
    ClientLayer -->|"prediction text"| Orchestration
    Orchestration -->|"prediction + reference"| AutoScore
    AutoScore -->|"needs_judge=True\n(IndicGenBench, BLEnD SA)"| Judge
    Judge -->|"all 3 models\nscore each output"| ClientLayer
    AutoScore --> JSONL
    Judge --> JudgeOut
    Orchestration --> JSONL
```

## Layer Descriptions

### Entry — `run_eval.py`
Typer CLI. Validates benchmark/model selections, then hands off to `run_all()`. Defaults to the full Tier 1 suite across all three models.

### Orchestration — `harness/runner.py`
Core async loop. For each benchmark × language × model:
1. Checks existing JSONL for completed IDs (resumability)
2. Fires async API calls behind a concurrency semaphore
3. Scores each prediction immediately after receipt
4. Appends records to per-model JSONL
5. Batches `needs_judge` examples and runs the multi-judge pass

### Config — `harness/config.py`
Single source of truth for language code mappings (each benchmark uses a different format: FLORES-200 codes, ISO codes, or language name strings), model IDs (overridable via env), dataset IDs, and per-benchmark settings.

### Benchmark Loaders — `harness/benchmarks/`
Each class implements two methods:
- `load(language_code) → list[dict]` — fetches from HuggingFace, caps examples, builds prompt strings
- `score(prediction, example) → dict` — returns automated metric scores and `needs_judge` flag

### API Clients — `harness/clients/`
Thin async wrappers with identical interfaces (`complete(prompt, system, max_tokens, temperature)`). All three use `tenacity` for exponential-backoff retry on rate limits and transient errors.

### Scoring — `harness/scoring.py` + `harness/judge.py`
Two-pass scoring:
- **Automated** (immediate): exact match for MCQ, numeric extraction for MGSM, ROUGE-L + chrF for generation
- **Multi-judge** (deferred): all three models score each other's generation outputs on a 1–5 rubric; `ConsensusResult` records mean score, cross-judge mean, self-score, and self-bias (self_score − cross_judge_mean)

### Storage — `results/`
Append-only JSONL files. One file per benchmark × model for raw predictions and automated scores; one `judge_scores.jsonl` per benchmark for consensus results.
