import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# LOAD DATA
df = pd.read_csv("household_data.csv")

# FEATURES
X = df.drop("TotalExpense", axis=1)

# TARGET
y = df["TotalExpense"]

# TRAIN MODEL
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# SAVE MODEL
joblib.dump(model, "budget_model.pkl")

print("MODEL TRAINED SUCCESSFULLY")