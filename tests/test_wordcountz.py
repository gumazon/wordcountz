from collections import Counter
from pathlib import Path

from wordcountz.wordcountz.src.wordcountz import count_words


def test_count_words():
    """Test word counting from a file."""

    expected = Counter({'over': 2, 'and': 2, 'insanity': 1, 'is': 1, 'doing': 1, 'the': 1, 'same': 1, 'thing': 1, 'expecting': 1, 'different': 1, 'results': 1})

    actual = count_words('{}/einstein.txt'.format(Path(__file__).parent))

    assert actual == expected, "Einstein quote counted incorrectly!"
