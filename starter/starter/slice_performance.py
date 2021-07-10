import pandas as pd
import joblib
from ml.model import *

df = pd.read_csv("../data/census_nospaces.csv")
model = joblib.load("../model/model.pkl") 
encoder = joblib.load("../model/encoder.enc")
lb = joblib.load("../model/lb.enc")

def get_sliced_metrics(df, feature):
    """ Function for calculating performance on slices of the dataset."""
    for cls in df[feature].unique():
        df_temp = df[df[feature] == cls]
        X_test, y_test, encoder, lb = process_data(
            test, categorical_features=cat_features, label="salary", training=False,
            encoder = encoder, lb = lb)
        
        preds = inference(model, X_test)
        precision, recall, fbeta = compute_model_metrics(y_test, preds)
        print(f"Class: {cls}")
        print(f"{feature} precision: {precision:.4f}")
        print(f"{feature} recall: {recall:.4f}")
        print(f"{feature} fbeta: {fbeta:.4f}")
    print()

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

for feat in cat_features:
    get_sliced_metrics(df, feat)
