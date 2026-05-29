import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

df = pd.DataFrame({
    "Salary": np.random.randint(20000, 100000, n),
    "Family_Size": np.random.randint(1, 6, n),

    "Rice": np.random.randint(5, 25, n),
    "Lentils": np.random.randint(2, 15, n),
    "Oil": np.random.randint(1, 8, n),
    "Vegetables": np.random.randint(5, 30, n),
    "Fruits": np.random.randint(2, 20, n),
    "Gas": np.random.randint(0, 4, n),
    "Spices": np.random.randint(1, 10, n)
})

# ---------------- REALISTIC EXPENSE MODEL (with noise) ----------------
df["Expense"] = (
    df["Rice"] * 60 +
    df["Lentils"] * 120 +
    df["Oil"] * 150 +
    df["Vegetables"] * 40 +
    df["Fruits"] * 80 +
    df["Gas"] * 850 +
    df["Spices"] * 200 +
    df["Family_Size"] * 1000   # lifestyle effect
)

# add randomness (VERY IMPORTANT for ML realism)
df["Expense"] = df["Expense"] + np.random.randint(-1000, 1000, n)

df.to_csv("household_ml_dataset.csv", index=False)

print("✅ REALISTIC ML DATASET CREATED")