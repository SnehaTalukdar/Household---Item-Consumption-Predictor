import joblib
import pandas as pd
import pickle

# Load the saved model
model = joblib.load("household_model.pkl")

# Load target column names
with open("target_columns.pkl", "rb") as f:
    target_columns = pickle.load(f)

# Predict next month (Feb 2026)
next_month = pd.DataFrame({"Year":[2026], "Month":[2]})
prediction = model.predict(next_month)

# Convert to DataFrame for readability
prediction_df = pd.DataFrame(prediction, columns=target_columns)
print("Prediction for next month:")
print(prediction_df.round(0))