import streamlit as st
from utils import set_bg

set_bg()

st.title("🧾 Household ML Input")

salary = st.number_input("Salary (₹)", 0)
family = st.number_input("Family Size", 1, 10)

rice = st.number_input("Rice (kg)", 0)
lentils = st.number_input("Lentils (kg)", 0)
oil = st.number_input("Oil (L)", 0)
veg = st.number_input("Vegetables (kg)", 0)
fruits = st.number_input("Fruits (kg)", 0)
gas = st.number_input("Gas Cylinders", 0)
spices = st.number_input("Spices (kg)", 0)

st.session_state["input_data"] = {
    "Salary": salary,
    "Family_Size": family,
    "Rice": rice,
    "Lentils": lentils,
    "Oil": oil,
    "Vegetables": veg,
    "Fruits": fruits,
    "Gas": gas,
    "Spices": spices
}

if st.button("➡ NEXT"):
    st.switch_page("pages/Result.py")