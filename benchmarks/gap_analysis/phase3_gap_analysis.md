# Phase 3: Gap Analysis — Where Existing Benchmarks Fall Short

**Date:** April 2026  
**Input:** Phase 1 (literature review) + Phase 2 (benchmark audit)  
**Output:** Prioritized gap list to guide Phase 4 benchmark design

---

## Summary

After reviewing 18+ multilingual benchmarks against the top-20 global speaker languages and three target models (Claude Opus 4.7, GPT-5.4, Gemini 3.1 Pro), we identify five high-priority gap categories. These gaps represent where a new benchmark would add the most research value.

---

## Gap 1: South Asian and Southeast Asian Languages in Reasoning Tasks

**Priority: CRITICAL**

### What's missing
The 8 languages below — representing approximately 1.4 billion native speakers — are absent from every published mathematical and commonsense reasoning benchmark:

| Language | Speakers | MGSM | XCOPA | XStoryCloze | INCLUDE | Any reasoning benchmark |
|----------|----------|------|-------|------------|---------|------------------------|
| Punjabi | ~113M | ✗ | ✗ | ✗ | ✓ (MCQ only) | None |
| Marathi | ~99M | ✗ | ✗ | ✗ | ✓ (MCQ only) | None |
| Tamil | ~90M | ✗ | ✓ (2-choice) | ✗ | ✓ (MCQ only) | Commonsense only |
| Telugu | ~96M | ✗ | ✗ | ✓ (2-choice) | ✓ (MCQ only) | Commonsense only |
| Urdu | ~230M | ✗ | ✗ | ✗ | ✓ (MCQ only) | None |
| Hindi | ~600M | ✗ | ✓ (2-choice) | ✓ (2-choice) | ✓ (MCQ only) | Commonsense only |
| Vietnamese | ~97M | ✗ | ✓ (2-choice) | ✓ (2-choice) | ✗ | Commonsense only |
| Bengali | ~268M | ✓ MGSM | ✗ | ✗ | ✓ (MCQ only) | Math only |

Note: MGSM exists for Bengali but covers only 250 problems — a very thin signal.

### Why this matters for our benchmark
Reasoning tasks (math, multi-step logic, causal inference) are where model capability differences are most meaningful. If all three models score similarly on MCQ knowledge benchmarks but diverge on reasoning in Hindi or Tamil, that divergence is invisible in existing data. Our benchmark should include multi-step math and logical reasoning in all top-20 languages.

### Recommended task additions
- Multi-step arithmetic word problems (MGSM-style) across all 20 languages
- Causal reasoning chains (extend XCOPA format) with natively authored scenarios
- Symbolic/logical reasoning problems translated by native speakers with cultural review

---

## Gap 2: Open-Ended Generation Quality — No Standardized Multilingual Benchmark

**Priority: CRITICAL**

### What's missing
Every major multilingual benchmark uses MCQ, classification, or extraction formats. There is no standardized, widely-adopted benchmark for evaluating **free-form multilingual text generation** across the top-20 languages.

| Format | Benchmarks | Top-20 Coverage |
|--------|-----------|-----------------|
| MCQ / multiple choice | MMMLU, MGSM, XCOPA, Belebele, INCLUDE | 8–20 languages |
| Classification | SIB-200, XNLI | 15–20 languages |
| Extraction | TyDiQA | 8 languages |
| Translation (reference-based) | FLORES-200, WMT | 20 languages |
| **Free-form generation** | MT-Bench variants (unstandardized) | ~9 languages |

MT-Bench multilingual extensions exist but are not standardized, cover ~9 languages, and rely on GPT-4 as judge in English — creating an evaluation loop that favors GPT-style outputs evaluated by a GPT judge.

### Why this matters for our benchmark
Generation quality is the most commercially relevant capability: summarization, explanation, instruction following, and creative tasks. A benchmark that only tests MCQ underestimates the gap between "can the model parse this language" vs. "can the model produce fluent, accurate, useful output in this language."

