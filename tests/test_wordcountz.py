from collections import Counter
from pathlib import Path

from wordcountz.wordcountz import count

quote = "Insanity is doing the same thing over and over and expecting different results."
with open("einstein.txt", "w") as file:
    file.write(quote)


def test_count_words():
    """Test word counting from a file."""

    expected = Counter({'over': 2, 'and': 2, 'insanity': 1, 'is': 1, 'doing': 1, 'the': 1, 'same': 1, 'thing': 1, 'expecting': 1, 'different': 1, 'results': 1})

    actual = count.words('{}/einstein.txt'.format(Path(__file__).parent))

    assert actual == expected, "Einstein quote counted incorrectly!"
