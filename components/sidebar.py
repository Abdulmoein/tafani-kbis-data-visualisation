import streamlit as st

def navigation():
    
    st.sidebar.title("📊Tafani KBIS Panel")
    
    page = st.sidebar.radio("", ["🏠Home", "👨🏻‍💻HR KBIS", "💻IT KBIS"])
    
    return page