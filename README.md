# What's driving negative Duolingo reviews, and do those complaints get better or worse after certain app updates?

INFO 4360 course project by Teenna Pachika and Johanna Garcia.

**Progress:** Phase 1 ✅ Completed · Phase 2 ✅ Completed · Phase 3 ✅ Completed

📄 **Final report:** [`notebooks/06_final_report.ipynb`](notebooks/06_final_report.ipynb) (HTML version: `notebooks/06_final_report.html`)

## The problem

Duolingo is one of the most popular language-learning apps, and 87% of its recent Google Play reviews are 4 or 5 stars. But about 8% of reviews are 1 or 2 stars, which is roughly 4,150 unhappy users in six weeks, and they are the ones most likely to quit the app. Duolingo's product team can't read them all, and a star rating doesn't say why someone is unhappy. We analyzed these reviews to find the most common complaints and whether they got worse after app updates, so the team can decide what to fix first.

## Data

| Field | Details |
|---|---|
| **Source** | Google Play Store reviews of the Duolingo app (US, English) |
| **Collected with** | `collect_reviews.ipynb`, using the `google-play-scraper` package |
| **Size** | 50,000 reviews (4,147 negative, 1-2 stars) |
| **Period** | July 29 to September 6, 2026 (only one review after Sep 6) |
| **File** | `data/duolingo_reviews.csv` |
| **Privacy** | Usernames and profile pictures were removed |

## Our approach (Path B: understanding)

1. **Classic text mining:** keywords, VADER sentiment, and NMF topic modeling to explore the reviews.
2. **Claude labeling:** we used Claude (`claude-haiku-4-5`) to label all 4,147 negative reviews with one or more complaint types.
3. **Quality checks:** we compared Claude with our keyword rules, re-checked the "bugs" label with a stricter prompt, and hand-checked 30 random reviews.
4. **Analysis:** we tracked each complaint week by week around app updates, and measured which complaints other users agree with most (thumbs-up).

## Main results

1. **Two specific changes caused the late-August jump in negative reviews.** Negative reviews rose from 7.6 to 9.5 per 100 reviews after app version 6.94. Most of the increase came from language-access complaints (0.4 → 1.3 per 100 reviews) and complaints about the changing app icon (0.4 → 1.1).
2. **Paying is the complaint users agree with most.** Paywall complaints are 16.9% of negative reviews but get 42.7% of all thumbs-up. Teaching quality, ads, and energy limits show the same pattern.
3. **The language-access spike comes from one group.** After August 24, 55% of these complaints mention Iran, Persian, or Farsi (up from 10%).
4. **Claude explained most negative reviews, cheaply and reliably.** Unexplained reviews dropped from 62% with keywords to 30% with Claude, and Claude agreed with our hand-check on 24 of 30 reviews.

**Recommendations for Duolingo:** let users turn off the changing app icon, respond clearly to users in Iran, test a gentler free version with more energy and fewer ads, and track complaints weekly after each update.

## API usage and cost

| Step | Input tokens | Output tokens | Cost |
|---|---|---|---|
| Labeling all negative reviews (incl. a 100-review test) | 223,696 | 74,803 | $0.60 |
| Stricter re-check of "bugs" | 47,784 | 10,465 | $0.10 |
| **Total** | **271,480** | **85,268** | **≈ $0.70** |

Claude's labels are saved in `data/claude_labels.csv` and `data/claude_bugs_check.csv`, so the notebooks can be re-run without paying again.

## Limitations

Our data only covers Android users in the US, writing in English, over six weeks. App release dates are estimated from the app versions in the reviews, so timing doesn't prove an update caused a complaint. Claude is less accurate on non-English reviews and sometimes misses a second complaint in the same review.

## Repository structure

| Path | What it contains |
|---|---|
| `notebooks/06_final_report.ipynb` | **Final report** (blog-style), with its HTML export |
| `notebooks/01_exploration_keywords_claude.ipynb` | Data exploration, keywords, complaint categories, and first Claude test (Phase 2) |
| `notebooks/02_sentiment_topics_path.ipynb` | Sentiment analysis, topic modeling, and why we chose Path B (Phase 2) |
| `notebooks/03_overview_sentiment_topics.ipynb` | Data overview, sentiment, and topic charts (Phase 3) |
| `notebooks/04_claude_labels_trends.ipynb` | Claude labeling, comparison with keywords, weekly trends, and thumbs-up analysis (Phase 3) |
| `notebooks/05_claude_hand_check.ipynb` | Hand-check of 30 Claude labels (Phase 3) |
| `data/` | Reviews dataset, Claude labels, bugs re-check, and hand-check results |
| `figures/` | All charts used in the report and presentation |
| `src/` | Reusable functions: data loading (`preprocessing.py`), sentiment (`sentiment.py`), topic modeling (`topics.py`), and app release dates (`app_versions.py`) |
| `collect_reviews.ipynb` | Code used to download the reviews |

## How to run

1. Clone the repository and move into it:
   ```
   git clone https://github.com/Teenna-Pachika/info4360-duolingo-reviews.git
   cd info4360-duolingo-reviews
   ```
2. Install the packages:
   ```
   pip install -r requirements.txt
   ```
3. Open and run `notebooks/06_final_report.ipynb`. It uses the saved data and Claude labels, so **no API key is needed**.
4. *(Optional)* To run Claude again, create a file named `.env` in the main folder with your key (`ANTHROPIC_API_KEY=your-key-here`) and set `RELABEL = True` in notebook 04. This costs about $0.70. `.env` is listed in `.gitignore`, so it is never committed.

Note: Rerunning `collect_reviews.ipynb` pulls the newest reviews, so the numbers would be different from ours. To reproduce our results, use the saved file in `data/`.

## Team

- Teenna Pachika
- Johanna Garcia