# Belebele Results

Reading comprehension MCQ across 20 languages, 900 examples per language (18,000 total per model).  
Scoring: exact match on A/B/C/D response letter.

## Overall Accuracy

| Model | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| Gemini 3.1 Flash-Lite Preview | 16,641 | 18,000 | **92.5%** |
| Claude Sonnet 4.6 | 15,791 | 18,000 | **87.7%** |
| GPT-5.4 Mini | — | — | *(in progress)* |

## Per-Language Accuracy

| Language | Code | Claude Sonnet 4.6 | Gemini 3.1 Flash-Lite | GPT-5.4 Mini |
|----------|------|:-----------------:|:---------------------:|:------------:|
| Arabic | arb_Arab | 93.8% | 95.2% | — |
| Bengali | ben_Beng | 83.7% | 90.6% | — |
| English | eng_Latn | 96.0% | 96.6% | — |
| French | fra_Latn | 92.6% | 95.6% | — |
| German | deu_Latn | 92.3% | 95.3% | — |
| Hindi | hin_Deva | 79.6% | 88.8% | — |
| Indonesian | ind_Latn | 90.8% | 94.1% | — |
| Japanese | jpn_Jpan | 88.8% | 92.2% | — |
| Korean | kor_Hang | 91.9% | 92.8% | — |
| Mandarin Chinese | zho_Hans | 91.7% | 94.1% | — |
| Marathi | mar_Deva | 80.7% | 90.9% | — |
| Portuguese | por_Latn | 92.6% | 94.6% | — |
| Punjabi | pan_Guru | 82.9% | 89.1% | — |
| Russian | rus_Cyrl | 89.7% | 94.9% | — |
| Spanish | spa_Latn | 89.7% | 94.2% | — |
| Tamil | tam_Taml | 77.9% | 87.1% | — |
| Telugu | tel_Telu | 80.8% | 85.9% | — |
| Turkish | tur_Latn | 88.2% | 92.8% | — |
| Urdu | urd_Arab | 80.2% | 90.9% | — |
| Vietnamese | vie_Latn | 91.0% | 93.4% | — |

## Key Observations

- **Gemini 3.1 Flash-Lite outperforms Claude Sonnet 4.6** across all 20 languages on this reading comprehension task (+4.8pp overall).
- **European languages** (English, French, German, Portuguese, Spanish) are strongest for both models (88–96%).
- **Indic languages** (Hindi, Marathi, Punjabi, Tamil, Telugu, Urdu) are the weakest cluster for Claude (78–83%), with Gemini showing a larger advantage here (+8–10pp).
- **Tamil and Telugu** are the lowest-scoring languages for both models.
- GPT-5.4 Mini results pending — will be updated once the run completes.
