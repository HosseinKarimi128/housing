#!/usr/bin/env python
# coding: utf-8
from sklearn.base import BaseEstimator, TransformerMixin

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import sys  
import pandas as pd
sys.path.insert(0, '/src/housing/features')
sys.path.insert(0, '/src/housing/preprocess')
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from load_data import internal_load
from columnsSpliter import get_columns
import math
import requests
import json
import pandas as pd
import numpy as np
import os
from IPython.display import clear_output
from sklearn.model_selection import train_test_split
from zlib import crc32

from sklearn.base import BaseEstimator, TransformerMixin

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import sys  
import pandas as pd
sys.path.insert(0, '/src/housing/features')
sys.path.insert(0, '/src/housing/preprocess')
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from load_data import internal_load
from columnsSpliter import get_columns
import math
import requests
import json
import pandas as pd
import numpy as np
import os
from IPython.display import clear_output
from sklearn.model_selection import train_test_split
from zlib import crc32

data = internal_load("C:/Users/h.karimi/Documents/pprojects/housing_hw/preprocess/interim/htt_with_lat_long.csv")
original_data = internal_load("C:/Users/h.karimi/Documents/pprojects/housing_hw/preprocess/external/train.csv")

# removing duplicate 
def remove_duplicate (data):
    data_copy = data.copy()
    data_new = data_copy.drop_duplicates()
    return(data_new)

# decapitalizing
def decapitalizing(data,string_columns,categorical_attribs):
    data_copy = data.copy()
    for column in string_columns: # decapitalizing the preprocess
        data_copy[column] = data_copy[column].str.lower().copy()
        
    for col in string_columns: # decapitalizing the metadata
        ca_copy = categorical_attribs[col].copy()
        categorical_attribs[col] = [x.lower() for x in ca_copy]    
    return data_copy

def strc_errors_handler(data,cat_columns, correction = True):
    data_copy = data.copy()
    strc_errors_printer.err_cols = {}
    for column in cat_columns:
        i = 0
        while i < len(data_copy[column]):
            case = data_copy.at[i,column]
            if case not in categorical_attribs[column] and not pd.isna(case):
                if column not in strc_errors_printer.err_cols.keys():
                    strc_errors_printer.err_cols[column] = set()
                strc_errors_printer.err_cols[column].add(case)
                if correction:
                    data_copy.drop(i,inplace = True)
            i += 1
    return data_copy

def correct_current_typos(data):    
    data_copy = data.copy()
    data_copy.replace('twnhs','twnhsI')
    data_copy.replace('brk cmn','brkcomm',inplace = True)
    data_copy.replace('cmentbd','cemntbd',inplace = True)
    data_copy.replace('wd shng','wdshing',inplace = True)    
    return data_copy

def na_handler(data,numerical_columns, numcat_columns,string_columns):   
    data_copy_num = data[numerical_columns].copy()
    data_copy_numcat = data[numcat_columns].copy()
    data_copy_string = data[string_columns].copy()
    
    data_copy_num.interpolate(inplace = True)
    for col in data_copy_num:
        i = 0
        if (pd.isna(data_copy_num.at[0,col])):
            while pd.isna(data_copy_num.at[i,col]):
                i += 1
            for j in range(i):
                data_copy_num.at[j,col] = data_copy_num.at[j+1,col]
        data_copy_numcat.interpolate(method = 'pad', inplace = True)
    data_copy_string.fillna(value = 'na',inplace = True)   
    return pd.concat([data_copy_num,data_copy_numcat,data_copy_string], axis=1)

#packing all above function
def data_cleaning(data):
    strCols = get_columns('str')
    nmcCols = get_columns('nmc')
    catCols = get_columns('cat')
    numCols = get_columns('num')
    data_copy = data.copy()
    return na_handler(correct_current_typos(decapitalizing(remove_duplicate(data_copy),strCols,catCols)),numCols,nmcCols,strCols)

