# Helper to estimate app update dates from the reviews.

import pandas as pd


# Estimate when each app version came out: the first day it got at least `min_daily` reviews.
def get_release_dates(df, min_reviews=1000, min_daily=20):
    """Return a Series of estimated release dates for each main app version (e.g. '6.94')."""
    versions = df.dropna(subset=["reviewCreatedVersion"]).copy()
    versions["release"] = versions["reviewCreatedVersion"].str.extract(r"^(\d+\.\d+)")[0]
    versions["day"] = versions["at"].dt.normalize()
    counts = versions.groupby(["release", "day"]).size()

    # Only versions with enough reviews, and only ones released after our data starts
    big = versions["release"].value_counts()
    big = big[big >= min_reviews].index
    dates = {r: counts[r][counts[r] >= min_daily].index.min() for r in big}
    start = df["at"].min().normalize()
    return pd.Series({r: d for r, d in dates.items() if d > start}).sort_values()