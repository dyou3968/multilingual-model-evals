# Phase 1: Literature Review — Multilingual Capabilities

**Date:** April 2026  
**Models:** Claude Opus 4.7 · GPT-5.4 · Gemini 3.1 Pro  
**Scope:** Official technical reports, model cards, system cards, blog posts, and supplementary community/third-party evaluations

## Release Timeline

| Model | Release Date | Multilingual Positioning |
|-------|-------------|--------------------------|
| Gemini 3.1 Pro | Feb 20, 2026 (preview) | First to land; set "13 of 16 benchmarks" narrative |
| GPT-5.4 | Mar 5, 2026 (Thinking + Pro); mini/nano Mar 17 | Positioned around agentic/computer-use gains, not multilingual |
| Claude Opus 4.7 | Apr 16, 2026 | Anthropic's retake; strongest coding, claimed to close multilingual gap |

---

## 1. Claude Opus 4.7 (Anthropic)

### Sources
- [Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude Opus 4.7 (model page)](https://www.anthropic.com/claude/opus)
- [Introducing Claude 4 (family)](https://www.anthropic.com/news/claude-4)
- [Claude 3 Model Card (predecessor baseline)](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)

### Multilingual Claims
Anthropic's Opus 4.7 announcement focuses on coding, vision, long-context, and agentic performance. **No dedicated multilingual section is disclosed** in the Opus 4.7 release materials, but third-party evaluations fill in some scores.

**Notable: Claude Opus 4.7 shipped with a new tokenizer.** Tokenizer efficiency on non-Latin scripts (Indic, Amharic, Thai) is a leading indicator of low-resource behavior and pricing — fewer tokens per character means lower cost and better context utilization for these scripts. This is the most practically significant multilingual-relevant change in the Opus 4.7 release even though it was not framed as a multilingual feature.

General model-level claims (from broader Claude documentation):
- Claude models support multilingual text input and output
- Strong capability in high-resource languages: English, French, German, Spanish, Portuguese, Japanese, Mandarin Chinese, Korean, Arabic, Hindi

### Benchmark Scores (Opus 4.7)
| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMMLU (14-language translated MMLU) | **91.5%** | Third-party / community eval |
| Global-MMLU-Lite (culturally rebalanced) | **~92.2%** | Based on 4.6 baseline; 4.7 marginally higher |
| SWE-bench Multilingual | **80.5%** | Coding benchmark — less language-sensitive |
| MMLU (English baseline) | **92.4%** | Reference point |
| MGSM | Not disclosed | No published score |

### Predecessor Baseline (Claude 3 Opus — for comparison)
| Benchmark | Score | Languages |
|-----------|-------|-----------|
| MGSM (0-shot) | >90% | 10 languages (avg) |
| MMMLU | >80% | German, Spanish, French, Italian, Dutch, Russian confirmed |
| FLORES-200 | Competitive; data contamination noted by researchers | 200 languages |
| WMT24 | 1st in 9/11 language pairs (Claude 3.5) | News translation |
| Machine translation (Lokalise 2025 blind study) | 78% rated "good" by professional translators | Multiple languages |

### Languages Mentioned
French, German, Spanish, Portuguese, Japanese, Mandarin Chinese, Korean, Arabic, Hindi (from general Claude documentation). No explicit top-20 language-by-language breakdown published for Opus 4.7.

### Training Data
Anthropic does not disclose multilingual training data composition publicly.

### Known Limitations / Caveats
- No per-language breakdown published for Opus 4.7
- Researchers have flagged potential FLORES-200 data contamination for Claude models
- Release notes emphasize coding and agentic workflows — multilingual capability treated as implicit rather than benchmarked
- Self-reported "multilingual support" lacks specificity on low-resource languages

---

## 2. GPT-5.4 (OpenAI)

### Sources
- [Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)
- [GPT-5 System Card (August 2025)](https://arxiv.org/html/2601.03267v1)
- [GPT-5.4 — Wikipedia](https://en.wikipedia.org/wiki/GPT-5.4)
- [GPT-5.4 — NxCode Guide](https://www.nxcode.io/resources/news/gpt-5-4-complete-guide-features-pricing-models-2026)
- [GPT-5: A Model Made for Multicultural Content? — MultiLingual](https://multilingual.com/gpt-5-multicultural-content/)

### Release
Released March 5, 2026. Available in variants: GPT-5.4 Thinking, GPT-5.4 Pro, GPT-5.4 mini, GPT-5.4 nano.

### Multilingual Claims
- Improved multilingual performance over GPT-4 and o1 claimed, but **multilingual disclosure is the thinnest of the three labs**
- "Responses sound more natural across accents and speech patterns" in Spanish, Hindi, Japanese, Arabic
- Community evals suggest GPT-5.x shows "modest or flat" multilingual gains vs GPT-5 — the jump went to agentic/computer-use, not languages
- Builds on GPT-5 System Card multilingual evaluations (August 2025 baseline)

### Benchmark Scores
The GPT-5 System Card (the most detailed public multilingual evaluation, baseline for GPT-5.4) reports **MMLU 0-shot across 14 languages** using professional human translations:

| Language | gpt-5-thinking | gpt-5-main | o3-high (reference) |
|----------|---------------|------------|---------------------|
| Arabic | ~0.87 | ~0.82 | ~0.88 |
| Bengali | ~0.85 | ~0.78 | ~0.83 |
| Chinese (Simplified) | ~0.88 | ~0.84 | ~0.89 |
| French | ~0.90 | ~0.87 | 0.906 |
| German | ~0.90 | ~0.86 | ~0.90 |
| Hindi | ~0.87 | ~0.82 | ~0.87 |
| Indonesian | 0.909 (highest) | ~0.83 | ~0.89 |
| Italian | ~0.90 | ~0.86 | ~0.90 |
| Japanese | ~0.88 | ~0.83 | ~0.88 |
| Korean | ~0.88 | ~0.83 | ~0.88 |
| Portuguese (Brazil) | ~0.90 | 0.879 (highest) | ~0.90 |
| Spanish | ~0.90 | ~0.86 | ~0.90 |
| Swahili | ~0.82 | ~0.70 | ~0.81 |
| Yoruba | 0.806 (lowest) | 0.664 (lowest) | 0.780 (lowest) |

*Note: Exact per-language figures for GPT-5.4 not separately published; GPT-5 System Card figures used as baseline.*

**Standard multilingual benchmark scores (third-party):**
| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMMLU | Not publicly reported | Lab has not published |
| Global-MMLU-Lite | Not reported | Lab has not published |
| MMLU (English baseline) | **~93%** | Reference point |
| MMLU-ProX (2026 leaderboard) | ~100% normalized | Ranked #3; strong across tested languages |

### Languages Mentioned
14 tested in System Card: Arabic, Bengali, Chinese (Simplified), French, German, Hindi, Indonesian, Italian, Japanese, Korean, Portuguese, Spanish, Swahili, Yoruba.

### Training Data
Not publicly disclosed in detail. OpenAI states multilingual training data but does not provide language composition breakdown.

### Known Limitations / Caveats
- 14 languages tested is a small subset — notably absent: Russian, Turkish, Tamil, Telugu, Punjabi, Marathi, Urdu, Vietnamese, Korean (inconsistent)
- Swahili and Yoruba show meaningful performance gaps vs. European languages
- System Card evaluation uses MMLU only — no reasoning, generation, or cultural tasks multilingually
- GPT-5.4-specific multilingual breakdown not separately published from GPT-5 System Card

---

## 3. Gemini 3.1 Pro (Google DeepMind)

### Sources
- [Gemini 3.1 Pro — Google DeepMind](https://deepmind.google/models/gemini/pro/)
- [Gemini 3.1 Pro Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
- [Gemini 3.1 Pro Blog Post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [Gemini 2.5 Technical Report](https://arxiv.org/abs/2507.06261) (predecessor baseline)

### Release
Released February 19, 2026. Available via Gemini API, Vertex AI, Gemini app, and NotebookLM. Context window: up to 1M tokens.

### Multilingual Claims
- MMMLU: **92.6%** (vs. Gemini 3 Pro: 91.8%)
- Automated safety policy evaluation conducted across multiple languages (languages not specified)
- Multilingual training data from web documents, books, code, images, audio, and video
- "Natively multimodal" with multilingual comprehension across text, audio, images, video
- Slight edge in non-English languages attributed to multilingual training data from Google Search

### Benchmark Scores
| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMMLU (14-language translated MMLU) | **92.6%** | Up from Gemini 3 Pro 91.8%; Gemini's headline multilingual number |
| Global-MMLU-Lite (culturally rebalanced) | **93.2%** | Gemini's clearest multilingual win over the other two models |
| MMLU (English baseline) | **93–94%** | Reference point |
| WMT23 (predecessor) | BLEURT 71.7 | Gemini 2.5-era baseline |
| Multilingual safety | +0.11% vs. Gemini 3 Pro | Safety-specific metric only |
| MMLU-ProX | ~100% (normalized) | Ranked #2 on BenchLM leaderboard |

**Artificial Analysis multilingual leaderboard (April 2026):** Gemini 3.1 Pro Preview scored **93 overall multilingual average**, **95 in English**, **94 in Chinese, Hindi, and Spanish**.

**Notable:** Gemini 3.1 Flash TTS (companion model) ships with native support for 70+ languages — Google is the only lab putting low-resource language parity in its marketing. The Pro text model card gestures at this but does not table it.

### Languages Mentioned
Model card does not provide a specific supported-language list. Multilingual training implied through Google Search corpus. Evaluation confirmed for: Chinese, Hindi, Spanish, English (Artificial Analysis). MMMLU covers 14 languages (same set as GPT-5 System Card).

### Training Data
Not publicly disclosed at the language-distribution level. Google has stated training includes multilingual web, books, and code.

### Known Limitations / Caveats
- No per-language benchmark breakdown published for Gemini 3.1 Pro beyond MMMLU aggregate
- Multilingual safety improvement (+0.11%) is a narrow metric — not a capability benchmark
- Model card does not list supported languages explicitly
- MMMLU aggregate masks within-language variation

---

## 4. Cross-Model Comparison Summary

### Headline Benchmark Scores

| Benchmark | Claude Opus 4.7 | GPT-5.4 | Gemini 3.1 Pro | Interpretation |
|-----------|----------------|---------|----------------|----------------|
| **MMMLU** (14-lang translated MMLU) | 91.5% | not reported | 92.6% | ~1pt delta; practitioners consider this range saturated |
| **Global-MMLU-Lite** (culturally rebalanced) | ~92.2% | not reported | **93.2%** | Gemini's clearest win; ~1pt advantage |
| **SWE-bench Multilingual** (coding) | **80.5%** | not reported | 80.6% overall | Effectively tied; coding less language-sensitive |
| **MMLU** (English baseline) | 92.4% | ~93% | 93–94% | English↔multilingual gap has narrowed significantly |

**Key takeaway from the PDF:** At the high-resource end, multilingual is a **three-way tie within noise**. The narrative of Gemini "leading" rests on a ~1-point delta on benchmarks most practitioners consider saturated. GPT-5.4 multilingual scores are largely not public — comparisons that pit it against Opus 4.7 and Gemini 3.1 Pro on MMMLU rely on either GPT-5.2 numbers or third-party reproductions.

### Per-Model Qualitative Findings

| Dimension | Claude Opus 4.7 | GPT-5.4 | Gemini 3.1 Pro |
|-----------|----------------|---------|----------------|
| **Multilingual transparency** | Thin — no per-language scores published | Thinnest of all three | Moderate — MMMLU aggregate + safety note |
| **Official multilingual benchmark** | None in release materials | MMLU (14 langs, GPT-5 baseline) | MMMLU 92.6%, Global-MMLU-Lite 93.2% |
| **Tokenizer** | **New tokenizer shipped** — directly improves non-Latin script quality and pricing | No disclosed tokenizer change | Not disclosed |
| **Low-resource marketing** | Not mentioned | Not mentioned | Gemini 3.1 Flash TTS: 70+ native languages |
| **INCLUDE (third-party eval)** | Stronger on **cultural register / tone** | Stronger on **structured reasoning** in translated tasks | Stronger on **region-specific factual recall** |
| **Perceived generation quality** | Outputs read more naturally in Korean/Japanese despite lower QA scores | — | Higher QA scores; lower perceived naturalness per user reports |
| **Multilingual focus in release** | Coding + agentic; multilingual implicit | Agentic + computer-use; multilingual not mentioned | Broad; multilingual explicitly cited |

### Key Observation
All three labs cherry-pick benchmarks in their release narratives: "13 of 16 wins" (Gemini), "beats GPT-5.4 and Gemini 3.1 Pro on most benchmarks" (Anthropic) — both can be simultaneously true on different benchmark sets. **None of the three models publishes a per-language breakdown across the full top-20.** This project fills that gap.

### Methodological Caveats (from source document)
- All three models' numbers come from lab-published technical reports using different prompting, eval harnesses, and shot counts — direct comparison is approximate
- Gemini 3.1 Pro has been in preview since February; GA scores may shift
- GPT-5.4 MMMLU comparisons rely on GPT-5.2 numbers or third-party reproductions, not official GPT-5.4 disclosures

This is a significant gap — and a direct motivation for this project.

---

## 5. Gaps Identified in Literature (Input to Phase 3)

1. **No model discloses per-language scores for all top-20 languages** — Punjabi, Marathi, Telugu, Tamil, Vietnamese, Urdu are entirely absent from published evaluations for all three models
2. **Evaluation limited to MCQ (MMLU format)** — reasoning, generation, cultural tasks, and multi-turn dialogue are not evaluated multilingually in any official report
3. **No cross-model comparison on the same benchmark** — each company uses different benchmarks, making head-to-head comparison impossible from public data alone
4. **Low-resource and South Asian language blindspot** — all three companies effectively ignore the ~600M speaker block of Punjabi, Marathi, Telugu, Tamil, Urdu in their public evaluations
5. **No evaluation of instruction-following quality in non-English** — all three reports use knowledge QA (MCQ), not generation or instruction tasks
6. **Self-evaluation bias unaddressed** — none of the three companies uses multi-judge or cross-model evaluation for multilingual tasks

---

*Sources referenced throughout:*
- [Anthropic Claude Opus 4.7 announcement](https://www.anthropic.com/news/claude-opus-4-7)
- [GPT-5 System Card (arXiv)](https://arxiv.org/html/2601.03267v1)
- [GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/)
- [Gemini 3.1 Pro model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
- [Gemini 3.1 Pro blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [BenchLM Multilingual Leaderboard](https://benchlm.ai/multilingual)
- [Artificial Analysis Multilingual](https://artificialanalysis.ai/models/multilingual)
- [GPT-5: Multicultural Content? (MultiLingual)](https://multilingual.com/gpt-5-multicultural-content/)
