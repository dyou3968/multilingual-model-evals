# Selected External Benchmarks

These are the existing benchmarks we are incorporating into this project's evaluation suite. They were chosen based on the gap analysis in Phase 3 — each addresses a specific hole in the existing landscape for the top-20 global speaker languages.

We will run Claude Opus 4.7, GPT-5.4, and Gemini 3.1 Pro against each benchmark and score them using our multi-judge consensus methodology.

---

## 1. BLEnD

**Paper:** [arXiv:2406.09948](https://arxiv.org/abs/2406.09948)  
**Full name:** Benchmark for Language-Embedded Diverse Knowledge

### Why included
BLEnD is the best available benchmark for **culturally grounded everyday knowledge** — one of the top-priority gaps from Phase 3. It tests knowledge that is genuinely local (not translatable from English) and includes both short-answer and MCQ formats, giving us a signal on open-ended cultural accuracy.

The 57.34% performance spread across cultures seen in GPT-4 is one of the starkest published findings about cultural bias in frontier models, and we want to replicate and extend that finding across all three target models.

### What we use
- Short-answer format (culturally grounded, harder to game)
- MCQ format (for cross-benchmark comparability)
- All available languages from the top-20 list: Korean, Japanese, Arabic, Hindi, Indonesian, Turkish, French, German, Spanish, Mandarin (~10/20)

### What it doesn't cover (our benchmark supplements)
- Punjabi, Marathi, Telugu, Tamil, Bengali, Urdu, Russian, Vietnamese, Portuguese — absent from BLEnD; our new benchmark will extend cultural QA to these languages

### Evaluation plan
- Run all three models in 0-shot and 5-shot settings
- Score short-answer with multi-judge consensus (all three models evaluate outputs)
- Score MCQ with exact match
- Track per-language and per-culture score variance

---

## 2. INCLUDE

**Paper:** [arXiv:2411.19799](https://arxiv.org/abs/2411.19799)  
**Full name:** INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge

### Why included
INCLUDE is the **largest authentically-sourced multilingual QA benchmark** (197,243 QA pairs across 44 languages), and critically it addresses the translation-artifact problem directly — questions come from regional exam materials, not translated English content.

It covers the most South Asian languages of any major knowledge benchmark, providing a baseline for Hindi, Bengali, Urdu, Tamil, Telugu, and Marathi that no other benchmark at this scale provides.

### What we use
- All questions for languages in our top-20 list: Hindi, Bengali, Urdu, Tamil, Telugu, Marathi, Arabic, Turkish, Indonesian, Korean, Vietnamese, and others
- MCQ format with regional domain coverage (science, social studies, language arts per country)

### What it doesn't cover (our benchmark supplements)
- Punjabi — limited in INCLUDE; our benchmark adds Punjabi coverage
- Open-ended generation and reasoning — INCLUDE is MCQ only; our new benchmark adds these task types

### Evaluation plan
- Run all three models in 0-shot and 5-shot settings
- Exact match / accuracy scoring per language
- Compare our results to any published baselines from the original paper
- Flag per-language accuracy gaps vs. the English baseline as a derived metric

---

## 3. IndicGenBench

**Paper:** [ACL Anthology 2024.acl-long.595](https://aclanthology.org/2024.acl-long.595/)  
**Full name:** IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages

### Why included
IndicGenBench is the **only generation benchmark** that covers Punjabi, Marathi, and the full suite of South Asian languages in our top-20 list. This fills the most critical task-type gap from Phase 3: open-ended generation quality for under-represented Indic languages.

It tests three distinct generation tasks (summarization, translation, cross-lingual QA), which together provide a richer signal than MCQ alone.

### What we use
- Cross-lingual summarization (English source → Indic language output): tests production quality
- Machine translation (between Indic languages): tests cross-lingual transfer
- Cross-lingual QA (English question + Indic context → English answer): tests reading comprehension
- Languages in top-20: Hindi, Bengali, Marathi, Telugu, Tamil, Urdu, Punjabi (7/20)

### What it doesn't cover (our benchmark supplements)
- Non-Indic top-20 languages — our new benchmark provides equivalent generation tasks for Mandarin, Arabic, Spanish, Russian, Japanese, Korean, French, German, Turkish, Vietnamese, Indonesian, Portuguese
- Multi-judge scoring — original paper uses ROUGE/chrF only; we apply multi-judge consensus scoring on top of metric-based scoring to capture fluency and cultural appropriateness

### Evaluation plan
- Run all three models on all three task types across the 7 Indic languages in our top-20
- Score with ROUGE-L and chrF (for comparability with published baselines)
- Additionally score with multi-judge consensus on a 500-sample subset per language (for quality signal beyond reference-based metrics)
- Compare to GPT-3.5, GPT-4, PaLM-2, LLaMA baselines from original paper

---

## Summary: Combined External Benchmark Coverage

| Language | BLEnD | INCLUDE | IndicGenBench | Combined coverage |
|----------|-------|---------|---------------|-------------------|
| Mandarin | ✓ | partial | — | Knowledge QA |
| Spanish | ✓ | partial | — | Knowledge QA |
| English | ✓ | ✓ | ✓ | Full |
| Hindi | ✓ | ✓ | ✓ | Full (knowledge + generation) |
| Arabic | ✓ | ✓ | — | Knowledge QA |
| Bengali | — | ✓ | ✓ | Knowledge + generation |
| Portuguese | — | partial | — | Limited |
| Russian | — | partial | — | Limited |
| Japanese | ✓ | partial | — | Knowledge QA |
| Punjabi | — | partial | ✓ | Generation only |
| Marathi | — | ✓ | ✓ | Knowledge + generation |
| Telugu | — | ✓ | ✓ | Knowledge + generation |
| Turkish | ✓ | ✓ | — | Knowledge QA |
| Tamil | — | ✓ | ✓ | Knowledge + generation |
| Vietnamese | — | ✓ | — | Knowledge QA |
| Korean | ✓ | ✓ | — | Knowledge QA |
| French | ✓ | partial | — | Knowledge QA |
| German | ✓ | partial | — | Knowledge QA |
| Urdu | — | ✓ | ✓ | Knowledge + generation |
| Indonesian | ✓ | ✓ | — | Knowledge QA |

**Remaining gaps after incorporating all three benchmarks** (to be filled by our new benchmark in Phase 4):
- Portuguese, Russian — sparse coverage across all three
- Punjabi — generation only (no knowledge QA)
- Math/reasoning — none of the three benchmarks cover this task type in South Asian/SEA languages
- Open-ended instruction following — not covered by any of the three
- Multi-turn dialogue — not covered by any of the three
