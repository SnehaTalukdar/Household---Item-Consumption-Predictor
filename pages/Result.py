import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from utils import set_bg

set_bg()

model = joblib.load("household_model.pkl")

st.title("📊 ML Prediction Result")

if "input_data" not in st.session_state:
    st.warning("Go to Input page first")
    st.stop()

data = st.session_state["input_data"]

X = pd.DataFrame([data])

prediction = model.predict(X)[0]
salary = data["Salary"]

# ---------------- STATUS ----------------
if prediction > salary:
    status = "❌ OVER BUDGET"
elif prediction < salary * 0.7:
    status = "✅ UNDER BUDGET"
else:
    status = "⚖️ OPTIMAL"

st.metric("Predicted Expense", f"₹{round(prediction,2)}")
st.metric("Salary", f"₹{salary}")
st.write("Status:", status)

# ---------------- GRAPH ----------------
st.subheader("📊 Item-wise Consumption")

items = list(data.keys())[2:]
values = list(data.values())[2:]

fig, ax = plt.subplots()
ax.bar(items, values)
plt.xticks(rotation=45)

st.pyplot(fig)

if st.button("➡ NEXT"):
    st.switch_page("pages/Thank_You.py")