from src.make_dataset import *

import pandas as pd
import sys

def main(targets):

    if 'data' in targets:
        make_dataset()
    elif 'test' in targets:
        test = True

if name == '__main__':

    targets = sys.argv[1:]
    main(targets)
