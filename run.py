from src.data.make_dataset import *
from src.viz.visualization import *

import sys

def main(targets):

    if 'data' in targets:
        inpath = 'data/raw/raw.csv'
        outpath = 'data/out/out.csv'
    elif 'test' in targets:
        inpath = 'data/test/test.csv'
        outpath = 'data/test/test_out.csv'

    try:
        make_dataset(inpath, outpath)
        fig_1, fig_2, fig_3 = make_visuals(outpath)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


if name == '__main__':

    targets = sys.argv[1:]
    main(targets)
