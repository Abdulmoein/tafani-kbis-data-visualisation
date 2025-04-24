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
    st.title("🧑🏻‍💼🧑🏻‍💼")

with col_title:
    st.title("HR Department • (KBIS) 📊")
    st.markdown(
        """
        These indicators pertain to the human resources sector. 🧑🏻‍💼✨
        """
    )


st.divider()

# ──────────────────────────────
# 🏢  Employee Turnover Rate
# ──────────────────────────────
st.subheader("🔄️🧑🏻‍💼Employee Turnover Rate")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the employee turnover rate, which is the percentage of employees who left the company during a specific period compared to the average number of employees at the beginning and end of that period. It reflects the effectiveness of employee retention strategies and provides insight into workforce stability. 
    """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()



# ──────────────────────────────
# 🏢  Employee Retention Rate
# ──────────────────────────────
st.subheader("🧑‍💼📈Employee Retention Rate")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the employee retention rate, which is the percentage of employees who remained with the company at the end of a specific period compared to the number of employees at the beginning of the period. It reflects the effectiveness of retention strategies and the overall work environment that influences employee stability.     """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()




# ──────────────────────────────
# 🏢  Employee Turnover Rate
# ──────────────────────────────
st.subheader("🔄️🧑🏻‍💼Employee Turnover Rate")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the employee turnover rate, which is the percentage of employees who left the company during a specific period compared to the average number of employees at the beginning and end of that period. It reflects the effectiveness of employee retention strategies and provides insight into workforce stability. 
    """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()




# ──────────────────────────────
# 🏢   	Employee Engagement Rate
# ──────────────────────────────
st.subheader("🧑‍💼💬Employee Engagement Rate")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the employee engagement rate, which is determined by the results of the employee integration survey conducted during a specific period. It reflects the level of employee involvement, satisfaction, and their emotional commitment to the organization.     """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()




# ──────────────────────────────
# 🏢  Vacant Positions Filling Period
# ──────────────────────────────
st.subheader("🕒📋Vacant Positions Filling Period")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the average time taken to fill vacant positions in the company, expressed in working days. It is calculated by dividing the total number of working days to fill vacancies by the number of jobs filled during a specific period. It reflects the efficiency of the recruitment process in terms of time taken to fill open positions.     """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()




# ──────────────────────────────
# 🏢 Recruitment Failure Rate
# ──────────────────────────────
st.subheader("❌📉Recruitment Failure Rate")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the recruitment failure rate, which is the percentage of new employees who failed (did not meet performance expectations or left the company) compared to the total number of new employees hired during a specific period. It helps.    """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()





# ──────────────────────────────
# 🏢  Employee Absenteeism Rate
# ──────────────────────────────
st.subheader("🚶‍♂️📉Employee Absenteeism Rate")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the absenteeism rate of employees, calculated as the percentage of total days employees were absent in a specific month compared to the total working days for all employees during that month. It helps to assess employees.
"""
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()




# ──────────────────────────────
# 🏢  Rate Of Completion Of Training Programs
# ──────────────────────────────
st.subheader("🎓✅Rate Of Completion Of Training Programs")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the rate of completion of training programs, calculated as the percentage of employees who have completed a training program compared to the total number of employees targeted for training during a specific period. It helps to assess the effectiveness and engagement of employees in training initiatives.    """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()




# ──────────────────────────────
# 🏢  Employee Satisfaction Rate"
# ──────────────────────────────
st.subheader("😊📊Employee Satisfaction Rate")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the employee satisfaction rate based on the scores from an employee satisfaction survey conducted during a specific period. It reflects the overall satisfaction and engagement of employees with their work environment, management, and the organization.    """
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


st.divider()



# ──────────────────────────────
# 🏢  Employee Performance Evaluation Percentage
# ──────────────────────────────
st.subheader("Employee Performance Evaluation Percentage")
st.markdown(
    """
This Key Behavioral Indicator (KBI) measures the percentage of employees evaluated during a specific period. It is calculated by dividing the number of evaluated employees by the total number of employees. This metric helps assess the company's commitment to regular performance reviews, supporting employee development and productivity. A higher percentage indicates effective performance monitoring and feedback."""
)

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

st.bar_chart({"X": x, "Y": y})


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