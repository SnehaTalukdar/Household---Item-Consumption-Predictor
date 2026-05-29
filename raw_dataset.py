import pandas as pd
import random

# ---------------- SETTINGS ----------------
items = ["Rice", "Lentils", "Oil", "Vegetables", "Fruits", "Flour", "Spices", "Gas"]

price_map = {
    "Rice": 60,
    "Lentils": 120,
    "Oil": 150,
    "Vegetables": 40,
    "Fruits": 80,
    "Flour": 45,
    "Spices": 200,
    "Gas": 850
}

data = {
    "Purchase_Date": [],
    "Item": [],
    "Quantity": [],
    "Price": []
}

# ---------------- GENERATE DATA (2026 FULL YEAR) ----------------
for month in range(1, 13):
    for _ in range(10):  # 10 transactions per month

        item = random.choice(items)

        data["Purchase_Date"].append(f"2026-{month:02d}-15")
        data["Item"].append(item)
        data["Quantity"].append(random.randint(1, 5))
        data["Price"].append(price_map[item])

# ---------------- CREATE DATAFRAME ----------------
df = pd.DataFrame(data)

# ---------------- SAVE RAW DATA ----------------
df.to_csv("household_raw.csv", index=False)

print("✅ Raw dataset created")
print(df.head())