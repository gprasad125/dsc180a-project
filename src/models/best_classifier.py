import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

def best_relevancy(inpath, parameters_svm):
    """
    Trains, tests, and evaluates the optimized versions of the following models:
    - Decision Tree Classifier
    - Support Vector Machine
    - Nearest Neighbors 

    Also sends confusion matrices to data/visuals as .PNGs 
    """
    df = pd.read_csv(inpath)
    x = df["text"]
    y = df["relevant"]

    plt.figure()
    metrics = {}
    model = Pipeline([
        ('tfidf', TfidfVectorizer()), 
        ('clf', SVC(**parameters_svm))
    ])

    name = "SupportVectorClassifier"

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)        
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    accuracy = (predictions == y_test).mean()

    stats = [
        accuracy,
        precision_score(predictions, y_test),
        recall_score(predictions, y_test),
        f1_score(predictions, y_test)
    ]

    cm = confusion_matrix(predictions, y_test)
    plot = sns.heatmap(cm, cmap = "Blues", annot = True, fmt = "1")
        
    path = "data/visuals/" + "optimized_" + str(name) + ".png"
    plot.figure.savefig(path)

    metrics[name] = stats

    print("finished testing the best classifier")

    return metrics
