import streamlit as st
import base64

def set_bg():
    with open("PIC.png", "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>

    /* Background image */
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Blur overlay */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        backdrop-filter: blur(8px);
        background-color: rgba(0,0,0,0.2);
        z-index: 0;
    }}

    /* Bring content above blur */
    .main {{
        position: relative;
        z-index: 1;
        font-size: 20px;
        font-weight: 700;
        color: #111;
    }}

    /* Make text bold + dark */
    h1, h2, h3, p, label {{
        color: #111 !important;
        font-weight: 800 !important;
    }}

    </style>
    """, unsafe_allow_html=True)