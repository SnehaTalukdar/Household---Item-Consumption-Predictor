import streamlit as st
from utils import set_bg

set_bg()

st.title("🎉 Thank You!")

st.success("Happy Shopping 🛍️")

if st.button("🏠 Back to Home"):
    st.switch_page("streamlit_app.py")