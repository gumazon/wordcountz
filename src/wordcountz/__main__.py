#!/usr/bin/env python

from pathlib import Path

import sys

from wordcountz import count_words


if __name__ == '__main__':
    _args = [_arg for _arg in sys.argv]
    print(_args)

    if len(_args) > 1:
        _file = _args[1]

    else:
        _file = '{}/Public/wordcountz/temp/zen.txt'.format(Path.home())

    print(count_words(_file))

