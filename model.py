import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib
import matplotlib.pyplot as plt

# 1. Load Dataset

df = pd.read_csv("Household_Item_Consumption_Sorted_Year_Date_Household.csv")

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

# 2. Date Processing

df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"], format="%d.%m.%y")
df["Year"] = df["Purchase_Date"].dt.year
df["Month"] = df["Purchase_Date"].dt.month

# 3. Monthly Aggregation

monthly_data = df.groupby(["Year", "Month", "Item"])["Quantity"].sum().reset_index()
print("\nMonthly Aggregated Data:")
print(monthly_data.head())
print("\nTotal rows after aggregation:", len(monthly_data))

# 4. Pivot Table

pivot_df = monthly_data.pivot_table(
    index=["Year", "Month"],
    columns="Item",
    values="Quantity",
    fill_value=0
).reset_index()

print("\nPivoted Monthly Data:")
print(pivot_df.head())
print("\nTotal rows after pivot:", len(pivot_df))

# 5. Model Training

X = pivot_df[["Year", "Month"]]
y = pivot_df.drop(columns=["Year", "Month"])

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
# Save target column names for later
import pickle
with open("target_columns.pkl", "wb") as f:
    pickle.dump(y.columns.tolist(), f)

# Evaluate
y_pred = model.predict(X)
print("\nR2 Score (overall):", r2_score(y, y_pred))

# Save model
joblib.dump(model, "household_model.pkl")

# 6. Next Month Prediction

next_month = pd.DataFrame({"Year": [2026], "Month": [2]})
prediction = model.predict(next_month)
prediction_df = pd.DataFrame(prediction, columns=y.columns).round(0)

print("\nPrediction for next month:")
print(prediction_df)

# 7. Graphs

# 7a. Actual vs Predicted Total Quantity
actual_total = y.sum(axis=1)
predicted_total = y_pred.sum(axis=1)

plt.figure(figsize=(10,5))
plt.plot(actual_total.values, marker='o', label="Actual Total")
plt.plot(predicted_total, marker='x', label="Predicted Total")
plt.title("Actual vs Predicted Total Quantity (Monthly)")
plt.xlabel("Month Index")
plt.ylabel("Total Quantity")
plt.legend()
plt.show()

# 7b. Next Month Prediction per Item
plt.figure(figsize=(12,5))
plt.bar(prediction_df.columns, prediction_df.iloc[0], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Predicted Household Item Consumption for Next Month")
plt.ylabel("Quantity")
plt.tight_layout()
plt.show()