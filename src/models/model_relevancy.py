import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score, f1_score

def relevancy(inpath):

    df = pd.read_csv(inpath)
    x = df["text"]
    y = df["relevant"]
    model = DecisionTreeClassifier()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)        
    model.fit(x_train, y_train)

    predictions = model.predict(x_test, y_test)
    accuracy = (predictions == y_test).mean()

    metrics = [
        accuracy,
        precision_score(predictions, y_test),
        recall_score(predictions, y_test),
        f1_score(predictions, y_test)
    ]

    return metrics
