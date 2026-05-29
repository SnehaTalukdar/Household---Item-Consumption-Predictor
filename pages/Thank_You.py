import streamlit as st
from utils import set_bg

set_bg()

st.title("🎉 Thank You!")

st.success("✔ Analysis Completed")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 BACK TO HOME"):
        st.switch_page("app.py")

with col2:
    if st.button("🔄 DONE"):
        st.session_state.clear()
        st.switch_page("app.py")