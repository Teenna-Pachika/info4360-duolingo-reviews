# What's Driving Negative Duolingo Reviews?

INFO 4360 course project by Teenna Pachika and Johanna Garcia.

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

## Plan

We are following Path B (understanding/extraction). We'll start by using the Claude API to label a sample of about 500 negative reviews into complaint types, such as hearts, streaks, ads, or pricing. Reviews are short, informal, and often mention more than one issue, so fixed keyword rules would miss a lot. Then we'll use keyword analysis, TF-IDF, and topic modeling on all negative reviews (about 4,150). These methods are fast and free to rerun, so we avoid an API call for every review, and they let us check that the complaint types from the sample hold up across the full dataset.

To make sure the patterns are real and not just a result of pooling everything together, we'll track each complaint type week by week and across the most common app versions, and compare 1-star vs. 2-star reviews. The goal is a recommendation the product team can act on. Instead of "users complain about ads," we want to say how big each complaint is, whether it's growing, and which app version it lines up with, so the team knows what to investigate first.

## How to run
1. Install the packages: `pip install google-play-scraper pandas`
2. Run `collect_reviews.ipynb`

Note: Rerunning the notebook pulls the newest reviews, so the numbers will be slightly different from ours. To reproduce our results exactly, use the saved file in `data/`.
