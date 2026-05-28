import streamlit as st
from utils import set_bg

set_bg()

st.title("🏠 Household Budget Tracker")

st.write("Plan your monthly expenses smartly 💰")

if st.button("🚀 Start"):
    st.switch_page("pages/Input.py")