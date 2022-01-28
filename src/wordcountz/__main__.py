#!/usr/bin/env python


from pathlib import Path
import sys
import count, plot
import matplotlib.pyplot as plt
import wordcountz


def main(*args, **kwargs):
    rgvs = []
    rgvs.extend(args)
    print(rgvs)

    if len(rgvs) > 1:
        file_path = rgvs[1]
    else:
        file_path = "{}/temp/einstein.txt".format(Path.cwd())

    if len(rgvs) > 2:
        n = int(rgvs[2])
    else:
        n = 10

    if len(rgvs) > 3:
        plot_type = rgvs[3]
    else:
        plot_type = 'bar'

    wrds = count.words(file_path)
    fig = plot.top_words(infile=file_path, n=n, word_counts=wrds, plot_type=plot_type)
    plt.show()


if __name__ == '__main__':
    print('wordcountz', 'v'+wordcountz.__version__)
    main(*[_av for _av in  sys.argv])
