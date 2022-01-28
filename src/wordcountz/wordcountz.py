from collections import Counter
from string import punctuation


def _load_text(input_file):
    """Load text from a text file and return as a string."""
    with open(input_file, "r") as file:
        text = file.read()
    return text


def _clean_text(text):
    """Lowercase and remove punctuation from a string."""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file):
    """Count unique words in a string."""
    text = _load_text(input_file)
    text = _clean_text(text)
    words = text.split()
    return Counter(words)
