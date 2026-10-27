# Topic modeling helper functions (TF-IDF + NMF).
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.decomposition import NMF


# Turn review texts into TF-IDF numbers, without stopwords.
def build_tfidf(texts, extra_stopwords=("duolingo", "app")):
    """Return the fitted TF-IDF vectorizer and the TF-IDF matrix."""
    stop = list(ENGLISH_STOP_WORDS) + list(extra_stopwords)
    tfidf = TfidfVectorizer(stop_words=stop, ngram_range=(1, 2), min_df=5, max_df=0.9)
    T = tfidf.fit_transform(texts)
    return tfidf, T


# Find k topics and list the top words of each one.
def show_topics(tfidf, T, k, n_words=10):
    """Fit NMF with k topics and return the model and a table of top words."""
    nmf = NMF(n_components=k, random_state=42, max_iter=500).fit(T)
    words = tfidf.get_feature_names_out()
    topics = {f"Topic {i}": ", ".join(words[t.argsort()[-n_words:][::-1]])
              for i, t in enumerate(nmf.components_)}
    return nmf, pd.Series(topics, name="top words")


# Give each review the topic it matches best.
def assign_topics(nmf, T):
    """Return the main topic number for each review."""
    return nmf.transform(T).argmax(axis=1)