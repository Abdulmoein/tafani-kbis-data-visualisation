import streamlit as st
from datetime import datetime
# ──────────────────────────────
# ⚙️ Page configuration
# ──────────────────────────────
st.set_page_config(
    page_title="📊 Tafani • KBIS Dashboard",
    page_icon="assets/tafani-logo.png",
    layout="centered",
)



# Hide Streamlit’s default elements & small style touch‑ups
st.markdown(
    """
    <style>
        #MainMenu, .stAppDeployButton, footer {visibility: hidden;}
        .stAppDeployButton {visibility: hidden;}
#         footer {visibility: hidden;}

    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────
# 🏠 Header
# ──────────────────────────────
col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.title("💻💻")

with col_title:
    st.title("IT Department • (KBIS) 📊")
    st.markdown(
        """
        These indicators pertain to the IT sector. 🧑🏻‍💼✨
        """
    )


st.divider()


st.subheader("🔜🔜🔜Comming soon 🔜🔜🔜")


st.divider()


# ──────────────────────────────
# 📬 Contact
# ──────────────────────────────
st.subheader("Got a question? Contact us 📬")
contact_cols = st.columns(2)
with contact_cols[0]:
    st.markdown(
        """
        ** 📧Email**  
        it@tafani.ly 


        """
    )
with contact_cols[1]:
    st.markdown(
        """
        **📞landline number**  
        114
        """
    )



# ──────────────────────────────
# 📌 Footer (sticky)
# ──────────────────────────────
current_year = datetime.now().year

st.markdown(
    f"""
    <style>
        /* Sticky footer */
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #f2f3f8;
            border-top: 1px solid #e0e0e0;
            text-align: center;
            padding: 0.4rem 0;
            font-size: 0.85rem;
            color: #555;
        }}


        .footer a {{
            color: inherit;
            text-decoration: none;
            font-weight: 600;
        }}
        .footer a:hover {{
            text-decoration: underline;
        }}


        .stApp {{padding-bottom: 40px;}}
    </style>

    <div class='footer'>
        Made with 💖 by <a href="https://tafani.ly/">Tafani Telecom & Technology 🚀</a>
        &nbsp;|&nbsp; © 2012 – {current_year}
    </div>
    """,
    unsafe_allow_html=True,
)