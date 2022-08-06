# official package

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class Cleaner (BaseEstimator, TransformerMixin):
    def __init__(self, str_cols, cat_cols, num_cols, nmc_cols):
        self.str_cols = str_cols
        self.cat_cols = cat_cols
        self.num_cols = num_cols
        self.nmc_cols = nmc_cols

    def fit(self, x):
        return self

    def transform(self, x, y=None):

        def clean(data, str_cols, cat_cols, num_cols, nmc_cols):

            def remove_duplicate(uncleaned_data):
                deduplicated_data = uncleaned_data.drop_duplicates()
                return deduplicated_data.reset_index(drop=True)

            def de_capitalizing(uncleaned_data):
                for column in str_cols:
                    # de_capitalizing the preprocess
                    uncleaned_data[column] = uncleaned_data[column].str.lower().copy()
                    # de_capitalizing the metadata
                    ca_copy = cat_cols[column].copy()
                    cat_cols[column] = [i.lower() for i in ca_copy]
                return uncleaned_data

            def correct_current_typos(uncleaned_data):
                uncleaned_data.replace('twnhs', 'twnhsi', inplace=True)
                uncleaned_data.replace('brk cmn', 'brkcomm', inplace=True)
                uncleaned_data.replace('cmentbd', 'cemntbd', inplace=True)
                uncleaned_data.replace('wd shng', 'wdshing', inplace=True)

                for column in str_cols:
                    uncleaned_data[column].str.strip()
                return uncleaned_data

            def structural_errors_handler(uncleaned_data, correction=True):
                err_cols = {}
                for column in cat_cols:
                    i = 0
                    while i < len(uncleaned_data[column]):
                        case = uncleaned_data.at[i, column]
                        if case not in cat_cols[column] and not pd.isna(case):
                            print(case, cat_cols[column])
                            if column not in err_cols.keys():
                                err_cols[column] = set()
                            err_cols[column].add(case)
                            if correction:
                                uncleaned_data.drop(i, inplace=True)
                        i += 1
                    uncleaned_data = uncleaned_data.reset_index(drop=True)
                return uncleaned_data.reset_index(drop=True)

            def na_handler(uncleaned_data):
                uncleaned_data_num = uncleaned_data[num_cols].copy()
                uncleaned_data_numcat = uncleaned_data[nmc_cols].copy()
                uncleaned_data_string = uncleaned_data[str_cols].copy()
                uncleaned_data_selected_columns = \
                    pd.concat([uncleaned_data_num, uncleaned_data_numcat, uncleaned_data_string], axis=1)
                uncleaned_data_remained = uncleaned_data.drop(columns=uncleaned_data_selected_columns)

                uncleaned_data_num.interpolate(inplace=True)
                for col in uncleaned_data_num:
                    i = 0
                    if pd.isna(uncleaned_data_num.at[0, col]):
                        while pd.isna(uncleaned_data_num.at[i, col]):
                            i += 1
                        for j in range(i):
                            uncleaned_data_num.at[j, col] = uncleaned_data_num.at[j+1, col].copy()
                    uncleaned_data_numcat.interpolate(method='pad', inplace=True)
                uncleaned_data_string.fillna(value='missing', inplace=True)
                return \
                    pd.concat([uncleaned_data_num, uncleaned_data_numcat,
                               uncleaned_data_string, uncleaned_data_remained], axis=1)

            m1 = remove_duplicate(data).copy().reset_index(drop=True)
            m2 = de_capitalizing(m1).copy().reset_index(drop=True)
            m3 = correct_current_typos(m2).copy().reset_index(drop=True)
            m4 = na_handler(m3).copy().reset_index(drop=True)
            m5 = structural_errors_handler(m4).copy().reset_index(drop=True)
            return m5
        return clean(x, self.str_cols, self.cat_cols, self.num_cols, self.nmc_cols)
