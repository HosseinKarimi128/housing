from typing import Union
from pandas import DataFrame, Series
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class FeatureScaler(BaseEstimator, TransformerMixin):
    def __init__(self, num_cols):
        self.num_cols = num_cols

    def fit(self, x):
        return self

    def transform(self, x, y=None):

        def standardizer(data):
            num_cols = self.num_cols
            from sklearn.preprocessing import StandardScaler
            cleaned_num_data = data.copy()
            remaining_data = pd.DataFrame()
            for column in cleaned_num_data:
                if column not in num_cols:
                    remaining_data[column] = cleaned_num_data[column]
                    cleaned_num_data.drop(columns=column, inplace=True)
            the_standard_scaler = StandardScaler()
            standard_cleaned_num_data = the_standard_scaler.fit_transform(cleaned_num_data).copy()
            standard_cleaned_num_data_pd = \
                pd.DataFrame(standard_cleaned_num_data, index=cleaned_num_data.index, columns=cleaned_num_data.columns)
            standard_cleaned_data: Union[DataFrame, Series] =\
                pd.concat([remaining_data, standard_cleaned_num_data_pd], axis=1)
            return standard_cleaned_data
        return standardizer(x)
