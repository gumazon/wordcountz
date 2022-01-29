from counter import count


class Model:
    def __init__(self, **kwargs):
        self.counter = self._words_counter(**kwargs)

    def _words_counter(self, **kwargs):
        return count(**kwargs.copy())




