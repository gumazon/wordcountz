#!/usr/bin/env python


import re
import os
from pathlib import Path
from string import punctuation
from collections import Counter

import sys

__api__ = {
    'path':   '<path> sys.argv[0]',
    'action': '<str> sys.argv[1]',    # options:[show|infograph]
    'params': {'data':  '<str|path> sys.argv[2]', 'limit': '<int> sys.argv[3]'}
}

# OUTPUT: collections.Counter
# API:
# - $( python src/wordcountz/counter.py <file:path> ):-> collections.Counter
#       eg: file="`pwd`/temp/zen.txt"
#
# - $( python src/wordcountz/counter.py <text:str> ):-> collections.Counter
#       eg: text='Einstein Qute\nInsanity is doing the same thing over and
#           over and expecting different results.'
#   API:
#       input:  python src/wordcountz/counter.py show text
#       output: collections.Counter
#   API:
#       input:  python src/wordcountz/counter.py show file
#       output: collections.Counter
#
#   API: Show Word-count Dictionary of Words in Given Text|Text File.
#       input:  python src/wordcountz/counter.py show <text|file>
#       output: <dict> {word: count}
# else:
#   API: Creates Top N Word-counts Infographic of Words in Given Text|Text-File.
#       run: $ python src/wordcountz/counter.py infograph <data:text|file> <limit:optional>
#       call:  Controller().infograph(data:str='', limit:int=0)


LAST_ID = 0

_temp_dir_path = Path.cwd().joinpath('temp')
TEMP_DIR = Path(_temp_dir_path)


def load(data=None) -> str or None:
    """Load text from a text file and return as a string.

    Parameters
    ----------
    data: str
        could be a file or text.

        file : path
            Path to text file. <matches path pattern: r'^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))'>

        text : str
            Text string.

    Returns
    -------
    str
        Text from text input or file.

    Examples
    --------
    >>> load(data="temp/text.txt")

    """
    path_pattern = r'^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))'
    if data:
        if re.match(path_pattern, data):
            with open(data, "r") as infile:
                return infile.read()
        else:
            return data


def remove_stopwords(text=''):
    stopwords = ['a', 'is', 'an', 'the', 'and', 'for', 'of', 'in', 'out', 'with', 'at', 'this', 'are', 'just']
    if text:
        title = ' '.join([remove_puncs(_wrd).capitalize() for _wrd in ((text.split('\n')[0]).split('.')[0]).split() if _wrd not in stopwords])
        words = [remove_puncs(_w) for _w in text.split() if _w not in stopwords]

        return title, words


def remove_puncs(text=''):
    """Lowercase and remove punctuation from a string.

    Parameters
    ----------
    text : str
        Text to remove_stopwords.

    Returns
    -------
    str
        Cleaned text.

    Examples
    --------
    >>> remove_puncs("Early optimization is the root of all evil!")

    """

    if text:
        text = text.lower()
        for p in punctuation:
            text = text.replace(p, "")
        return text



class DataCollection:
    def __init__(self):
        self.id = 0
        self.name = ''


class CollectionParent(DataCollection):


    def __init__(self, data=None):
        super().__init__()
        self.origin = ''
        self.__new(data)

    def new(self, data=None):
        if data:
            self.origin = self.__load(data)
            self.name = ' '.join(
                [wrd for wrd in remove_puncs((self.origin.split('\n')[0]).split('.')[0].lower()).split()])

    def __load(self, data=None):
        """Load text from a text file and return as a string.

    Parameters
    ----------
    data: str
        could be a file or text.

        file : path
            Path to text file. <matches path pattern: r'^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))'>

        text : str
            Text string.

    Returns
    -------
    str
        Text from text input or file.

    Examples
    --------
    >>> load(data="temp/text.txt")

    """

        if data:
            if re.match(self.path_pattern, data):
                with open(data, "r") as infile:
                    return infile.read()
            else:
                return data

    __new = new


collparent = CollectionParent().new(data=str(TEMP_DIR.joinpath('jeffrey_epstein.txt')))


class CollectionChild(DataCollection):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent_id = 0
        self.attrs = {}
        self.__new(**kwargs)

    def new(self, **kwargs):
        _img_path = kwargs.get('path',
                               TEMP_DIR.joinpath('outdir/{}.png'.format('_'.join([_w for _w in self.name.split()]))))
        self.attrs = {
            "limit": kwargs.get('limit', str(10)),
            "chart": kwargs.get('chart', 'bar'),
            "path": str(_img_path)
        }
        self.attrs.update(**kwargs)

    __new = new



