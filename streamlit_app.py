import streamlit as st

st.set_page_config(page_title="Household Budget", layout="wide")

st.title("🏠 Welcome to Household Budget Tracker")
st.write("Plan your monthly expenses smartly 💰")

if st.button("🚀 Start"):
    st.switch_page("pages/Input.py")