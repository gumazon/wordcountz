from pathlib import Path
import matplotlib.pyplot as plt


def top_words(infile, n=10, word_counts=None, plot_type='bar'):
    """Plot a bar chart of top `n` words in `word_counts` from `infile`.
    --------------------------------------------------------------------

    Creates a matplotlib.container.BarContainer, bar chart object, of top N words.
    Then saves it as a PNG image file, into parent direcotry of the input text file.


    Parameters
    ----------
    n: int, optional
        The `n` number of words to include in the plot.

    word_counts: collections.Counter
        Counter object of word counts.

    infile : str
        Path to text file.

    plot_type: str
        type of plot, default='bar'

    Returns
    -------
    fig: matplotlib.container.BarContainer
        - creates a bar chart fig of the top N words.
        - saves fig to "top_{n}_{input_file_stem}_words.png" image file,
          in parent dir of `input_file`.

    Examples
    --------
    >>> from wordcountz import count, plot
    ... wrds = count.words('text.txt')
    ... plot.top_words(infile='text.txt', n=10, word_counts=wrds, plot_type='bar')

    """
    if word_counts:
        infile = Path(infile)
        _title = 'Top {} {} Words'.format(n, infile.stem.capitalize())

        top_n_words = word_counts.most_common(n)
        word, count = zip(*top_n_words)
        if plot_type == 'bar':
            fig = plt.bar(range(n), count)
            plt.title(_title)
            plt.xticks(range(n), labels=word, rotation=30)
            plt.xlabel('Word')
            plt.ylabel('Count')
            plt.savefig('{}/{}.png'.format(infile.parent, '_'.join([_word.lower() for _word in _title.split(' ')])))
            return fig
