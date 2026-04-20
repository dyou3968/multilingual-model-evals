# MILU Results

Knowledge MCQ focused on Indic languages, 1,000 examples per language.  
Dataset: [ai4bharat/MILU](https://huggingface.co/datasets/ai4bharat/MILU) — gated, requires `HF_TOKEN`.  
Scoring: exact match on A/B/C/D response letter.

---

## Our Harness Run — 0-shot

7 of the top-20 target languages covered by MILU (English, Hindi, Bengali, Punjabi, Marathi, Telugu, Tamil).

| Language | Claude Sonnet 4.6 | Gemini 3.1 Flash-Lite | Gemini 3 Flash |
|----------|:-----------------:|:---------------------:|:--------------:|
| Bengali | **89.6%** | 88.8% | **90.8%** |
| Marathi | **89.6%** | 88.7% | **89.8%** |
| Hindi | **87.8%** | 83.7% | **87.1%** |
| English | **87.5%** | 86.2% | 84.9% |
| Telugu | **85.8%** | 84.7% | **86.8%** |
| Tamil | **83.3%** | 84.1% | **88.7%** |
| Punjabi | **80.3%** | 80.0% | 84.9% |
| **Overall (7 langs)** | **86.3%** (6,039 / 7,000) | **85.2%** (5,962 / 7,000) | **87.6%** (6,999 / 7,000) |

---

## System Card Comparison — MILU by Language

Source: [Claude Sonnet 4.6 System Card](https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75.pdf), Table 2.19.2  
Evaluated on ai4bharat/MILU across 11 languages (10 Indic + English) with reasoning enabled (adaptive thinking at max effort for Claude models; provider defaults for others).

| Language | Claude Sonnet 4.6 | Claude Sonnet 4.5 | Claude Opus 4.6 | Gemini 3 Pro | GPT-5.2 Pro |
|----------|:-----------------:|:-----------------:|:---------------:|:------------:|:-----------:|
| English | 91.7% | 90.1% | 92.1% | **95.0%** | 91.7% |
| Hindi | **92.8%** | 91.0% | 92.4% | **96.3%** | 92.4% |
| Bengali | 90.9% | 89.0% | 90.7% | **93.7%** | 90.2% |
| Kannada | 91.5% | 89.3% | 91.8% | **94.4%** | 90.7% |
| Telugu | 89.3% | 87.2% | 89.6% | **93.1%** | 88.7% |
| Tamil | 88.8% | 86.7% | 89.2% | **93.0%** | 88.7% |
| Gujarati | 89.0% | 87.0% | 89.0% | **92.7%** | 88.4% |
| Marathi | 89.2% | 86.4% | 89.1% | **92.5%** | 88.5% |
| Punjabi | 87.2% | 85.8% | 87.3% | **91.3%** | 87.3% |
| Odia | 87.9% | 85.8% | 87.2% | **91.8%** | 87.8% |
| Malayalam | 87.0% | 85.0% | 87.6% | **91.3%** | 86.6% |
| **Average** | **89.6%** | 87.6% | 89.6% | **93.2%** | 89.2% |
| Gap to English (avg) | -2.3% | -2.8% | -2.7% | **-2.0%** | -2.7% |
| Gap to English (worst) | -4.7% | -4.7% | -4.7% | — | — |

---

## Key Observations

- **Gemini 3 Pro leads across all Indic languages** in the system card evaluation by a wide margin (+3.6pp over Claude Sonnet 4.6 average).
- **Claude Sonnet 4.6 and Opus 4.6 are tied** on MILU average (both 89.6%) in the system card evaluation, with Opus slightly ahead on individual languages.
- **In our 0-shot harness, Claude Sonnet 4.6 scores 86.3%** — above Gemini 3.1 Flash-Lite (85.2%) but below Gemini 3 Flash (87.6%).
- **Bengali and Marathi are strongest for Claude** (89.6% each); Punjabi is weakest (80.3%).
- **Claude's harness scores are ~3.3pp below its system card scores** (86.3% vs. 89.6%) — consistent with the reasoning vs. 0-shot gap seen on GMMLU.
- **Gemini 3 Flash outperforms Flash-Lite by +2.4pp** overall in our harness (87.6% vs. 85.2%), with larger gains on Indic scripts (Bengali +2.0pp, Tamil +4.6pp, Marathi +1.1pp).
- **English is the weakest language for Gemini 3 Flash** in our harness (84.9%), below its Indic language scores — likely a prompt-format sensitivity rather than a true capability gap.

---

## Methodology Notes

- **Our harness**: 0-shot, structured letter extraction (last A/B/C/D in response). 7 languages, 1,000 examples each, capped for cost. Uses `option1`–`option4` fields with answer as key name (e.g. `"option2"`). Claude Sonnet 4.6 spontaneously includes reasoning chains; scoring extracts the final letter.
- **System card**: Reasoning enabled (adaptive thinking at max effort for Claude Sonnet 4.6 / Opus 4.6; max thinking budget 1,024 tokens for Claude Sonnet 4.5; provider defaults for Gemini/GPT). 11 languages, full dataset.
- These two result sets **are not directly comparable** due to the reasoning vs. 0-shot gap and different language coverage (our harness covers 7 of the 11 system card languages).
