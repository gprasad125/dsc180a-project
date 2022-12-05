def write_results(path, results):

    with open(path, "w") as f:
        
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