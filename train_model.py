import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# ---------------- LOAD DATA ----------------
df = pd.read_csv("household_ml_dataset.csv")

# ---------------- FEATURES & TARGET ----------------
X = df.drop("Expense", axis=1)
y = df["Expense"]

# ---------------- TRAIN TEST SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ----------------
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=12,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- PREDICTION ----------------
y_pred = model.predict(X_test)

# ---------------- METRICS ----------------
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("MAE:", mae)
print("RMSE:", rmse)

# ======================================================
# 📊 1. ACTUAL vs PREDICTED GRAPH
# ======================================================
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Expense")
plt.ylabel("Predicted Expense")
plt.title("Actual vs Predicted Expense")
plt.grid()
plt.show()

# ======================================================
# 📉 2. ERROR DISTRIBUTION
# ======================================================
errors = y_test - y_pred

plt.figure()
plt.hist(errors, bins=20)
plt.title("Prediction Error Distribution")
plt.xlabel("Error")
plt.ylabel("Frequency")
plt.grid()
plt.show()

# ======================================================
# 🌲 3. FEATURE IMPORTANCE (VERY IMPORTANT FOR RF)
# ======================================================
importances = model.feature_importances_
features = X.columns

plt.figure()
plt.barh(features, importances)
plt.title("Feature Importance (Random Forest)")
plt.xlabel("Importance Score")
plt.grid()
plt.show()

# ---------------- SAVE MODEL ----------------
joblib.dump(model, "household_model.pkl")

print("✅ REAL ML MODEL TRAINED + EVALUATED")