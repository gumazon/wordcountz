#!/usr/bin/env python

# OUTPUT: collections.Counter
# API:
# - $( python src/wordcountz/counter.py <file:path> ):-> collections.Counter
#       eg: file="`pwd`/temp/zen.txt"
#
# - $( python src/wordcountz/counter.py <text:str> ):-> collections.Counter
#       eg: text='Einstein Qute\nInsanity is doing the same thing over and
#           over and expecting different results.'

from string import punctuation
from collections import Counter

import sys

__all__ = ['load', 'count']


def main(*args):
    _args = [_arg for _arg in args]
    print(_args)

    if len(_args) > 1:
        _val = _args[1]

        if '/' in _val:
            # API: python src/wordcountz/counter.py <file:path>
            return count(file=_val)
        else:
            # API: python src/wordcountz/counter.py <text:str>
            return count(text=_val)


def load(file=''):
    """Load text from a text file and return as a string.

    Parameters
    ----------
    file : str
        Path to text file.

    Returns
    -------
    str
        Text file contents.

    Examples
    --------
    >>> load(file="text.txt")

    """
    try:
        with open(file, "r") as infile:
            text = infile.read()
    except Exception as e:
        print(file, e.args[1])
    else:
        return text


def count(**kwargs):
    """Count words in text from given string or file.

        Words are made lowercase and punctuation is removed
        before counting.

        Parameters
        ----------
        text : str
            Text string.

        file : str
            Path to text file.

        Returns
        -------
        collections.Counter
            dict-like object where keys are words and values are counts.

        Examples
        --------
        >>> # Text from text
        ... _txt = '''Einstein Qute \nInsanity is doing the same thing over and over and expecting different results.'''
        ... count(text=_txt)

    """

    file = kwargs.get('file', '')
    text = (load(file) if file else kwargs.get('text', ''))
    title = _title_from(text)
    text = _sani_str(text)
    words = _sani_ls((text.split() if text else []))
    return title, Counter(words),


def _title_from(text=''):
    if text:
        _wrds = (text.split('\n\n')[0])
        _wrds = (_wrds.split("\\n")[0])
        _wrds = (_wrds.split('\n')[0])
        # print('_line', _wrds)

        _wrds = (_wrds.split('.')[0])
        # print('_cent', _wrds)

        _wrds = (_wrds.split(' '))
        # print('_wrds', _wrds)

        return ' '.join([_wrd.capitalize() for _wrd in _wrds])


def _sani_str(text=''):
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
    >>> _sani_str("Early optimization is the root of all evil!")

    """

    if text:
        text = text.lower()
        for p in punctuation:
            text = text.replace(p, "")
        return text


def _sani_ls(words):
    return _exclude_stopwords(words)


def _exclude_stopwords(words):
    stopwords = ['a', 'is', 'an', 'the', 'and', 'for', 'of', 'in', 'out', 'with']
    _outwords = []

    for word in words:
        if word not in stopwords:
            _outwords.append(word)

    return _outwords


if __name__ == '__main__':
    print(main(*[_arg for _arg in sys.argv]))
