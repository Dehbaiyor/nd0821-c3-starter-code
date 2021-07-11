import joblib
from ml.model import *

X_train = joblib.load("../data/X_train.pkl")
X_test = joblib.load("../data/X_test.pkl")
y_train =joblib.load("../data/y_train.pkl")
y_test = joblib.load("../data/y_test.pkl")
model = joblib.load("../model/model.pkl")

def print_metrics(model, X, y, description):
    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    print(description)
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"Fbeta: {fbeta:.4f}")
    print()
    
print_metrics(model, X_train, y_train, "Training Set Metrics")
print_metrics(model, X_test, y_test, "Test Set Metrics")