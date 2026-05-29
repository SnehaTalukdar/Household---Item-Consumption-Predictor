import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from utils import set_bg

set_bg()

# ---------------- LOAD MODEL ----------------
model = joblib.load("household_model.pkl")

st.title("📊 ML Prediction Result")

# ---------------- CHECK SESSION ----------------
if "input_data" not in st.session_state:
    st.warning("Go to Input page first")
    st.stop()

data = st.session_state["input_data"]

# ======================================================
# REMOVE SALARY BEFORE PREDICTION
# because model was trained without Salary
# ======================================================
input_data = data.copy()

input_data.pop("Salary")

X = pd.DataFrame([input_data])

# ---------------- PREDICTION ----------------
prediction = model.predict(X)[0]

salary = data["Salary"]

# ---------------- STATUS ----------------
if prediction > salary:
    status = "❌ OVER BUDGET"

elif prediction < salary * 0.7:
    status = "✅ UNDER BUDGET"

else:
    status = "⚖️ OPTIMAL"

# ---------------- METRICS ----------------
st.metric("Predicted Expense", f"₹{round(prediction, 2)}")

st.metric("Salary", f"₹{salary}")

st.write("Status:", status)

# ---------------- GRAPH ----------------
st.subheader("📊 Item-wise Consumption")

items = list(input_data.keys())[1:]
values = list(input_data.values())[1:]

fig, ax = plt.subplots(figsize=(7, 4))

ax.bar(items, values)

plt.xticks(rotation=45)

st.pyplot(fig)

# ---------------- NEXT PAGE ----------------
if st.button("➡ NEXT"):
    st.switch_page("pages/Thank_You.py")