### Our benchmark advantage: multi-judge consensus
Using all three models as cross-judges eliminates single-judge bias and can produce reliable generation scores without human annotation. This is a methodological advance over MT-Bench's GPT-4-only judge.

### Recommended task additions
- **Instruction following:** native-language instructions with verifiable outputs (rewrite, format, extract, summarize)
- **Open-ended explanation:** explain a concept in the target language; scored on accuracy + fluency + cultural appropriateness
- **Document summarization:** summarize a 500–1000 word passage; evaluates compression and fidelity across languages
- **Multi-turn dialogue:** 3–5 turn conversations in target language; tests context retention and coherence

---

## Gap 3: Cultural Authenticity — Translated vs. Natively Authored Content

**Priority: HIGH**

### What's missing
Of all major benchmarks, only **TyDiQA** systematically uses natively authored content per language. The rest — MMMLU, XNLI, XCOPA, XStoryCloze, Belebele — are translations of English-origin content.

| Authorship type | Benchmarks | Problem |
|-----------------|-----------|---------|
| Translated from English | MMMLU, XNLI, XCOPA, XStoryCloze, Belebele | Anglo-centric reasoning patterns; idiomatic loss; cultural context stripped |
| Natively authored | TyDiQA | Only 8/20 languages; extractive QA only |
| Mixed/semi-native | BLEnD, INCLUDE | Partial; limited reasoning depth |

Translation artifacts systematically disadvantage models that are better at authentic cross-cultural reasoning vs. models trained heavily on translated content. A model that handles cultural nuance in authentic Tamil may score lower on a Tamil benchmark derived from English questions than a model that learned Tamil primarily from translated material.

### Why this matters for our benchmark
If the benchmark goal is to measure actual multilingual capability (not translation ability), the benchmark itself should use natively authored content or at minimum require cultural grounding per language.

### Recommended task additions
- **Culturally grounded QA:** questions that require knowledge of local customs, events, idioms, or social norms — answerable only with cultural knowledge, not by translating an English answer
- **Idiomatic understanding:** prompts with idiomatic expressions in each language; tests whether models understand or fail gracefully
- **Native speaker review:** synthetic dataset generation pipeline requires native speaker (or strong native-language model) review of each item before inclusion

---

## Gap 4: Instruction Following in Non-English — Completely Uncharted

**Priority: HIGH**

### What's missing
None of the three target models (Claude Opus 4.7, GPT-5.4, Gemini 3.1 Pro) has published scores on multilingual instruction-following benchmarks. The benchmarks that do exist for this task type have limited language coverage and no frontier model evaluations:

| Benchmark | Languages | Frontier Model Scores | Task Type |
|-----------|-----------|----------------------|-----------|
| Okapi | 26 | None published | Instruction following (win-rate) |
| BenchMAX | 17 | None published | Instruction following + other |
| MT-Bench multilingual | ~9 | Unstandardized | Multi-turn instruction |

No benchmark measures: whether a model correctly follows a complex multi-step instruction **written entirely in the target language**, covering the full top-20.

### Why this matters for our benchmark
This is the most practically important evaluation dimension for deployment. Users in Hindi or Tamil interact with models by giving instructions — and model capability at parsing, disambiguating, and executing those instructions in the native language is what determines real-world usefulness.

### Recommended task additions
- **Format instruction following:** "Write a 3-item bulleted list of X in [language]" — verifiable without a judge
- **Constraint following:** multi-constraint prompts (word limit + topic + style) in native language
- **Cross-language instruction execution:** instruction given in language A, response expected in language B — tests cross-lingual understanding

---

## Gap 5: Long-Context and Document-Level Understanding in Non-English

**Priority: MEDIUM**

### What's missing
Virtually no multilingual benchmark tests long-context understanding. BenchMAX includes a 128k-token long-context QA task across 17 languages, but frontier models have not been evaluated on it.

