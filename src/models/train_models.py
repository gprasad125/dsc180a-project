import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def train_models(inpath, target, status):

    df = pd.read_csv(inpath)
    x = df["text"]
    y = df[target]
    model = DecisionTreeClassifier()

    if status == 'test':

        model.fit(x, y)

    else:

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
        model.fit(x_train, y_train)

        
    return model
