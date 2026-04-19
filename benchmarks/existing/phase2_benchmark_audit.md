# Phase 2: Benchmark Audit — Existing Multilingual Benchmarks

**Date:** April 2026  
**Scope:** Major multilingual NLP benchmarks; coverage mapped against top-20 global speaker languages  
**Models of interest:** Claude Opus 4.7 · GPT-5.4 · Gemini 3.1 Pro

---

## Target Languages (Top 20 by Global Speakers)

| # | Language | Script Family | Family |
|---|----------|--------------|--------|
| 1 | Mandarin Chinese | Logographic | Sino-Tibetan |
| 2 | Spanish | Latin | Indo-European |
| 3 | English | Latin | Indo-European |
| 4 | Hindi | Devanagari | Indo-European |
| 5 | Arabic | Arabic | Afro-Asiatic |
| 6 | Bengali | Bengali | Indo-European |
| 7 | Portuguese | Latin | Indo-European |
| 8 | Russian | Cyrillic | Indo-European |
| 9 | Japanese | Mixed (Kanji/Kana) | Japonic |
| 10 | Punjabi | Gurmukhi / Shahmukhi | Indo-European |
| 11 | Marathi | Devanagari | Indo-European |
| 12 | Telugu | Telugu | Dravidian |
| 13 | Turkish | Latin | Turkic |
| 14 | Tamil | Tamil | Dravidian |
| 15 | Vietnamese | Latin + diacritics | Austroasiatic |
| 16 | Korean | Hangul | Koreanic |
| 17 | French | Latin | Indo-European |
| 18 | German | Latin | Indo-European |
| 19 | Urdu | Arabic (Nastaliq) | Indo-European |
| 20 | Indonesian | Latin | Austronesian |

---

## Benchmark Catalog

### 1. Global-MMLU / MMMLU (Multilingual MMLU)

| Field | Detail |
|-------|--------|
| **Task type** | Multiple-choice knowledge QA (57 academic subjects) |
| **Languages** | 42 languages. Top-20 covered: Mandarin, Spanish, English, Hindi, Arabic, Bengali, Portuguese, Russian, Japanese, French, German, Turkish, Korean, Indonesian — **14/20** |
| **Top-20 gaps** | Punjabi, Marathi, Telugu, Tamil, Vietnamese, Urdu |
| **Metric** | Accuracy (%) — 0-shot and 5-shot |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | ~100% normalized (MMLU-ProX leaderboard) |
| **Gemini 3.1 Pro** | 92.6% (MMMLU aggregate) |
| **Limitations** | Translated from English; cultural bias; benchmark saturation for frontier models |

---

### 2. FLORES-200

| Field | Detail |
|-------|--------|
| **Task type** | Machine translation (sentence-level parallel corpus) |
| **Languages** | 200 languages. **All 20/20 top-20 covered** |
| **Top-20 gaps** | None |
| **Metric** | spBLEU, chrF++ |
| **Claude Opus 4.7** | Not published (Claude 3 Opus had data contamination concerns) |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Translation-only; Wikimedia/news source sentences; uneven reference translation quality for low-resource langs; does not test comprehension or reasoning |

---

### 3. MGSM (Multilingual Grade School Math)

| Field | Detail |
|-------|--------|
| **Task type** | Mathematical reasoning — arithmetic word problems |
| **Languages** | 10: Spanish, English, French, German, Russian, Japanese, Mandarin, Thai, Bengali, Swahili. Top-20 covered: Spanish, English, French, German, Russian, Japanese, Mandarin, Bengali — **8/20** |
| **Top-20 gaps** | Hindi, Arabic, Portuguese, Punjabi, Marathi, Telugu, Turkish, Tamil, Vietnamese, Korean, Urdu, Indonesian |
| **Metric** | Exact match accuracy (%) |
| **Claude Opus 4.7** | Not published (Claude 3 Opus: >90% avg 0-shot) |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | ~100% normalized (BenchLM, 35% weight in score) |
| **Limitations** | Only 10 languages; translated from English GSM8K; 250 problems/language (small); 12 of top-20 entirely absent |

---

### 4. MMLU-ProX

