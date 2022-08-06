from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd

def show_valid_cat_features():
    print("SalePrice_cat\n",
        "YearRemodAdd_cat\n",
        "YearBuilt_cat\n",
        "FullBath_cat\n",
        "1stFlrSF_cat\n",
        "TotalBsmtSF_cat\n",
        "GarageCars_cat\n",
        "GrLivArea_cat\n",
        "OverallQual_cat")

def split (data,feature):
    new_data = data.copy()
    if feature == 'SalePrice_cat':
            new_data["SalePrice_cat"] = pd.cut(new_data["SalePrice"],
                bins=[0,100000, 200000, 300000, 400000, 500000, 600000, 700000,1000000],
                labels=[1, 2, 3, 4, 5, 6, 7, 8])
    elif feature == 'OverallQual_cat':
            new_data["OverallQual_cat"] = pd.cut(new_data["OverallQual"],
                bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100],
                labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    elif feature == 'GrLivArea_cat':
            new_data["GrLivArea_cat"] = pd.cut(new_data["GrLivArea"],
                bins=[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 40000],
                labels=[1, 2, 3, 4, 5, 6, 7, 8 , 9])
    elif feature == 'GarageCars_cat':
            new_data["GarageCars_cat"] = pd.cut(new_data["GarageCars"],
                bins=[-1, 0.9, 1.9, 2.9, 3.9, 10],
                labels=[1, 2, 3, 4, 5])
    elif feature == 'TotalBsmtSF_cat':
            new_data["TotalBsmtSF_cat"] = pd.cut(new_data["TotalBsmtSF"],
                bins=[-1, 500, 1000, 1500, 2000, 20000],
                labels=[1, 2, 3, 4, 5])
    elif feature == '1stFlrSF_cat':
            new_data["1stFlrSF_cat"] = pd.cut(new_data["1stFlrSF"],
                bins=[0, 500, 1000, 1500, 2000, 20000],
                labels=[1, 2, 3, 4, 5])
    elif feature == 'FullBath_cat':
            new_data["FullBath_cat"] = pd.cut(new_data["FullBath"],
                bins=[-1, 0.9, 1.9, 2.9, 10],
                labels=[1, 2, 3, 4])
    elif feature == 'TotRmsAbvGrd_cat':
            new_data["TotRmsAbvGrd_cat"] = pd.cut(new_data["TotRmsAbvGrd"],
                bins=[-1, 0.9, 1.9, 2.9,3.9,4.9,5.9,6.9,7.9,8.9,9.9,10.9,11.9, 20],
                labels=[1, 2, 3, 4,5,6,7,8,9,10,11,12,13])
    elif feature == 'YearBuilt_cat':
            new_data["YearBuilt_cat"] = pd.cut(new_data["YearBuilt"],
                bins=[0, 1900, 1920, 1940,1960,1980,2000,2005,2011],
                labels=[1, 2, 3, 4,5,6,7,8])
    elif feature == 'YearRemodAdd_cat':
            new_data["YearRemodAdd_cat"] = pd.cut(new_data["YearRemodAdd"],
                bins=[0, 1950, 1960,1970,1980,1990,2000,2005,2011],
                labels=[1, 2, 3, 4,5,6,7,8])
                      
    cat_columns_train = {
        "SalePrice_cat": pd.DataFrame(),
        "YearRemodAdd_cat": pd.DataFrame(),
        "YearBuilt_cat":pd.DataFrame(),
        "FullBath_cat":pd.DataFrame(),
        "1stFlrSF_cat":pd.DataFrame(),
        "TotalBsmtSF_cat":pd.DataFrame(),
        "GarageCars_cat":pd.DataFrame(),
        "GrLivArea_cat":pd.DataFrame(),
        "OverallQual_cat":pd.DataFrame()
    }
    cat_columns_test = {
        "SalePrice_cat": pd.DataFrame(),
        "YearRemodAdd_cat": pd.DataFrame(),
        "YearBuilt_cat":pd.DataFrame(),
        "TotRmsAbvGrd_cat":pd.DataFrame(),
        "FullBath_cat":pd.DataFrame(),
        "1stFlrSF_cat":pd.DataFrame(),
        "GarageCars_cat":pd.DataFrame(),
        "GrLivArea_cat":pd.DataFrame(),
        "OverallQual_cat":pd.DataFrame()
    }
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(new_data, new_data[feature]):
        cat_columns_train[feature] = new_data.loc[train_index]
        cat_columns_test[feature] = new_data.loc[test_index]           
    cat_columns_test[feature].drop(feature, axis=1, inplace=True)
    cat_columns_train[feature].drop(feature, axis=1, inplace=True)
    return cat_columns_train[feature], cat_columns_test[feature]