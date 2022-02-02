from collections import Counter

from counter import count


class Model:
    def __init__(self, **kwargs):
        self._index = []
        self._selected = {
            "id": 0,
            "title": "",
            "counter": Counter({})
        }
        self.__save(**kwargs.copy())

    def index(self):
        return self._index

    def show(self, title=''):
        _output = []
        for _n in self._index:
            if title in _n.get('title', ''):
                _output.append(_n)

        self._selected = _output[0]

        return self._selected

    def save(self, **kwargs):

        return count(**kwargs.copy())

    __save = save

    def update(self, **kwargs):
        pass

    def delete(self):
        pass