The practical capability gap here is significant: Gemini 3.1 Pro has a 1M token context window — but whether this capability transfers to non-English document processing is entirely unevaluated publicly.

### Recommended task additions (lower priority for initial benchmark)
- Long-document summarization (>2000 tokens) in each target language
- Multi-document QA with sources in target language
- Can be added as a stretch module after core benchmark is validated

---

## Gap 6: Model Score Transparency — All Three Models

**Priority: META (motivates the entire project)**

### What's missing
| Capability | Claude Opus 4.7 | GPT-5.4 | Gemini 3.1 Pro |
|------------|----------------|---------|----------------|
| Per-language MMMLU | ✗ | ✗ (GPT-5 baseline only) | ✗ (aggregate only) |
| MGSM (multilingual math) | ✗ | ✗ | ✗ |
| FLORES-200 | ✗ | ✗ | ✗ |
| Belebele | ✗ | ✗ | ✗ |
| Open-ended generation | ✗ | ✗ | ✗ |
| Cultural QA | ✗ | ✗ | ✗ |
| Instruction following (multilingual) | ✗ | ✗ | ✗ |

None of the three target models has published the data needed for a fair cross-model multilingual comparison. This project fills that gap directly.

---

## Prioritized Gap Summary

| Priority | Gap | Languages Most Affected | Benchmark Type to Create |
|----------|-----|------------------------|--------------------------|
| 1 | Math and reasoning missing for South Asian + SEA languages | Punjabi, Marathi, Tamil, Telugu, Urdu, Hindi, Vietnamese | Multi-step reasoning across all 20 |
| 2 | No standardized free-form generation benchmark | All 20 (no current standard) | Open-ended generation + multi-judge |
| 3 | Translation-artifact content across most benchmarks | All 20 affected | Natively authored / culturally grounded QA |
| 4 | Instruction following not evaluated multilingually | All 20 uncharted | Verifiable instruction-following tasks |
| 5 | Long-context understanding | All 20 uncharted | Long-document tasks (stretch goal) |
| 6 | No cross-model comparison data exists | All three models | Core motivation: run all three models on same tasks |

---

## Recommended Benchmark Design Principles (for Phase 4)

Based on the gap analysis, the new benchmark should:

1. **Cover all 20 languages** for every task — no partial coverage
2. **Include natively authored or culturally reviewed content** — not purely translated from English
3. **Mix task types**: MCQ (for comparability to existing benchmarks), reasoning (math, logic, causal), instruction following (verifiable), and open-ended generation (judge-scored)
4. **Use multi-judge consensus** (all three models judge each other) for generation tasks — eliminates single-judge bias
5. **Track self-evaluation bias** explicitly — flag cases where a model scores itself differently than the other two judges
6. **Use synthetic data generation** with cross-model review: each model generates benchmark items; the other two models critique and improve them
7. **Report per-language, per-task scores** — no aggregate-only reporting
8. **Publish all raw outputs** — enable external researchers to re-score with new judge models

---

## What the New Benchmark Adds Relative to Existing Work

| Dimension | Existing Benchmarks | Our Benchmark |
|-----------|--------------------|--------------| 
| Language coverage (top-20) | FLORES/Belebele cover all 20 but test translation/MCQ only | All 20 × all task types |
| Task diversity | Fragmented — different benchmarks for different tasks | Unified suite: MCQ + reasoning + generation + instruction |
| Reasoning in South Asian/SEA languages | Near-zero | Core task category |
| Evaluation methodology | Single model judge or human | Multi-judge consensus (all 3 models cross-judge) |
| Model transparency | None for these three models | First published cross-model comparison for Opus 4.7, GPT-5.4, Gemini 3.1 Pro |
| Dataset authorship | Mostly translated from English | Synthetic multi-model generation + native review |
| Self-evaluation bias tracking | Not measured | Explicit bias metric per model per language |
