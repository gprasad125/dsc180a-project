import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

def score(inpath):
    """
    Trains and evaluates a vanilla KNeighborsRegressor to score Tweets. 
    Unoptimized since default parameters were proven best. 
    """

    df = pd.read_csv(inpath)
    df.dropna(inplace = True)
    x = df["text"]
    y = df["score"]
    model = Pipeline([
            ('tfidf', TfidfVectorizer()), 
            ('clf', KNeighborsRegressor())
        ])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)        
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    metrics = [
        mean_squared_error(predictions, y_test),
        r2_score(y_test, predictions)
    ]

    print("Finished evaluating Nearest Neighbors Regressor")

    return metrics
