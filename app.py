import streamlit as st
from utils import set_bg

set_bg()

# ---------------- HOME PAGE ----------------
st.title("🏠 Household Item and Budget ML System")

st.markdown("""
Welcome to the **Smart Household Expense Predictor** 💰

This system uses **Machine Learning (Random Forest Regressor)** to:
- Predict monthly household expenses
- Analyze spending behavior
- Compare income vs expenses
""")

st.info("Use the sidebar to navigate: Input → Result → Thank You")

# ---------------- START BUTTON ----------------
st.markdown("### 🚀 Start Your Budget Analysis")

if st.button("START"):
    st.switch_page("pages/Input.py")