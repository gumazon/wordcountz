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

    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def words(infile=None, value=None):
    """Count words in a text file.

    Words are made lowercase and punctuation is removed
    before counting.

    Parameters
    ----------
    infile : str
        Path to text file.

    value : str
        Text value.

    Returns
    -------
    collections.Counter
        dict-like object where keys are words and values are counts.

    Examples
    --------
    >>> from wordcountz.wordcountz import count
    ...
    ... # Text from infile
    ... count.words(infile="text.txt")
    ...
    ... # Text from value
    ... count.words(value="Insanity is doing the same thing over and over and expecting different results.")

    """
    text = ''
    if infile is not None:
        text = load(infile)
    elif value is not None:
        text = value
    else:
        print('Missing text value or file path.')

    if text:
        text = sanitize(text)

        wrds = text.split()
        return Counter(wrds)
