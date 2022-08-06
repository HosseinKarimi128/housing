
from sklearn.base import BaseEstimator, TransformerMixin
from src.preprocess.cat_handler import CatDataHandler
from src.preprocess.cleaner import Cleaner
from src.preprocess.columns_classifier import get_columns
from src.preprocess.feature_scaler import FeatureScaler
from src.preprocess.dataset_splitter import CreateSet
from src.preprocess.address import AddressConverter
from sklearn.pipeline import Pipeline


class TransformerPipeLine(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, x):
        return self

    def transform(self, x, y=None):
        # required_set = self.required_set
        cat_cols = get_columns('cat')
        str_cols = get_columns('str')
        num_cols = get_columns('num')
        nmc_cols = get_columns('nmc')
        housing_transform_pipeline = Pipeline([
            ('AddressConverter', AddressConverter("Neighborhood")),
            ('Cleaner', Cleaner(str_cols, cat_cols, num_cols, nmc_cols)),
            # ('FeatureScaler', FeatureScaler(num_cols)),
            ('CatDataHandler', CatDataHandler(str_cols, nmc_cols)),
            ('CreateSet', CreateSet())])
        return housing_transform_pipeline.fit_transform(x)
