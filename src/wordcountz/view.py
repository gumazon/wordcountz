import plotter


class View:
    @staticmethod
    def show(count_words=None):
        _output = {"words": {}}
        if count_words:
            title, wcounter = count_words
            _output['title'] = title
            for wrd in zip(wcounter.keys(), wcounter.values()):
                _word, _count = wrd
                _output['words'][_word] = _count
        return _output

    @staticmethod
    def infograph(count_words=None, n=0):
        if count_words:
            if not n:
                n = len([_wrd for _wrd in list(count_words[-1])])
            fig = plotter.draw(count_words, n)
            plotter.save(count_words[0], fig)
            plotter.show(fig)
