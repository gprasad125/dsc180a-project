# load visuals & feature creation 
from asyncore import write
from src.data.make_dataset import *
from src.viz.visualization import *

# load machine learning 
from src.models.model_relevancy import *
from src.models.model_score import *
from src.models.opt_model_relevancy import *
from src.models.best_classifier import *
from src.models.best_scoring import *

# load results handling
from src.results.write_results import *

import sys
import json
import warnings

def main(targets):
    """
    Runs data creation, visualization and modeling.
    Current targets include:
    - `test`: Runs this on a 5-line test CSV file (data/test/test.csv)
    - `data`: Runs this on the full data

    Saves results of modeling to data/results in txt file, and saves visuals to data/visuals directory
    """

    if 'data' in targets:
        inpath = 'data/raw/SentimentLabeled_10112022.csv'
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
        metrics_sco = score(outpath)

        # optimized metrics
        opt_metrics_rel = opt_relevancy(outpath, optimized_parameters["DTC"], optimized_parameters["SVM"], optimized_parameters["KNN"])

        # best metrics (group)
        best_metrics_rel = best_relevancy(outpath, optimized_parameters["SVM_O"])
        best_metrics_sco = best_score(outpath, optimized_parameters["ridge"])

        # collect metrics
        metrics = [metrics_rel, opt_metrics_rel, best_metrics_rel, metrics_sco, best_metrics_sco]

        # write metrics to txt file
        answers_path = "data/results/results.txt"
        write_results(answers_path, metrics)
        

    except Exception as ex:
        exception_msg = "Exception Type: {0}. Arguments: \n{1!r}"
        message = exception_msg.format(type(ex).__name__, ex.args)
        print(message)


if __name__ == '__main__':

    targets = sys.argv[1:]
    warnings.filterwarnings('ignore')
    main(targets)