def create(data):
    """Returns the first sentence of the first line of given text.

    Punctuations are removed from the returned title string.

    :param data: <str (text|path)>  Text or path to text file.

    :return: <str> Title string.

    Example
    ------
    >>> extract_title(data='text|file_path')

    """
    id = str(int(LAST_ID+1))
    text = load(data=data)
    title = remove_puncs((text.split('\n')[0]).split('.')[0])
    colls = {}

    def add_coll_word_count(coll_title='Word Count'):
        coll_id = (len(colls.keys())+1)
        coll_title = ' '.join([title, coll_title])
        colls.update(**{
            f"{coll_id}": {
                "id": str(coll_id),
                "title": coll_title,
                "data": {
                    f""
                },       # Counter(remove_puncs(text.lower()).split()),
                "images": {

                }      # [img for img in next_images(title)]
            }
        })

    return {
      "id": str(int(LAST_ID+1)),
      "origin": text,
      "title": title,
      "data": {},       # Counter(remove_puncs(text.lower()).split()),
      "images": {}      # [img for img in next_images(title)]
    }


def next_images(title='', imgs=None):
    if title:
        if imgs is None:
            imgs = []
        imgs.append(f"bar_chart_{'_'.join(title.split())}.png")

        return imgs

#       output: <dict>
#         collections: [
#           {
#               "id": 0,
#               "origin": "load_text(text|file)",
#               "title": f"{sen1line1title_sans_puncs(text)}",
#               "data": {"word1", word1_count, "word2", word2_count, ...},
#               "images": [f"bar_chart_{coll_name(title)}.png", ...]
#           }
#       ]
#
#     # API: python src/wordcountz/counter.py infograph file
#     # API: python src/wordcountz/counter.py infograph file <n:[OPTIONAL]>
#     return count(text=_val)


__all__ = ['count']


def request_route(*argvs):
    """

    :param argvs: <sys.argv>
    :return: <dict>
        {
            'path':   '<path> sys.argv[0]',
            'action': '<str> sys.argv[1]',    # options:[show|infograph]
            'params': {
                'data':  '<str|path> sys.argv[2]',
                'limit': '<int> sys.argv[3]'
            }
        }
    """
    params_keys = ['data', 'limit']
    in_argv = [arg for arg in argvs]

    request_obj = {}
    params_vals = []

    if len(in_argv) > 0:
        request_obj['path'] = in_argv[0]

    if len(in_argv) > 1:
        request_obj['action'] = in_argv[1]

    if len(in_argv) > 2:
        params_vals.extend(in_argv[2:])
        params = {}
        for n in zip(params_keys, params_vals):
            params[n[0]] = n[1]

        request_obj['params'] = params

    return request_obj


def test_request_route():
    expected = {'path': 'src/wordcountz/counter.py', 'action': 'infograph', 'params': {'data': 'we are just testing this thing for now', 'limit': '15'}}
    actual = os.system('python src/wordcountz/counter.py infograph "we are just testing this thing for now" 15')
    assert actual == expected


def main(*args):
    # API: python src/wordcountz/counter.py <action:sys.argv[1]> <args:sys.argv[2:]>
    print(request_route(sys.argv))

#
# def count(**kwargs):
#     """Count words in text from given string or file.
#
#         Words are made lowercase and punctuation is removed
#         before counting.
#
#         Parameters
#         ----------
#         kwargs:
#             text : str
#                 Text string.
#
#             file : str
#                 Path to text file.
#
#         Returns
#         -------
#         title:
#             Title string to be used as fig title and infograph-image file name.
#
#         collections.Counter
#             dict-like object where keys are words and values are counts.
#
#         Examples
#         --------
#         >>> # With text from input
#         ... _txt = '''Einstein Qute \nInsanity is doing the same thing over and over and expecting different results.'''
#         ... count(text=_txt)
#         ...  # With text from file
#         ... _file = '../../temp/einstein.txt'
#         ... count(file=_file)
#
#     """
#
#     file = kwargs.get('file', '')
#     text = (load(file) if file else kwargs.get('text', ''))
#     title, words = remove_stopwords(text)
#     return title, Counter(words)



if __name__ == '__main__':
    print(main(*[_arg for _arg in sys.argv]))
    print(test_request_route())
