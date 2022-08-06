from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
def num_data_null_handler(data):
    data_num = data.select_dtypes(exclude=["object"])
    non_data_num = data.select_dtypes(include=["object"])
    imputer = SimpleImputer(strategy="median")
    data_num_null_handeled_array = imputer.fit_transform(data_num)
    data_num_null_handeled_dataFrame = pd.DataFrame(data_num_null_handeled_array, columns=data_num.columns)
    data_num_medians = imputer.statistics_
    new_data = pd.concat([data_num_null_handeled_dataFrame, non_data_num], axis=1)
    return new_data

def cat_data_to_num(data,attribs):
    data_copy = data.copy()
    data_copy.fillna('NA', inplace=True)
    for attrib in attribs:
        to_encode_data = data_copy[attrib]
        to_encode_data_np = to_encode_data.to_numpy()
        not_encode_data = data_copy.drop(attrib, axis=1)
        to_encode_data_np = to_encode_data_np.reshape(-1, 1)
        _cat_encoder = OneHotEncoder()
        encoded_data_np = _cat_encoder.fit_transform(to_encode_data_np).toarray()
        columns = []
        for item in _cat_encoder.categories_:
            columns.append(attrib + " " + item)
        encoded_data = pd.DataFrame(encoded_data_np, columns = columns[:])
        new_data = pd.concat([not_encode_data, encoded_data], axis=1)
        data_copy = new_data.copy()
    return new_data

def binary_cat_to_num(data, attrib, baseValue):
    data_copy = data.copy()
    i = 0
    while i < len(data_copy[attrib]):
        if data_copy.at[i,attrib] == baseValue:
#             print(data_copy.loc[i].at[attrib])
            data_copy.at[i,attrib] = 1.0
        else:
            data_copy.at[i,attrib] = 0.0 
        i += 1
    new_data = data_copy.rename(columns={attrib: attrib+ " is " +baseValue})
    return new_data

    