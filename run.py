from src.data.make_dataset import *
from src.viz.visualization import *

import pandas as pd
import sys

def main(targets):

    if 'data' in targets:
        inpath = 'data/raw/raw.csv'
        outpath = 'data/out/out.csv'
    elif 'test' in targets:
        inpath = 'data/test/test.csv'
        outpath = 'data/test/test_out.csv'

    make_dataset(inpath, outpath)
    fig_1, fig_2, fig_3 = make_visuals(outpath)




if name == '__main__':

    targets = sys.argv[1:]
    main(targets)
