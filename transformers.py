import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer

def load_data(path):
    return pd.read_csv(path+ '.csv')


def split_data(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 0, train_size = 0.8)
    return X_train, X_test, y_train, y_test


def transformers():
    num_transformers = Pipeline(steps= [('Imputer', SimpleImputer(strategy= 'median')), ('scale', MinMaxScaler())])
    cat_transformers = Pipeline(steps= [('Imputer', SimpleImputer(strategy= 'most_frequent', fill_value= 'missing')), ('onehot', OneHotEncoder())])
    return num_transformers, cat_transformers
    
def create_model(X_train, model):
    num_transformers, cat_transformers = transformers()
    num_variables = X_train.select_dtypes(include = ['int32', 'int64', 'float64']).columns
    cat_variables = X_train.select_dtypes(include= ['object']).columns
    preprocessing = ColumnTransformer(transformers= [('numeric', num_transformers, num_variables), 
                                                 ('categorical', cat_transformers, cat_variables)], 
                                      remainder= 'passthrough')
    rf = Pipeline(steps= [('preprocessing', preprocessing), ('model', model)])
    return rf                         