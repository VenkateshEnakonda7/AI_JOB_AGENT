import re
from collections import Counter
from config import STOPWORDS, MIN_KEYWORD_FREQUENCY

def clean_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower()

def extract_keywords(job_descriptions):
    all_text = " ".join(job_descriptions)
    cleaned = clean_text(all_text)
    words = cleaned.split()
    common_words = Counter(words)

    keywords = [
        word for word, freq in common_words.items()
        if word not in STOPWORDS and freq >= MIN_KEYWORD_FREQUENCY
    ]
    return keywords
    