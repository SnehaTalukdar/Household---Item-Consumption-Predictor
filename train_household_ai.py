import pandas as pd
import os
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -------------------- LOAD DATA --------------------
file_path = os.path.join(
    os.getcwd(),
    "Household_Item_Consumption_Sorted_Year_Date_Household.csv"
)

df = pd.read_csv(file_path)

# -------------------- DATE CLEANING --------------------
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

# -------------------- FEATURES & TARGET --------------------
X = df[["Year", "Month", "Day"]]
y = df["Quantity"]

# -------------------- TRAIN TEST SPLIT --------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------- MODEL TRAINING --------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

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

# -------------------- GRAPH 1: ACTUAL VS PREDICTED --------------------
plt.figure()
plt.plot(y_test.values[:50], label="Actual")
plt.plot(y_pred[:50], label="Predicted")
plt.title("Actual vs Predicted Quantity")
plt.legend()
plt.grid()
plt.show()

# -------------------- GRAPH 2: ERROR DISTRIBUTION --------------------
errors = y_test.values - y_pred

plt.figure()
plt.hist(errors, bins=20)
plt.title("Prediction Error Distribution")
plt.grid()
plt.show()

# -------------------- GRAPH 3: SCATTER PLOT --------------------
plt.figure()
plt.scatter(y_test, y_pred)
plt.title("Actual vs Predicted (Scatter Plot)")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.grid()
plt.show()

# -------------------- SAVE MODEL --------------------
joblib.dump(model, "household_model.pkl")

print("\n✅ MODEL TRAINED AND SAVED SUCCESSFULLY")