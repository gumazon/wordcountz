from pathlib import Path
import matplotlib.pyplot as plt

__all__ = ['draw', 'save', 'show']


def main(counter_count=None, n=10):
    if counter_count:
        title, word_counter = counter_count

        fig = draw(word_counter=counter_count, n=n)
        save(title=title, fig=fig)
        show(fig=fig)


def draw(word_counter=None, n=10):
    if word_counter:
        return _bar_fig(word_counter=word_counter, n=n)


def _bar_fig(word_counter, n):
    """Plot a bar chart of top N words.

    Creates a matplotlib.container.BarContainer, bar chart object, of top N words.
    Then saves it as a PNG image file, into parent direcotry of the input text file.


    Parameters
    ----------
    title : str
        Title of text.

    n: int, optional
        The `n` number of words to include in the plot.

    word_counter: collections.Counter
        Counter object of word counts.

    Returns
    -------
    fig: matplotlib.container.BarContainer
        - creates a bar chart fig of the top N words.
        - saves fig to "top_{n}_{input_file_stem}_words.png" image file,
          in parent dir of `input_file`.

    Examples
    --------
    >>> from wordcountz.wordcountz.src.wordcountz.counter import count
    ... counter = count()
    ... bar_fig(title='Word Counts', word_counts=counter, n=10)

    """

    if word_counter:
        title, word_counter = word_counter
        title = ' '.join([title, 'Word Count Top', str(n)])

        top_n_words = word_counter.most_common(n)
        word, count = zip(*top_n_words)

        fig = plt.bar(range(n), count)
        plt.title(title)
        plt.xticks(range(n), labels=word, rotation=90)
        plt.xlabel('Word')
        plt.ylabel('Count')
        return fig


def save(title, fig=None):
    if fig:
        _name = '_'.join([str(_wrd).lower() for _wrd in title.split()])
        _outdir = Path.cwd().joinpath('temp/outdir')
        _outfile = Path(_outdir).joinpath('{}.png'.format(_name))
        fig = fig
        plt.savefig(_outfile)


def show(fig=None):
    if fig:
        fig = fig
        plt.show()


if __name__ == '__main__':
    from counter import count
    _counter = count(text='Einstein Qute\nInsanity is doing the same thing over and over and expecting different results.')
    main(_counter, n=len([_n for _n in list(_counter[1])]))
