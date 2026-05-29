import streamlit as st
from utils import set_bg

st.set_page_config(page_title="Household Budget", layout="wide")

set_bg()

st.title("🏠 Welcome to Household Item and Budget Tracker")
st.write("Plan your monthly expenses smartly 💰")

if st.button("🚀 Start"):
    st.switch_page("pages/Input.py")