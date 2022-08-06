import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split


class CreateSet(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, x):
        return self

    def transform(self, x, y=None):
        y = x['SalePrice']
        x = x.drop(columns='SalePrice')
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        return x_train, x_test, y_train, y_test
