import pandas as pd
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -------------------- LOAD DATA --------------------
file_path = os.path.join(
    os.getcwd(),
    "Household_Item_Consumption_Sorted_Year_Date_Household.csv"
)

df = pd.read_csv(file_path)

# -------------------- DATE FIX --------------------
df["Purchase_Date"] = pd.to_datetime(
    df["Purchase_Date"],
    format="mixed",
    errors="coerce"
)

df = df.dropna(subset=["Purchase_Date"])

# -------------------- FEATURE ENGINEERING --------------------
df["Year"] = df["Purchase_Date"].dt.year
df["Month"] = df["Purchase_Date"].dt.month
df["Day"] = df["Purchase_Date"].dt.day

df["Item"] = df["Item"].astype("category").cat.codes

# -------------------- FEATURES / TARGET --------------------
X = df[["Item", "Year", "Month", "Day"]]
y = df["Quantity"]

# -------------------- TRAIN TEST SPLIT --------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------- MODEL --------------------
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -------------------- PREDICTION --------------------
y_pred = model.predict(X_test)

# -------------------- METRICS --------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# -------------------- 📉 GRAPH 1: ACTUAL vs PREDICTED --------------------
plt.figure(figsize=(8,5))
plt.plot(y_test.values[:50], label="Actual", marker='o')
plt.plot(y_pred[:50], label="Predicted", marker='x')
plt.title("Actual vs Predicted Quantity")
plt.xlabel("Samples")
plt.ylabel("Quantity")
plt.legend()
plt.grid()
plt.show()

# -------------------- 📉 GRAPH 2: ERROR DISTRIBUTION --------------------
errors = y_test.values - y_pred

plt.figure(figsize=(8,5))
plt.hist(errors, bins=20, color='skyblue')
plt.title("Prediction Error Distribution")
plt.xlabel("Error")
plt.ylabel("Frequency")
plt.grid()
plt.show()

# -------------------- 📉 GRAPH 3: SCATTER PLOT --------------------
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)
plt.title("Actual vs Predicted (Scatter)")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.grid()
plt.show()

# -------------------- SAVE MODEL --------------------
with open("household_ai_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n✅ AI MODEL TRAINED SUCCESSFULLY")
print("📦 Model saved as household_ai_model.pkl")