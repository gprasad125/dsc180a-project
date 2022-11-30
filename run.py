from src.data.make_dataset import *
from src.viz.visualization import *
from src.models.model_relevancy import *
from src.models.model_score import *

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
        make_visuals(outpath)
        metrics_rel = relevancy(outpath)

        print(metrics_rel)
       # metrics_sco = score(outpath)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
