import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

def score(inpath):

    df = pd.read_csv(inpath)
    x = df["text"]
    y = df["score"]
    model = DecisionTreeRegressor()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)        
    model.fit(x_train, y_train)

    predictions = model.predict(x_test, y_test)

    metrics = [
        mean_squared_error(predictions, y_test)
    ]

    return metrics
