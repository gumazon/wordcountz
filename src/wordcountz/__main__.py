#!/usr/bin/env python


import sys
import wordcountz
from controller import Controller


def main(*args, **kwargs):
    """

    API:
          python src/wordcountz <action> <text> <n>
    show: json
         python src/wordcountz show "`pwd`/temp/zen.txt"
    infograph: png
         python src/wordcountz infograph "`pwd`/temp/zen.txt" 10

    :param args:
    :param kwargs:
    :return:
    """
    rgvs = []
    rgvs.extend(args)
    print(rgvs)
    _output = {}

    action = 'show'
    file = ''
    text = ''
    n = 0

    if len(rgvs) > 1:
        action = rgvs[1]

    if len(rgvs) > 2:
        _val = rgvs[2]
        if '/' in _val:
            file = _val
        else:
            text = _val
    if action == 'infograph':
        if len(rgvs) > 3:
            n = rgvs[3]

    app = Controller()
    if action == 'show':
        return app.show(file=file, text=text, n=n)
    if action == 'infograph':
        return app.infograph(file=file, text=text, n=n)


if __name__ == '__main__':
    print(wordcountz.__version__)
    # print(bin(5).replace("0b", ""))
    print("{0:b}".format(int(5)))
    print(main(*[_av for _av in sys.argv]))
