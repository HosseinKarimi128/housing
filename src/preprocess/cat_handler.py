
# official package
# get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder


class CatDataHandler(BaseEstimator, TransformerMixin):
    def __init__(self, str_cols, nmc_cols):
        self.strCols = str_cols
        self.nmcCols = nmc_cols

    def fit(self, x):
        return self

    def transform(self, x, y=None):
        def str_column_encoder(data, str_columns):
            data_copy = data.copy()
            new_data = data_copy.copy()
            _cat_encoder = OneHotEncoder() 
            for col in str_columns:
                new_data = new_data.drop(col, axis=1)  # isolate the non categorical preprocess
            for col in str_columns:
                encoded_col = _cat_encoder.fit_transform(data_copy[col].to_numpy().reshape(-1, 1))
                cols = [col + ": " + str(s) for s in _cat_encoder.categories_[0]]
                encoded_col_df = pd.DataFrame(encoded_col.toarray(), columns=cols)
                new_data = pd.concat([new_data, encoded_col_df], axis=1)
            return new_data
        return str_column_encoder(x, self.strCols)
