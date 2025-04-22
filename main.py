import streamlit as st
from components.sidebar import navigation

page = navigation()

if page == "🏠Home":
    from pages.home import show
    
elif page == "👨🏻‍💻HR KBIS":
    from pages.hr_kbis import show
    
elif page == "💻IT KBIS":
    from pages.it_kbis import show

show()
