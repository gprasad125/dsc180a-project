# load visuals & feature creation 
from src.data.make_dataset import *
from src.viz.visualization import *

# load machine learning 
from src.models.model_relevancy import *
from src.models.model_score import *
from src.models.opt_model_relevancy import *

import sys
import json

def main(targets):

    if 'data' in targets:
        inpath = 'data/raw/raw.csv'
        outpath = 'data/out/out.csv'
    elif 'test' in targets:
        inpath = 'data/test/test.csv'
        outpath = 'data/test/test_out.csv'

    try:

        # baseline EDA 
        make_dataset(inpath, outpath)
        make_visuals(outpath)

        # load model parameters
        config_path = "config/model_parameters.json"
        with open(config_path) as mp:
            optimized_parameters = json.load(mp)

        # vanilla metrics
        metrics_rel = relevancy(outpath)
        metrics_sco = None # score(outpath)

        # optimized metrics
      #  opt_metrics_rel = opt_relevancy(outpath, optimized_parameters)

        # print results 
        print("The vanilla metrics:")
        print(metrics_rel, metrics_sco)

        print("The optimized metrics:")
        print(optimized_parameters)

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
