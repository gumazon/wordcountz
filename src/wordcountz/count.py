from collections import Counter
from string import punctuation


def load(infile):
    """Load text from a text file and return as a string.

    Parameters
    ----------
    infile : str
        Path to text file.

    Returns
    -------
    str
        Text file contents.

    Examples
    --------
    >>> from wordcountz.wordcountz import count
    ... count.load("text.txt")
    """
    with open(infile, "r") as file:
        text = file.read()
    return text


def sanitize(text):
    """Lowercase and remove punctuation from a string.

    Parameters
    ----------
    text : str
        Text to clean.

    Returns
    -------
    str
        Cleaned text.

    Examples
    --------
    >>> from wordcountz.wordcountz import count
    ... count.sanitize("Early optimization is the root of all evil!")
    'early optimization is the root of all evil'
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def words(infile):
    """Count words in a text file.

    Words are made lowercase and punctuation is removed
    before counting.

    Parameters
    ----------
    infile : str
        Path to text file.

    Returns
    -------
    collections.Counter
        dict-like object where keys are words and values are counts.

    Examples
    --------
    >>> from wordcountz.wordcountz import count
    ... count.words("text.txt")
    """
    text = load(infile)
    text = sanitize(text)
    wrds = text.split()
    return Counter(wrds)
