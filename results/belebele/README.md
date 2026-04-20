# Belebele Results

Reading comprehension MCQ across 20 languages, 900 examples per language (18,000 total per model).  
Scoring: exact match on A/B/C/D response letter.

## Overall Accuracy

| Model | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| Gemini 3.1 Flash-Lite Preview | 16,641 | 18,000 | **92.5%** |
| GPT-5.4 Mini | 16,103 | 18,000 | **89.5%** |
| Claude Sonnet 4.6 | 15,791 | 18,000 | **87.7%** |

## Per-Language Accuracy

| Language | Code | Claude Sonnet 4.6 | GPT-5.4 Mini | Gemini 3.1 Flash-Lite |
|----------|------|:-----------------:|:------------:|:---------------------:|
| Arabic | arb_Arab | 93.8% | 91.4% | 95.2% |
| Bengali | ben_Beng | 83.7% | 86.6% | 90.6% |
| English | eng_Latn | 96.0% | 95.1% | 96.6% |
| French | fra_Latn | 92.6% | 93.4% | 95.6% |
| German | deu_Latn | 92.3% | 93.1% | 95.3% |
| Hindi | hin_Deva | 79.6% | 84.6% | 88.8% |
| Indonesian | ind_Latn | 90.8% | 89.9% | 94.1% |
| Japanese | jpn_Jpan | 88.8% | 89.2% | 92.2% |
| Korean | kor_Hang | 91.9% | 91.1% | 92.8% |
| Mandarin Chinese | zho_Hans | 91.7% | 92.3% | 94.1% |
| Marathi | mar_Deva | 80.7% | 86.8% | 90.9% |
| Portuguese | por_Latn | 92.6% | 92.1% | 94.6% |
| Punjabi | pan_Guru | 82.9% | 86.4% | 89.1% |
| Russian | rus_Cyrl | 89.7% | 92.9% | 94.9% |
| Spanish | spa_Latn | 89.7% | 91.7% | 94.2% |
| Tamil | tam_Taml | 77.9% | 84.3% | 87.1% |
| Telugu | tel_Telu | 80.8% | 82.8% | 85.9% |
| Turkish | tur_Latn | 88.2% | 88.8% | 92.8% |
| Urdu | urd_Arab | 80.2% | 86.0% | 90.9% |
| Vietnamese | vie_Latn | 91.0% | 90.7% | 93.4% |

## Key Observations

- **Gemini 3.1 Flash-Lite leads overall** (+4.8pp vs. Claude, +3.0pp vs. GPT-5.4 Mini).
- **GPT-5.4 Mini outperforms Claude Sonnet 4.6** by +1.8pp overall and is notably stronger on Indic languages (+5–7pp on Hindi, Marathi, Urdu, Tamil).
- **European languages** (English, French, German, Portuguese, Spanish) are strongest for all three models (88–97%).
- **Indic languages** (Hindi, Marathi, Punjabi, Tamil, Telugu, Urdu) are the weakest cluster: Claude 78–83%, GPT 82–87%, Gemini 86–91%.
- **Tamil and Telugu** are the lowest-scoring languages for all three models.
- **Claude leads GPT-5.4 Mini** on Arabic (93.8% vs. 91.4%) and Korean (91.9% vs. 91.1%).
