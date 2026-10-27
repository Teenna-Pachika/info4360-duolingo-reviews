import re
import pandas as pd

# Load the reviews file and prepare it: real dates, no empty text, and a word count.
def load_reviews(path="../data/duolingo_reviews.csv"):
    """Load reviews, parse dates, fill empty text, add word count."""
    df = pd.read_csv(path)
    df["at"] = pd.to_datetime(df["at"])
    df["content"] = df["content"].fillna("")
    df["n_words"] = df["content"].str.split().str.len()
    return df

# Keep only the negative reviews (1-2 stars).
def get_negative(df, max_stars=2):
    """Keep only 1-2 star reviews."""
    return df[df["score"] <= max_stars].copy()

# Clean the text: remove HTML tags and links, lowercase,
# keep only letters, and fix extra spaces and line breaks.
def clean_text(text):
    """Lowercase and keep only letters and spaces."""
    text = re.sub(r"<[^>]+>", " ", text)              # HTML tags like <br>
    text = re.sub(r"http\S+|www\.\S+", " ", text)     # links
    text = re.sub(r"[^a-z\s]", " ", text.lower())     # numbers, symbols, emojis
    return re.sub(r"\s+", " ", text).strip()          # extra spaces and line breaks