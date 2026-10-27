# What's driving negative Duolingo reviews, and do those complaints get better or worse after certain app updates?

INFO 4360 course project by Teenna Pachika and Johanna Garcia.

**Progress:** Phase 1 ✅ Completed · Phase 2 ✅ Completed · Phase 3 ⏳ In progress

## The problem

Duolingo is one of the most popular language-learning apps, and 87% of its recent Google Play reviews are 4 or 5 stars. But a high rating can hide real problems: about 8% of reviews are 1 or 2 stars, which is roughly 4,150 unhappy users in six weeks, and they are the ones most likely to cancel or delete the app. Duolingo's product team can't read them all, and a star rating doesn't say why someone is unhappy. We're analyzing these reviews to find the most common complaints and whether they get worse after certain app updates, so the team can decide what to fix first.

## Data

| Field | Details |
|---|---|
| **Source** | Google Play Store reviews of the Duolingo app (US, English) |
| **Collected with** | `collect_reviews.ipynb`, using the `google-play-scraper` package |
| **Size** | 50,000 reviews, 6 columns |
| **Period** | July 29 to September 10, 2026 |
| **File** | `data/duolingo_reviews.csv` |

| Column | Description |
|---|---|
| `reviewId` | Unique ID for each review |
| `content` | Text of the review |
| `score` | Star rating, from 1 to 5 |
| `thumbsUpCount` | Number of users who marked the review as helpful |
| `reviewCreatedVersion` | App version the user had when writing the review|
| `at` | Date and time the review was posted |

Usernames were dropped for privacy.

## Phase 2 key findings

1. **Unhappy users explain more.** Only 8.3% of reviews are 1-2 stars, but they are much longer than positive ones (about 17-19 words vs. 5), so they carry most of the detail about problems.
2. **Paying, ads, and energy are the biggest complaints.** Keyword categories show that about 14% of negative reviews mention paying or subscriptions, and about 9% each mention ads and energy/hearts. Topic modeling found the same themes, plus some we didn't expect: AI-generated content, app icon changes, the chess course, and language requests.
3. **Some complaints change over time.** Complaints about the app icon and notifications went from about 2-3% of negative reviews in early August to 9.3% in the week ending Sep 6, around the same time the overall share of negative reviews went up.
4. **Stars and sentiment can't explain the "why."** Sentiment mostly agrees with star ratings, but about 1 in 5 negative reviews (19.8%) sound positive, and 62% didn't match any of our keywords. This is why we plan to use Claude in Phase 3.

## Plan for Phase 3

We are following Path B (understanding/extraction). We'll use the Claude API to label a sample of about 500 negative reviews into complaint types, then compare Claude's labels with our keyword rules and improve the rules. Then we'll apply the rules to all ~4,150 negative reviews and track each complaint type week by week. The goal is a recommendation the product team can act on: how big each complaint is, whether it's growing, and when it changed, so the team knows what to investigate first.

## Repository structure

| Path | What it contains |
|---|---|
| `data/` | The reviews dataset |
| `notebooks/01_exploration_keywords_claude.ipynb` | Data exploration, keywords, complaint categories, Claude test, and Phase 3 tool plan |
| `notebooks/02_sentiment_topics_path.ipynb` | Sentiment analysis, topic modeling, and why we chose Path B |
| `src/` | Reusable functions for loading and cleaning data (`preprocessing.py`), sentiment (`sentiment.py`), and topic modeling (`topics.py`) |
| `collect_reviews.ipynb` | Code used to download the reviews |

## How to run

1. Clone the repository:
   ```
   git clone https://github.com/Teenna-Pachika/info4360-duolingo-reviews.git
   ```
2. Install the packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a file named `.env` in the main folder with your Claude API key (only needed for the Claude test in notebook 01):
   ```
   ANTHROPIC_API_KEY=your-key-here
   ```
4. Run `notebooks/01_exploration_keywords_claude.ipynb`, then `notebooks/02_sentiment_topics_path.ipynb`.

Note: The notebooks use the saved file in `data/`, so you don't need to download the reviews again. Rerunning `collect_reviews.ipynb` pulls the newest reviews, so the numbers would be different from ours.
