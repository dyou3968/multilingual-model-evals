# Global MMLU Results

Knowledge MCQ across multiple languages, 1,000 examples per language.  
Dataset: [CohereLabs/Global-MMLU](https://huggingface.co/datasets/CohereLabs/Global-MMLU) — 57 academic subjects.  
Scoring: exact match on A/B/C/D response letter.

---

## Our Harness Run — 0-shot

15 of the top-20 target languages (Punjabi, Marathi, Tamil, Urdu not in dataset).

| Language | Code | Claude Sonnet 4.6 | Gemini 3.1 Flash-Lite |
|----------|------|:-----------------:|:---------------------:|
| English | en | **91.5%** | 88.0% |
| Russian | ru | **90.6%** | 86.7% |
| German | de | **90.3%** | 87.2% |
| Portuguese | pt | **90.0%** | 86.8% |
| Spanish | es | **89.8%** | 86.9% |
| Turkish | tr | **89.0%** | 85.4% |
| Indonesian | id | **89.2%** | 85.5% |
| Mandarin Chinese | zh | **88.6%** | 85.8% |
| French | fr | **88.1%** | 85.7% |
| Vietnamese | vi | **88.1%** | 84.9% |
| Japanese | ja | **88.0%** | 86.0% |
| Hindi | hi | **87.8%** | 85.9% |
| Korean | ko | **87.2%** | 83.1% |
| Arabic | ar | **85.4%** | 85.3% |
| Bengali | bn | **85.1%** | 83.3% |
| **Overall (15 langs)** | | **88.6%** (13,281 / 14,994) | **85.8%** (12,865 / 15,000) |

---

## System Card Comparison — GMMLU by Resource Tier

Source: [Claude Sonnet 4.6 System Card](https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75.pdf), Table 2.19.1.A  
Evaluated on CohereLabs/Global-MMLU across 42 languages with reasoning enabled (adaptive thinking at max effort for Claude models; provider defaults for others). Scores reflect accuracy on successfully parsed responses.

| Tier | Claude Sonnet 4.6 | Claude Sonnet 4.5 | Claude Opus 4.6 | Gemini 3 Pro | GPT-5.2 Pro |
|------|:-----------------:|:-----------------:|:---------------:|:------------:|:-----------:|
| English | 92.9% | 93.1% | 93.9% | **94.4%** | 93.1% |
| High-resource avg¹ | 91.0% | 91.1% | 92.2% | **92.9%** | 91.5% |
| Mid-resource avg² | 90.2% | 90.0% | 91.6% | **92.5%** | 90.9% |
| Low-resource avg | 83.8% | 81.3% | 85.5% | **89.4%** | 87.2% |
| **Overall avg (all langs)** | 88.7% | 87.9% | 90.1% | **91.8%** | 90.1% |

**Low-resource languages (individual):**

| Language | Claude Sonnet 4.6 | Claude Sonnet 4.5 | Claude Opus 4.6 | Gemini 3 Pro | GPT-5.2 Pro |
|----------|:-----------------:|:-----------------:|:---------------:|:------------:|:-----------:|
| Igbo | 76.7% | 77.9% | 80.8% | **88.1%** | 85.3% |
| Chichewa | 78.8% | 75.9% | 81.3% | **88.0%** | 85.5% |
| Yoruba | 80.3% | 73.2% | 81.3% | **86.2%** | 82.4% |
| Shona | 82.2% | 79.5% | 85.3% | **89.3%** | 87.4% |
| Somali | 82.3% | 78.5% | 83.3% | **90.0%** | 87.9% |
| Malagasy | 83.9% | 80.9% | 86.4% | **89.8%** | 88.2% |
| Hausa | 84.1% | 78.8% | 85.0% | **88.8%** | 86.7% |
| Amharic | 86.7% | 85.7% | 88.2% | **90.3%** | 87.9% |
| Kyrgyz | 86.9% | 84.2% | 85.9% | **88.3%** | 86.6% |
| Swahili | 87.0% | 84.3% | 88.9% | **90.6%** | 88.7% |
| Sinhala | 88.1% | 86.9% | 89.5% | **92.2%** | 90.0% |
| Nepali | 89.1% | 89.1% | 89.8% | **91.8%** | 90.3% |

**Summary gaps to English:**

| | Claude Sonnet 4.6 | Claude Sonnet 4.5 | Claude Opus 4.6 | Gemini 3 Pro | GPT-5.2 Pro |
|-|:-----------------:|:-----------------:|:---------------:|:------------:|:-----------:|
| Avg gap | -4.4% | -5.4% | -3.9% | **-2.7%** | -3.1% |
| Worst gap | -16.2% | -19.9% | -13.2% | **-8.2%** | -10.7% |

¹ High-resource (15): French, German, Spanish, Portuguese, Russian, Chinese, Japanese, Arabic, Italian, Dutch, Korean, Polish, Turkish, Swedish, Czech  
² Mid-resource (14): Hindi, Vietnamese, Indonesian, Persian, Greek, Hebrew, Romanian, Ukrainian, Serbian, Filipino, Malay, Bengali, Lithuanian, Telugu

---

## Methodology Notes

- **Our harness**: 0-shot, structured letter extraction (last A/B/C/D in response). 15 languages, 1,000 examples each, capped for cost. Claude Sonnet 4.6 spontaneously includes reasoning chains even without a chain-of-thought prompt; scoring extracts the final letter from these chains.
- **System card**: Reasoning enabled (adaptive thinking at max effort for Claude Sonnet 4.6 / Opus 4.6; max thinking budget 1,024 tokens for Claude Sonnet 4.5; provider defaults for Gemini/GPT). 42 languages, full dataset.
- These two result sets **are not directly comparable** due to the reasoning vs. 0-shot gap and different language subsets. The system card scores reflect best-effort performance; our harness scores reflect practical inference costs.
