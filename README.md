# What's Driving Negative Duolingo Reviews?

INFO 4360 course project by Teenna Pachika.

## The problem
Duolingo gets thousands of app reviews every week, which makes it hard for their product team to tell what's actually making users unhappy or making them quit. I'm looking at the 1–2 star reviews to figure out which complaints come up the most (things like hearts, streaks, ads, and the free vs. paid gap), and whether they get worse after certain app updates, so the team knows what to fix first.

## Data
- 50,000 Google Play Store reviews of the Duolingo app (US, English), from July 29 to Sept 10, 2026
- Collected with `collect_reviews.ipynb` using the google-play-scraper package
- Saved in `data/duolingo_reviews.csv`
- Columns: review text, star rating, thumbs-up count, app version, and date
- Usernames were dropped for privacy

## Plan
Path B (understanding/extraction). I'll use Claude to label a sample of negative reviews into complaint types, then keyword analysis, TF-IDF, and topic modeling to look at all of them and see how complaints change over time and across app versions.

## How to run
1. `pip install google-play-scraper pandas`
2. Run `collect_reviews.ipynb`

Note: rerunning it pulls the newest reviews, so the numbers will be a bit different from mine.