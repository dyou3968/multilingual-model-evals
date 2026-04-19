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
        LangMap["TOP_20_LANGUAGES\n────────────────\nlanguage name ↔\nFLORES-200 code"]
        ModelMap["MODELS\n────────────────\nclaude → claude-sonnet-4-6\nopenai → gpt-5.4-mini\ngemini → gemini-3.1-flash-lite-preview"]
        BenchCfg["BENCHMARK_CONFIGS\n────────────────\nmax_examples_per_language\ndataset ID"]
    end

    subgraph DataLayer ["harness/benchmarks/  —  Benchmark Loader"]
        Belebele["belebele.py\n────────────────\nReading comprehension MCQ\n900 examples / language\nFLORES-200 language codes\nfacebook/belebele on HF"]
    end

    HF[("🤗 HuggingFace\nDatasets")]

    subgraph ClientLayer ["harness/clients/  —  Async API Clients"]
        direction LR
        Claude["claude_client.py\nAsyncAnthropic\n+ tenacity retry"]
        OAI["openai_client.py\nAsyncOpenAI\n+ tenacity retry"]
        Gem["gemini_client.py\nGenerativeAI\n+ tenacity retry"]
    end

    subgraph ScoringLayer ["Scoring — harness/scoring.py"]
        AutoScore["mcq_correct()\n──────────────────\nextracts A/B/C/D from response\ncompares to reference letter\nreturns correct: true/false"]
    end

    subgraph Storage ["results/belebele/  —  Output"]
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
Typer CLI. Accepts `--models` and `--languages` flags (both optional — defaults to all three models and all 20 languages), then hands off to `run_all()`.

### Orchestration — `harness/runner.py`
Core async loop. For each language × model:
1. Checks existing JSONL for completed IDs (resumability — safe to interrupt and restart)
2. Fires async API calls behind a concurrency semaphore
3. Scores each prediction immediately after receipt
4. Appends records to per-model JSONL

### Config — `harness/config.py`
Central config for the 20 target languages (name → FLORES-200 code), model IDs (overridable via `.env`), and Belebele dataset settings.

### Benchmark Loader — `harness/benchmarks/belebele.py`
Loads `facebook/belebele` from HuggingFace. Each example has a passage, question, and four answer options (A–D). The loader builds the prompt string and records the correct answer letter as the reference. 900 examples per language, no few-shot prefix required.

### API Clients — `harness/clients/`
Three thin async wrappers with an identical interface (`complete(prompt, system, max_tokens, temperature)`). All use `tenacity` for exponential-backoff retry on rate limits and transient errors.

### Scoring — `harness/scoring.py`
Single-pass, fully automated. `mcq_correct()` extracts the first A/B/C/D letter from the model response and compares it to the reference. No judge pass needed.

### Storage — `results/belebele/`
Append-only JSONL. One file per model (`claude.jsonl`, `openai.jsonl`, `gemini.jsonl`). Each record contains the example ID, language code, model key, raw prediction, reference answer, and a boolean `correct` field.
