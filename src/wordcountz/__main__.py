#!/usr/bin/env python

from pathlib import Path
import matplotlib.pyplot as plt

import sys

from wordcountz import count_words


class View:
    @staticmethod
    def plot_top(n=10, word_counts=None, input_file=None, plot_type='bar'):
        """Plot a bar chart of top `n` words in `word_counts` from `input_file`.
        ------------

        Creates a matplotlib.container.BarContainer, bar chart object, of top N words.
        Then saves it as a PNG image file, into parent direcotry of the input text file.


        Parameters
        ----------
        n: int, optional
            The `n` number of words to include in the plot.

        word_counts: collections.Counter
            Counter object of word counts.

        input_file : str
            Path to text file.

        plot_type: str
            type of plot, default='bar'

        Returns
        -------
        top_{n}_{input_file_stem}_words.png: image
            Writtes a bar chart, PNG image file, of the top N words,
            to the parent dir of the given input_file.

        Examples
        --------
        >>> wrds = words('text.txt')
        ... View().plot_top(n=10, word_counts=wrds, input_file='text.txt', plot_type='bar')
        """
        if word_counts:
            if input_file is None:
                input_file = '{}/Public/wordcountz/temp/zen.txt'.format(Path.home())
            input_file = Path(input_file)
            _title = 'Top {} {} Words'.format(n, input_file.stem.capitalize())

            top_n_words = word_counts.most_common(n)
            word, count = zip(*top_n_words)
            if plot_type == 'bar':
                fig = plt.bar(range(n), count)
                plt.title(_title)
                plt.xticks(range(n), labels=word, rotation=30)
                plt.ylabel('Word')
                plt.xlabel('Count')
                plt.savefig('{}/{}.png'.format(input_file.parent, '_'.join([_word.lower() for _word in _title.split(' ')])))
                return fig


class Controller:
    def __init__(self, input_file=None):
        self._input_file = input_file
        self._model = self.__count_words(self.input_file)
        self._view = View()

    @property
    def input_file(self):
        return self._input_file

    @input_file.setter
    def input_file(self, path):
        self._input_file = path

    def plot_top(self, n=10):
        wrds = self._model.words_count
        print(wrds)
        return self._view.plot_bar_top(n, wrds)

    __count_words = count_words


if __name__ == '__main__':
    _args = [_arg for _arg in sys.argv]
    print(_args)

    if len(_args) > 1:
        _file = _args[1]

    else:
        _file = '{}/Public/wordcountz/temp/zen.txt'.format(Path.home())

    _output = Controller(_file)

    print(_output.plot_top())
