import pandas as pd
import pytest
import joblib
from .ml.data import *
from .ml.model import *

@pytest.fixture
def data():
    """ Load initial data """
    return pd.read_csv("./starter/data/census_nospaces.csv")

@pytest.fixture
def model():
    """ Load a pretrained model """
    return joblib.load("./starter/model/model.pkl")

def test_preprocess_data(data):
    """ Check to see if there are no . """
    try:    
        cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
        process_data(data, categorical_features=cat_features, label="salary", training=True)
    except:
        assert False
    assert True
    
def test_model(model):
    try:
        model.best_estimator_
    except:
        assert False
    assert True
    
def test_inference(data):
    try:
        model = joblib.load("./starter/model/model.pkl")
        X, _, _, _ = process_data(data, categorical_features=cat_features, label="salary", training=True)
        inference(model, X)
    except:
        assert False
    assert True 
