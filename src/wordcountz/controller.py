from model import Model
from view import View


class Controller:
    def __init__(self, model=Model, view=View):
        self._model = model
        self._view = view()
        self._collection = {}

    def show(self, **kwargs):
        """Returns Word-count Dictionary

        Example:
        -------
        >>> " `python src/wordcountz show $(pwd)/temp/zen.txt` "
        """
        self._collection = kwargs.copy()
        return self._view.show(self._model(**self._collection.copy()).counter)

    def infograph(self, **kwargs):
        self._collection = kwargs.copy()
        return self._view.infograph(self._model(**self._collection.copy()).counter, 0)