| Field | Detail |
|-------|--------|
| **Task type** | Cross-language professional knowledge QA (harder than MMLU) |
| **Languages** | ~10–15 languages (exact list varies by version; covers major European + some Asian) |
| **Top-20 gaps** | Punjabi, Marathi, Telugu, Tamil, Urdu, Vietnamese likely absent |
| **Metric** | Accuracy (%) |
| **Claude Opus 4.7** | ~100% normalized (BenchLM, 65% weight in score) |
| **GPT-5.4** | ~100% normalized |
| **Gemini 3.1 Pro** | ~100% normalized |
| **Limitations** | New benchmark (2025); language coverage still limited; 65% of BenchLM's multilingual score weight concentrated here; leaderboard normalization obscures actual differences |

---

### 5. BenchMAX

| Field | Detail |
|-------|--------|
| **Task type** | Multi-task: instruction following, code generation, reasoning (math+science), long-context QA (128k), tool use, translation |
| **Languages** | 17: English, Spanish, French, German, Russian, Bengali, Japanese, Thai, Swahili, Chinese, Telugu, Arabic, Korean, Serbian, Czech, Hungarian, Vietnamese. Top-20 covered: Spanish, English, French, German, Russian, Bengali, Japanese, Chinese, Telugu, Arabic, Korean, Vietnamese — **12/20** |
| **Top-20 gaps** | Hindi, Portuguese, Punjabi, Marathi, Turkish, Tamil, Urdu, Indonesian |
| **Metric** | Task-specific (accuracy, pass@k, ROUGE, win-rate) |
| **Claude Opus 4.7** | Not evaluated in original paper |
| **GPT-5.4** | Not evaluated in original paper |
| **Gemini 3.1 Pro** | Not evaluated in original paper |
| **Limitations** | Published February 2025; frontier models not yet evaluated; heterogeneous metrics make cross-task aggregation difficult |
| **Source** | [arXiv:2502.07346](https://arxiv.org/html/2502.07346v1) |

---

### 6. XCOPA (Cross-lingual Choice of Plausible Alternatives)

| Field | Detail |
|-------|--------|
| **Task type** | Commonsense reasoning — 2-choice causal/temporal classification |
| **Languages** | 11: English, Italian, Indonesian, Vietnamese, Mandarin, Hindi, Turkish, Tamil, Thai, Swahili, Haitian Creole. Top-20: English, Indonesian, Vietnamese, Mandarin, Hindi, Turkish, Tamil — **7/20** |
| **Top-20 gaps** | Spanish, Arabic, Bengali, Portuguese, Russian, Japanese, Punjabi, Marathi, Telugu, Korean, French, German, Urdu |
| **Metric** | Accuracy (%) |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | 500 examples/language (very small); translated from English COPA; no culturally authentic reasoning |

---

### 7. XStoryCloze

| Field | Detail |
|-------|--------|
| **Task type** | Narrative commonsense reasoning — story completion (2-choice) |
| **Languages** | 11: Russian, Mandarin, Spanish, Arabic, Hindi, Indonesian, Telugu, Swahili, Basque, Burmese, Yoruba. Top-20: Russian, Mandarin, Spanish, Arabic, Hindi, Indonesian, Telugu — **7/20** |
| **Top-20 gaps** | English (train only), Bengali, Portuguese, Japanese, Punjabi, Marathi, Turkish, Tamil, Vietnamese, Korean, French, German, Urdu |
| **Metric** | Accuracy (%) |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Translated from English StoryCloze; Western cultural narratives; very small test sets |

---

### 8. XNLI (Cross-lingual Natural Language Inference)

| Field | Detail |
|-------|--------|
| **Task type** | Natural language inference — 3-class (entailment/neutral/contradiction) |
| **Languages** | 15: English, French, Spanish, German, Russian, Arabic, Mandarin, Bulgarian, Greek, Hindi, Swahili, Thai, Turkish, Urdu, Vietnamese. Top-20: English, French, Spanish, German, Russian, Arabic, Mandarin, Hindi, Turkish, Urdu, Vietnamese — **11/20** |
| **Top-20 gaps** | Bengali, Portuguese, Japanese, Punjabi, Marathi, Telugu, Tamil, Korean, Indonesian |
| **Metric** | Accuracy (%) |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Translated from English MultiNLI; translation artifacts; saturated for frontier LLMs (>90% avg); 2018 benchmark — low diagnostic value for modern models |

---

### 9. XTREME / XTREME-R

| Field | Detail |
|-------|--------|
| **Task type** | Multi-task suite: NLI, QA, NER, POS, dependency parsing, sentence retrieval |
| **Languages** | 40 (XTREME) / 50 (XTREME-R). Top-20: English, French, Spanish, German, Russian, Arabic, Mandarin, Hindi, Turkish, Urdu, Vietnamese, Japanese, Korean, Indonesian, Tamil, Telugu — **16/20** |
| **Top-20 gaps** | Bengali, Punjabi, Marathi |
| **Metric** | Task-specific F1/accuracy; macro-average |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Designed for encoder models; generative LLMs rarely formally submitted; several sub-tasks ill-suited for generative models; many tasks saturated |

---

### 10. TyDiQA (Typologically Diverse Question Answering)

| Field | Detail |
|-------|--------|
| **Task type** | Extractive/abstractive QA — natively authored questions per language |
| **Languages** | 11: English, Arabic, Bengali, Finnish, Indonesian, Japanese, Korean, Russian, Swahili, Telugu, Thai. Top-20: English, Arabic, Bengali, Indonesian, Japanese, Korean, Russian, Telugu — **8/20** |
| **Top-20 gaps** | Mandarin, Spanish, Hindi, Portuguese, Punjabi, Marathi, Turkish, Tamil, Vietnamese, French, German, Urdu |
| **Metric** | F1, Exact Match |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Mostly extractive; missing Mandarin and Spanish (two largest languages); GoldP task constrains context to single passage |
| **Strength** | Only major benchmark with natively authored (non-translated) questions across languages |

---

### 11. BLEnD (Benchmark for Language-Embedded Diverse Knowledge)

| Field | Detail |
|-------|--------|
| **Task type** | Everyday cultural/factual knowledge QA grounded in local contexts |
| **Languages** | ~52 languages. Top-20 approx: Korean, Japanese, Arabic, Hindi, Indonesian, Turkish, French, German, Spanish, Mandarin — **~12/20** |
| **Top-20 gaps** | Punjabi, Marathi, Telugu, Tamil, Bengali (limited), Urdu (limited) |
| **Metric** | Exact match / F1 |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | 2024 benchmark; limited adoption; South Asian language coverage uneven |

---

### 12. INCLUDE

| Field | Detail |
|-------|--------|
| **Task type** | Multiple-choice knowledge QA across diverse domains (underrepresented languages focus) |
| **Languages** | 44 languages. Top-20 coverage: Hindi, Bengali, Urdu, Tamil, Telugu, Marathi, and others — strong South Asian coverage |
| **Top-20 gaps** | Punjabi (limited); most top-20 present |
| **Metric** | Accuracy (%) |
| **Claude Opus 4.7** | Not published (frontier models in original 2024 paper show 60–70% avg) |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | MCQ format; uneven question quality across languages; limited to classification format |

---

### 13. IndicGenBench / IndicBench

| Field | Detail |
|-------|--------|
| **Task type** | Generation: summarization, translation, QA, cross-lingual QA (Indic focus) |
| **Languages** | 29 Indic languages. Top-20: Hindi, Bengali, Marathi, Telugu, Tamil, Urdu, Punjabi — **7/20** |
| **Top-20 gaps** | All non-Indic top-20 languages |
| **Metric** | ROUGE, chrF, exact match |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Indic-only scope; generation metrics (ROUGE) imperfect proxies for quality |

---

### 14. Belebele

| Field | Detail |
|-------|--------|
| **Task type** | Reading comprehension — MCQ across 122 language variants |
| **Languages** | 122 languages and variants. **All 20/20 top-20 covered**, including Punjabi in both scripts (Gurmukhi and Shahmukhi) |
| **Top-20 gaps** | None |
| **Metric** | Accuracy (%) |
| **Claude Opus 4.7** | Not published (frontier models generally ~80–82% avg) |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | All passages are parallel translations of FLORES-200 source material; MCQ only; does not test generation or open-ended reasoning |

---

### 15. SIB-200

| Field | Detail |
|-------|--------|
| **Task type** | Topic classification (7 classes) |
| **Languages** | 200 languages. **All 20/20 top-20 covered** |
| **Top-20 gaps** | None |
| **Metric** | Accuracy (%) |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Very simple task — near-ceiling performance for frontier models; not diagnostic of complex capabilities |

---

### 16. MEGA (Multilingual Evaluation of Generative AI)

| Field | Detail |
|-------|--------|
| **Task type** | Multi-task suite across 16 tasks: NLI, QA, commonsense, summarization, MT |
| **Languages** | 70+ languages. Top-20 approx: English, Hindi, Bengali, Arabic, Portuguese, Spanish, French, German, Russian, Turkish, Vietnamese, Japanese, Korean, Indonesian, Urdu — **~15/20** |
| **Top-20 gaps** | Mandarin, Punjabi, Marathi, Telugu, Tamil |
| **Metric** | Task-specific (accuracy, F1, ROUGE, chrF) |
| **Claude Opus 4.7** | Not published |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Not published |
| **Limitations** | Aggregates existing benchmarks — inherits their limitations; not a unified leaderboard |

---

### 17. WMT (Workshop on Machine Translation — Annual)

| Field | Detail |
|-------|--------|
| **Task type** | Machine translation (primarily news domain) |
| **Languages** | Varies by year. WMT24: English, German, Czech, Japanese, Russian, Spanish, Mandarin, Hindi, Ukrainian. Top-20: English, German, Japanese, Russian, Spanish, Mandarin, Hindi — **7/20** |
| **Top-20 gaps** | Bengali, Punjabi, Marathi, Telugu, Turkish, Tamil, Vietnamese, Korean, French (rare), Urdu, Indonesian, Portuguese, Arabic |
| **Metric** | BLEU, chrF, COMET, MQM (human) |
| **Claude Opus 4.7** | Not published (Claude 3.5 ranked 1st in 9/11 WMT24 pairs) |
| **GPT-5.4** | Not published |
| **Gemini 3.1 Pro** | Gemini 2.5 predecessor: BLEURT 71.7 (WMT23) |
| **Limitations** | News-domain only; language pair selection biased toward European/East Asian; inconsistent year-to-year language coverage |

---

### 18. AI Language Proficiency Monitor

| Field | Detail |
|-------|--------|
| **Task type** | Multi-task: translation, QA, math, reasoning — aggregated from FLORES+, MMLU, GSM8K, TruthfulQA, ARC |
| **Languages** | Up to 200 languages; focuses on low-resource languages |
| **Top-20 gaps** | Comprehensive; likely covers all 20 |
| **Metric** | Composite proficiency score |
| **Claude Opus 4.7** | Unknown |
| **GPT-5.4** | Unknown |
| **Gemini 3.1 Pro** | Unknown |
| **Source** | [arXiv:2507.08538](https://arxiv.org/html/2507.08538v1) |
| **Limitations** | Aggregated from existing benchmarks; methodology still evolving |

---

## Coverage Matrix: Top-20 Languages × Benchmarks

| Language | FLORES-200 | Belebele | SIB-200 | MMMLU | MGSM | MMLU-ProX | BenchMAX | XNLI | XCOPA | XStoryCloze | TyDiQA | XTREME | INCLUDE | IndicBench | BLEnD | WMT | **Total** |
|----------|-----------|---------|---------|-------|------|-----------|---------|------|-------|------------|--------|--------|---------|-----------|-------|-----|---------|
| Mandarin | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | **14** |
| Spanish | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | **13** |
| English | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | **15** |
| Hindi | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | **13** |
| Arabic | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | **12** |
| Bengali | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | — | **9** |
| Portuguese | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | — | ✓ | — | — | — | — | **7** |
| Russian | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | **13** |
| Japanese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | **13** |
| Punjabi | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | — | — | ✓ | ✓ | — | — | **5** |
| Marathi | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | — | — | ✓ | ✓ | — | — | **5** |
| Telugu | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | **9** |
| Turkish | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | **9** |
| Tamil | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | **7** |
| Vietnamese | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | **9** |
| Korean | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | — | **11** |
| French | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | — | — | **11** |
| German | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | — | ✓ | **12** |
| Urdu | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | **7** |
| Indonesian | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | **11** |

---

## Language Coverage Ranking (Least → Most Covered)

| Rank | Language | Benchmark Count | Critical Gap |
|------|----------|-----------------|--------------|
| 1 (lowest) | **Punjabi** | 5 | Present only in FLORES-200, Belebele, SIB-200, INCLUDE, IndicBench — no reasoning or generation benchmarks |
| 2 | **Marathi** | 5 | Same as Punjabi — confined to Indic-specific benchmarks |
| 3 | **Tamil** | 7 | No math, no knowledge QA (MMMLU), limited reasoning |
| 4 | **Urdu** | 7 | No math, no knowledge QA, limited generation |
| 5 | **Portuguese** | 7 | Surprisingly low given 236M speakers — absent from reasoning benchmarks |
| 6 | **Telugu** | 9 | Better than Tamil/Urdu due to TyDiQA and XStoryCloze, but no math |
| 7 | **Vietnamese** | 9 | No knowledge QA, no math |
| 8 | **Bengali** | 9 | MGSM present, but no cultural, generation, or multi-turn tasks |
| 9 | **Turkish** | 9 | No math (MGSM), no generation benchmarks |
| 10 | **Korean** | 11 | Reasonable coverage but no open-ended generation benchmark |

---

## Task Type Coverage Summary

| Task Type | Coverage | Well-Covered Languages | Gap |
|-----------|----------|----------------------|-----|
| Machine Translation | Good | All 20 (FLORES-200) | Translation ≠ comprehension |
| Reading Comprehension (MCQ) | Good | All 20 (Belebele), 8 (TyDiQA natively authored) | MCQ doesn't test generation |
| Knowledge QA (MCQ) | Moderate | 14/20 (MMMLU) | Punjabi, Marathi, Tamil, Telugu, Vietnamese, Urdu absent |
| Mathematical Reasoning | Poor | 8/20 (MGSM) + partial extensions | 12 of top-20 absent |
| Commonsense Reasoning | Poor–Moderate | 7–11/20 (XCOPA, XStoryCloze) | South Asian and European langs thin |
| Natural Language Inference | Moderate | 11/20 (XNLI) | Saturated; limited diagnostic value |
| Open-ended Generation | **Very Poor** | ~9 languages (MT-Bench variants) | No standardized benchmark with top-20 coverage |
| Cultural Knowledge QA | **Poor** | ~10 languages (BLEnD, scattered) | Fragmented; no comprehensive benchmark |
| Multi-turn Dialogue | **Very Poor** | ~9 languages | No robust multilingual multi-turn benchmark |
| Long-context Understanding | **Very Poor** | English primarily | Almost nonexistent in multilingual settings |
| Instruction Following | **Poor** | ~10–16 languages (Okapi, BenchMAX) | Not standardized; no frontier model scores |
| Code Generation (multilingual NL→code) | **Very Poor** | English-centric | MultiPL-E tests programming languages, not natural language |
| Summarization | Poor | ~10–15 languages | Results not comparable across papers |

---

## Key Findings

### Finding 1: Two benchmarks cover all 20 languages — but both have critical limitations
FLORES-200 and Belebele cover all 20 target languages. However:
- FLORES-200 tests translation only, not comprehension or reasoning
- Belebele is MCQ over FLORES-sourced passages — both are effectively translation-artifact benchmarks

### Finding 2: Math reasoning is the starkest gap
MGSM covers only 8/20 languages. The 12 missing include Hindi (600M+ speakers), Arabic (380M+), Portuguese (236M+), and the entire South Asian and Southeast Asian block. No frontier model has published multilingual math scores for Punjabi, Marathi, Tamil, Telugu, or Urdu.

### Finding 3: Open-ended generation is essentially unmeasured at scale
No standardized multilingual benchmark evaluates free-form generation quality across the top-20 languages with reliable scoring. MT-Bench variants exist but are unstandardized, cover ~9 languages, and use LLM-as-judge (GPT-4) in English — an evaluation bias concern.

### Finding 4: Cultural knowledge is a known gap with poor tooling
BLEnD (2024) is the best available cultural knowledge benchmark, but South Asian language coverage is thin, and its adoption by major labs is limited. No frontier model has published BLEnD scores.

### Finding 5: None of the three target models publish comprehensive multilingual scores
Claude Opus 4.7, GPT-5.4, and Gemini 3.1 Pro have not published per-language scores on MGSM, FLORES-200, Belebele, TyDiQA, XCOPA, or BLEnD. The only published multilingual metrics are MMMLU aggregate (Gemini 3.1 Pro: 92.6%) and normalized leaderboard scores (BenchLM.ai).

---

## Sources

- [BenchMAX (arXiv:2502.07346)](https://arxiv.org/html/2502.07346v1)
- [BenchLM Multilingual Leaderboard](https://benchlm.ai/multilingual)
- [Artificial Analysis Multilingual](https://artificialanalysis.ai/models/multilingual)
- [MMLU-ProX (arXiv:2503.10497)](https://arxiv.org/html/2503.10497v1)
- [AI Language Proficiency Monitor (arXiv:2507.08538)](https://arxiv.org/html/2507.08538v1)
- [Multilingual Evaluations in LLMs — Medium](https://medium.com/@vbsowmya/multilingual-evaluations-in-llms-a-comparison-1d58b0fd9848)
- [MGSM Leaderboard](https://llm-stats.com/benchmarks/mgsm)
- [MMMLU Leaderboard](https://llm-stats.com/benchmarks/mmmlu)
