def write_results(path, results):

    f = open(path, "w")
    f.write("Vanilla Classifiers:")
    f.write(results[0])
    f.write("Optimized Classifiers:")
    f.write(results[1])
    f.write("Vanilla Classifiers:")
    f.write(results[2])