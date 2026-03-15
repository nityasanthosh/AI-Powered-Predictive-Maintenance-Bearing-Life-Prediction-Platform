import joblib
import numpy as np

model = joblib.load("model/rul_model.pkl")

def predict_bearing_life(sensor_data):
    """
    Prediction model intentionally removed from public repository.
    This function is a placeholder for the trained RUL model.
    """
    raise Exception("Trained model not included in this repository.")

    return round(prediction,2)
