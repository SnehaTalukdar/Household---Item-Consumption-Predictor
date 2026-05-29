import streamlit as st
from utils import set_bg

set_bg()

st.title("📊 Budget Result")

salary = st.session_state.get("salary", 0)
total = st.session_state.get("total", 0)

balance = salary - total

st.write(f"💰 Salary: ₹{salary}")
st.write(f"🧾 Total Expense: ₹{total}")
st.write(f"💵 Savings: ₹{balance}")

if balance < 0:
    st.error(f"🔴 Over Budget by ₹{abs(balance)}")
elif balance <= 2000:
    st.warning("🟡 Under Budget (Low Savings)")
else:
    st.success("🟢 Optimal Budget")

st.divider()

if st.button("🎉 Finish"):
    st.switch_page("pages/Thank_You.py")