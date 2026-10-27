# Sentiment helper functions (VADER).

import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Score each review from -1 (very negative) to +1 (very positive) and add it as a new column.
def add_sentiment(df, text_col="content"):
    """Add a 'sentiment' column with the VADER compound score."""
    sia = SentimentIntensityAnalyzer()
    df = df.copy()
    df["sentiment"] = df[text_col].apply(lambda t: sia.polarity_scores(t)["compound"])
    return df


# Plot the sentiment scores for each star rating.
def plot_sentiment_by_score(df):
    """Boxplot of sentiment by star rating."""
    df.boxplot(column="sentiment", by="score")
    plt.suptitle("")
    plt.title("VADER Sentiment by Star Rating")
    plt.xlabel("Star rating")
    plt.ylabel("Sentiment score (-1 to 1)")
    plt.show()


# Find reviews whose text sounds positive even though the rating is low.
def find_mismatches(df, min_sentiment=0.5):
    """Return rows with sentiment above min_sentiment."""
    return df[df["sentiment"] > min_sentiment]