import streamlit as st
from utils import set_bg

set_bg()

st.title("🧾 Input Page")

salary = st.number_input("Monthly Salary (₹)", min_value=0, value=0)

st.subheader("🛒 Essentials")

rice = st.number_input("Rice (₹60/kg) - kg", min_value=0.0, value=0.0)
dal = st.number_input("Dal (₹120/kg) - kg", min_value=0.0, value=0.0)
flour = st.number_input("Flour (₹45/kg) - kg", min_value=0.0, value=0.0)
vegetables = st.number_input("Vegetables (₹40/kg) - kg", min_value=0.0, value=0.0)
fruits = st.number_input("Fruits (₹80/kg) - kg", min_value=0.0, value=0.0)
oil = st.number_input("Oil (₹150/litre)", min_value=0.0, value=0.0)
spices = st.number_input("Spices (₹200/unit)", min_value=0.0, value=0.0)
gas = st.number_input("Gas Cylinder (₹850/unit)", min_value=0.0, value=0.0)

extra = st.text_area("Extra Notes")

if st.button("🧮 Calculate"):

    total = (
        rice*60 + dal*120 + flour*45 + vegetables*40 +
        fruits*80 + oil*150 + spices*200 + gas*850
    )

    st.session_state["salary"] = salary
    st.session_state["total"] = total
    st.session_state["extra"] = extra
    st.session_state["done"] = True

    st.success(f"Total Expense: ₹{total}")

if st.session_state.get("done"):

    if st.button("➡ Next"):
        st.switch_page("pages/Result.py")