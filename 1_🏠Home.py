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

        /* 🎯 highlight box */
        .highlight-box {
            background-color:rgba(173, 19, 173, 0.4);
            padding:0.6rem 1rem;
            border-radius:10px;
            font-size:1.1rem;
            font-weight:600;
            display:inline-block;
            margin-top:0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────
# 🏠 Header
# ──────────────────────────────
col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.image("assets/tafani-logo.png", width=120)

with col_title:
    st.title("Tafani • (KBIS) Dashboard Project 📈")
    st.markdown(
        """
        This project is designed to **measure** the performance of **Tafani Telecom & Technology**  
        by deploying **Key Behavior Indicators (KBIs)** across every division and department.  
        By making data‑driven insights readily available, it empowers *faster, smarter* decision‑making and brings the company’s strategic vision into sharp focus. 📊✨
        """
    )
    # 🎯 highlighted tagline
    st.markdown(
        "<div class='highlight-box'>🎯💪TAFANI is a real transformation</div>",
        unsafe_allow_html=True,
    )

st.divider()

# ──────────────────────────────
# 🏢 About us
# ──────────────────────────────
st.subheader("Who we are 🏢")
st.markdown(
    """
**Tafani** is a **FinTech** company specializing in digital transformation and business intelligence since **2012**.

🎯 **Our goal:** Toward a smart tech environment.

🚀 **Our mission:** To adapt and facilitate service technology for the benefit of society.

🌟 **Our values**
- 💪 **Dedication**
- 🤝🏻 **Loyalty**
- 💯 **Integrity**
- 💡 **Innovation**
- 🎯 **Audacity**
- 🤝 **Sharing**
    """
)

st.divider()

# ──────────────────────────────
# 🚀 KBIS at a glance
# ──────────────────────────────
st.subheader("What is KBIS? 🚀")
st.markdown(
    """
**KBIS – Key Behavior Indicators System** is our company‑wide framework for defining, tracking, and acting on the
behaviors that truly drive business success.  
By unifying data from every department (🧑🏻‍💼HR, 💸Commercial, 💻IT, …​) and translating it into clear, behavior‑based metrics,
KBIS turns scattered activity into actionable insight.

**Why KBIS matters — top benefits**  
- 📏 **Measure performance precisely** — quantify how teams and individuals behave against strategic targets.  
- 🧭 **Guide strategic & managerial decisions** — focus leadership on the behaviors that move the needle, not just the outcomes.  
- ⚡ **Accelerate operational agility** — surface emerging trends early so managers can pivot in real time.  
- 🔄 **Drive continuous improvement** — give every division a feedback loop to experiment, learn, and refine processes.  
- 🎯 **Align the entire organization** — create a common language where goals, incentives, and daily actions all point in the same direction.  
- 🛡️ **Strengthen accountability & transparency** — fine‑grained permissions ensure the right people see the right insights while everyone knows the score.  
    """
)

st.link_button("Open the KBIS data entry dashboard »", "http://localhost:5000/main/en/")

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