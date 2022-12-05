def write_results(path, results):
    """
    Writes out the results list into a text file. 
    """

    with open(path, "w") as f:

        # explanation
        f.write(
            "For classifiers, the metrics are: [accuracy, precision, recall, f1-score], and for scoring, the metrics are [mean squared error, r2 score]."
        )
        f.write("\n" + "\n")
        
        f.write("Vanilla Classifiers:" + "\n")
        f.write(str(results[0]) + "\n")
        f.write("Optimized Classifiers:" + "\n")
        f.write(str(results[1]) + "\n")
        f.write("Best Classifiers:" + "\n")
        f.write(str(results[2]) + "\n")
        f.write("\n")
        f.write("Vanilla Scoring:" + "\n")
        f.write(str(results[3]) + "\n")
        f.write("Best Scoring:" + "\n")
        f.write(str(results[4]))

    f.close()