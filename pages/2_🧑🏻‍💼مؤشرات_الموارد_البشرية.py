import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px

import requests

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
    .stMain {
        direction: rtl;
    }

    #MainMenu {
        visibility: hidden;
    }
    .stAppDeployButton {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
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
    st.title("🧑🏻‍💼🧑🏻‍💼")

with col_title:
    st.title("قطاع الموارد البشرية • (KBIS) 📊")
    st.markdown(
        """
        المؤشرات التي بالأسفل تخص قطاع الموارد البشرية. 🧑🏻‍💼✨
        """
    )


st.divider()

# ──────────────────────────────
# 🏢  Employee Turnover Rate
# ──────────────────────────────
st.subheader("🔄️🧑🏻‍💼معدل دوران الموظفين")
st.markdown(
    """
هذا المؤشر (KBI) يقيس معدل دوران الموظفين، وهو النسبة المئوية للموظفين الذين غادروا الشركة خلال فترة معينة مقارنةً بمتوسط عدد الموظفين في بداية ونهاية تلك الفترة, يعكس هذا المؤشر فعالية استراتيجيات الاحتفاظ بالموظفين ويوفر رؤية حول استقرار القوى العاملة.    """
)

# تحديد السنة والشهر من خلال مفاتيح فريدة لكل حقل
current_year = datetime.now().year
years = list(range(2012, current_year + 16))
months = list(range(1, 13))

col1, col2 = st.columns(2)
with col1:
    start_year = st.selectbox("سنة البداية", years, index=years.index(current_year), key="start_year_turnover")
    start_month = st.selectbox("شهر البداية", months, index=0, key="start_month_turnover")

with col2:
    end_year = st.selectbox("سنة النهاية", years, index=years.index(current_year), key="end_year_turnover")
    end_month = st.selectbox("شهر النهاية", months, index=11, key="end_month_turnover")

# رابط الـ API الخاص بمعدل دوران الموظفين
api_url = f"http://localhost:5000/api/employee_turnover_rate/average_by_month/?start_year={start_year}&start_month={start_month}&end_year={end_year}&end_month={end_month}"

try:
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        if data:
            df = pd.DataFrame(data)
            
            # تغيير تنسيق التاريخ ليعرض السنة والشهر فقط (بدون اليوم والساعة)
            df["month"] = pd.to_datetime(df["month"], format="%Y-%m").dt.strftime('%Y-%m')

            # إضافة % إلى calculated_value لعرضها بشكل مئوي
            df["calculated_value_with_percent"] = df["calculated_value"].apply(lambda x: f"{x}%" if pd.notna(x) else "0%")

            # تلوين حسب القيم وتغيير كلمة color إلى status
            df["الحالة"] = df["calculated_value"].apply(lambda x: 'معدل طبيعي' if x >= 10 else 'تحت الطبيعي')

            # تعديل الأسماء الإنجليزية الطويلة إلى أسماء مختصرة بالعربية
            df["عدد الموظفين المغادرين"] = df["number_of_departing_employees"]
            df["عدد الموظفين في بداية ونهاية الفترة"] = df["average_number_of_employees_at_the_beginning_and_end_of_the_period"]

            # حذف الأعمدة الأصلية التي تحتوي على الأسماء الطويلة
            df = df.drop(columns=["number_of_departing_employees", "average_number_of_employees_at_the_beginning_and_end_of_the_period", "calculated_value"])

            # إعادة تعيين الفهرس ليبدأ من 1
            df.index = df.index + 1

            # تعديل اسم العمود من 'month' إلى 'التاريخ'
            df.rename(columns={'month': 'التاريخ', 'calculated_value_with_percent': 'النتيجة'}, inplace=True)

            # عرض البيانات في جدول
            st.write("### البيانات المحدثة:")
            st.dataframe(df)

            st.divider()
            st.subheader("📊 اختر نوع الرسوم البيانية لعرض البيانات:")

            # إضافة مفتاح فريد للـ multiselect
            chart_types = st.multiselect(
                "أنواع الرسوم:",
                ["📊 Bar Chart", "📈 Line Chart", "💥 Scatter Chart"],
                default=["📊 Bar Chart"],
                key="chart_types_turnover"  # مفتاح فريد لهذا العنصر
            )

            # البيانات التي تظهر عند التمرير فوق العناصر
            hover_data = {
                "التاريخ": True,
                "النتيجة": True,
                "عدد الموظفين المغادرين": True,
                "عدد الموظفين في بداية ونهاية الفترة": True,
                "الحالة": False  # الحالة لا تحتاج لإظهارها في hover_data
            }

            # إضافة الرسوم البيانية بناءً على الاختيارات
            if "📊 Bar Chart" in chart_types:
                st.write("### 📊 Bar Chart")
                fig = px.bar(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Bar Chart"
                )
                st.plotly_chart(fig)

            if "📈 Line Chart" in chart_types:
                st.write("### 📈 Line Chart")
                fig = px.line(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    markers=True,
                    title="Line Chart"
                )
                st.plotly_chart(fig)

            if "💥 Scatter Chart" in chart_types:
                st.write("### 💥 Scatter Chart")
                fig = px.scatter(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Scatter Chart"
                )
                st.plotly_chart(fig)

        else:
            st.warning("❗ لا توجد بيانات في الفترة المحددة.")
    else:
        st.error(f"خطأ في الاتصال بالسيرفر: {response.status_code}")

except Exception as e:
    st.error(f"حدث خطأ أثناء جلب البيانات: {e}")

st.divider()

# ──────────────────────────────
# 🏢  Employee Retention Rate
# ──────────────────────────────
st.subheader("🧑‍💼📈معدل الإحتفاظ الموظفين")
st.markdown(
    """
ذا مؤشر السلوك الرئيسي (KBI) يقيس معدل الاحتفاظ بالموظفين، وهو النسبة المئوية للموظفين الذين استمروا في العمل بالشركة في نهاية فترة معينة مقارنةً بعدد الموظفين في بداية تلك الفترة. يعكس هذا المؤشر فعالية استراتيجيات الاحتفاظ بالموظفين وبيئة العمل بشكل عام التي تؤثر على استقرار الموظفين.
"""
)

# نفس الإجراءات الخاصة بالمعدل
col1, col2 = st.columns(2)
with col1:
    start_year = st.selectbox("سنة البداية", years, index=years.index(current_year), key="start_year_retention")
    start_month = st.selectbox("شهر البداية", months, index=0, key="start_month_retention")

with col2:
    end_year = st.selectbox("سنة النهاية", years, index=years.index(current_year), key="end_year_retention")
    end_month = st.selectbox("شهر النهاية", months, index=11, key="end_month_retention")

# رابط الـ API الخاص بمعدل احتفاظ الموظفين
employee_retention_api_url = f"http://localhost:5000/api/employee_retention_rate/average_by_month/?start_year={start_year}&start_month={start_month}&end_year={end_year}&end_month={end_month}"

try:
    response = requests.get(employee_retention_api_url)

    if response.status_code == 200:
        data = response.json()

        if data:
            df = pd.DataFrame(data)
            
            # تغيير تنسيق التاريخ ليعرض السنة والشهر فقط (بدون اليوم والساعة)
            df["month"] = pd.to_datetime(df["month"], format="%Y-%m").dt.strftime('%Y-%m')

            # إضافة % إلى calculated_value لعرضها بشكل مئوي
            df["calculated_value_with_percent"] = df["calculated_value"].apply(lambda x: f"{x}%" if pd.notna(x) else "0%")

            # تلوين حسب القيم وتغيير كلمة color إلى status
            df["الحالة"] = df["calculated_value"].apply(lambda x: 'معدل طبيعي' if x >= 90 else 'تحت الطبيعي')

            # تعديل الأسماء الإنجليزية الطويلة إلى أسماء مختصرة بالعربية
            df["عدد الموظفين في بداية الفترة"] = df["number_of_employees_at_the_beginning_of_the_period"]
            df["عدد الموظفين في نهاية الفترة"] = df["number_of_employees_at_the_end_of_the_period"]

            # حذف الأعمدة الأصلية التي تحتوي على الأسماء الطويلة
            df = df.drop(columns=["number_of_employees_at_the_beginning_of_the_period", "number_of_employees_at_the_end_of_the_period", "calculated_value"])

            # إعادة تعيين الفهرس ليبدأ من 1
            df.index = df.index + 1

            # تعديل اسم العمود من 'month' إلى 'التاريخ'
            df.rename(columns={'month': 'التاريخ', 'calculated_value_with_percent': 'النتيجة'}, inplace=True)

            # عرض البيانات في جدول
            st.write("### البيانات المحدثة:")
            st.dataframe(df)

            st.divider()
            st.subheader("📊 اختر نوع الرسوم البيانية لعرض البيانات:")

            # إضافة مفتاح فريد للـ multiselect
            chart_types = st.multiselect(
                "أنواع الرسوم:",
                ["📊 Bar Chart", "📈 Line Chart", "💥 Scatter Chart"],
                default=["📊 Bar Chart"],
                key="chart_types_retention"  # مفتاح فريد لهذا العنصر
            )

            # البيانات التي تظهر عند التمرير فوق العناصر
            hover_data = {
                "التاريخ": True,
                "النتيجة": True,
                "عدد الموظفين في بداية الفترة": True,
                "عدد الموظفين في نهاية الفترة": True,
                "الحالة": False  # الحالة لا تحتاج لإظهارها في hover_data
            }

            # إضافة الرسوم البيانية بناءً على الاختيارات
            if "📊 Bar Chart" in chart_types:
                st.write("### 📊 Bar Chart")
                fig = px.bar(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Bar Chart"
                )
                st.plotly_chart(fig)

            if "📈 Line Chart" in chart_types:
                st.write("### 📈 Line Chart")
                fig = px.line(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    markers=True,
                    title="Line Chart"
                )
                st.plotly_chart(fig)

            if "💥 Scatter Chart" in chart_types:
                st.write("### 💥 Scatter Chart")
                fig = px.scatter(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Scatter Chart"
                )
                st.plotly_chart(fig)

        else:
            st.warning("❗ لا توجد بيانات في الفترة المحددة.")
    else:
        st.error(f"خطأ في الاتصال بالسيرفر: {response.status_code}")

except Exception as e:
    st.error(f"حدث خطأ أثناء جلب البيانات: {e}")


    
st.divider()




# ──────────────────────────────
# 🏢  Employee Engament Rate
# ──────────────────────────────
st.subheader("🔄️🧑🏻‍💼معدل مشاركة الموظفين")
st.markdown(
    """
هذا مؤشر السلوك الرئيسي (KBI) يقيس معدل التفاعل الوظيفي للموظفين، والذي يتم تحديده من خلال نتائج استبيان تكامل الموظفين الذي يتم إجراؤه خلال فترة معينة. يعكس هذا المؤشر مستوى مشاركة الموظفين ورضاهم وارتباطهم العاطفي بالمؤسسة.    """
)


col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("تاريخ البداية", value=datetime(current_year, 1, 1), key="start_date_engagement")
with col2:
    end_date = st.date_input("تاريخ النهاية", value=datetime(current_year, 12, 31), key="end_date_engagement")

# رابط الـ API الخاص بمعدل التفاعل الوظيفي
employee_engagement_api_url = f"http://localhost:5000/api/employee_engagement_rate/average_by_date/?start_date={start_date}&end_date={end_date}"

try:
    # طلب البيانات من الـ API
    response = requests.get(employee_engagement_api_url)

    if response.status_code == 200:
        data = response.json()

        if data:
            df = pd.DataFrame(data)

            # تحويل تواريخ البداية والنهاية إلى التنسيق المناسب
            df["from"] = pd.to_datetime(df["from"]).dt.strftime('%Y-%m-%d')
            df["to"] = pd.to_datetime(df["to"]).dt.strftime('%Y-%m-%d')

            # إضافة النتيجة مع نسبة مئوية (إذا كان ذلك مناسبًا)
            df["النتيجة"] = df["employee_integration_survey"].apply(lambda x: f"{x}%" if pd.notna(x) else "0%")

            # إضافة حالة بناءً على القيمة
            df["الحالة"] = df["employee_integration_survey"].apply(
                lambda x: "معدل طبيعي" if pd.notna(x) and x >= 75 else "تحت الطبيعي"
            )

            # إضافة فحص للتأكد من أن القيمة موجودة وتحويل أي قيم غير صالحة إلى NaN
            df["employee_integration_survey"] = df["employee_integration_survey"].apply(pd.to_numeric, errors='coerce')

            # إضافة عمود اللون بناءً على القيمة
            df["color"] = df["employee_integration_survey"].apply(lambda x: 'blue' if pd.notna(x) and x >= 75 else 'red')

            # إعادة ترتيب الأعمدة
            df = df.rename(columns={"from": "من", "to": "إلى", "employee_integration_survey": "معدل التفاعل الوظيفي"})

            # إعادة تعيين الفهرس ليبدأ من 1
            df.index = df.index + 1

            # عرض البيانات في جدول
            st.write("### البيانات المحدثة:")
            st.dataframe(df)

            st.divider()
            st.subheader("📊 اختر نوع الرسوم البيانية لعرض البيانات:")

            # إضافة مفتاح فريد للـ multiselect
            chart_types = st.multiselect(
                "أنواع الرسوم:",
                ["📊 Bar Chart", "📈 Line Chart", "💥 Scatter Chart"],
                default=["📊 Bar Chart"],
                key="chart_types_engagement"
            )

            # البيانات التي تظهر عند التمرير فوق العناصر
            hover_data = {
                "من": True,
                "إلى": True,
                "معدل التفاعل الوظيفي": True,
                "النتيجة": True,
                "الحالة": False  # الحالة لا تحتاج لإظهارها في hover_data
            }

            # إضافة الرسوم البيانية بناءً على الاختيارات
            if "📊 Bar Chart" in chart_types:
                st.write("### 📊 Bar Chart")
                fig = px.bar(
                    df,
                    x="من",  # تغيير إلى "من"
                    y="معدل التفاعل الوظيفي",  # تغيير إلى "معدل التفاعل الوظيفي"
                    hover_data=hover_data,
                    color=df["color"],  # استخدام العمود الجديد للون
                    title="Bar Chart"
                )
                st.plotly_chart(fig)

            if "📈 Line Chart" in chart_types:
                st.write("### 📈 Line Chart")
                fig = px.line(
                    df,
                    x="من",  # تغيير إلى "من"
                    y="معدل التفاعل الوظيفي",  # تغيير إلى "معدل التفاعل الوظيفي"
                    hover_data=hover_data,
                    markers=True,
                    color=df["color"],  # استخدام العمود الجديد للون
                    title="Line Chart"
                )
                st.plotly_chart(fig)

            if "💥 Scatter Chart" in chart_types:
                st.write("### 💥 Scatter Chart")
                fig = px.scatter(
                    df,
                    x="من",  # تغيير إلى "من"
                    y="معدل التفاعل الوظيفي",  # تغيير إلى "معدل التفاعل الوظيفي"
                    hover_data=hover_data,
                    color=df["color"],  # استخدام العمود الجديد للون
                    title="Scatter Chart"
                )
                st.plotly_chart(fig)

        else:
            st.warning("❗ لا توجد بيانات في الفترة المحددة.")
    else:
        st.error(f"خطأ في الاتصال بالسيرفر: {response.status_code}")

except Exception as e:
    st.error(f"حدث خطأ أثناء جلب البيانات: {e}")

# col1, col2 = st.columns(2)
# with col1:
#     start_date = st.date_input("تاريخ البداية", value=datetime(current_year, 1, 1), key="start_date_engagement")
# with col2:
#     end_date = st.date_input("تاريخ النهاية", value=datetime(current_year, 12, 31), key="end_date_engagement")

# # رابط الـ API الخاص بمعدل التفاعل الوظيفي
# employee_engagement_api_url = f"http://localhost:5000/api/employee_engagement_rate/average_by_date/?start_date={start_date}&end_date={end_date}"

# try:
#     # طلب البيانات من الـ API
#     response = requests.get(employee_engagement_api_url)

#     if response.status_code == 200:
#         data = response.json()

#         if data:
#             df = pd.DataFrame(data)

#             # تحويل تواريخ البداية والنهاية إلى التنسيق المناسب
#             df["from"] = pd.to_datetime(df["from"]).dt.strftime('%Y-%m-%d')
#             df["to"] = pd.to_datetime(df["to"]).dt.strftime('%Y-%m-%d')

#             # إضافة النتيجة مع نسبة مئوية (إذا كان ذلك مناسبًا)
#             df["النتيجة"] = df["employee_integration_survey"].apply(lambda x: f"{x}%" if pd.notna(x) else "0%")

#             # إضافة حالة بناءً على القيمة
#             df["الحالة"] = df["employee_integration_survey"].apply(
#                 lambda x: "معدل طبيعي" if x >= 75 else "تحت الطبيعي"
#             )

#             # إعادة ترتيب الأعمدة
#             df = df.rename(columns={"from": "من", "to": "إلى", "employee_integration_survey": "معدل التفاعل الوظيفي"})

#             # إعادة تعيين الفهرس ليبدأ من 1
#             df.index = df.index + 1

#             # عرض البيانات في جدول
#             st.write("### البيانات المحدثة:")
#             st.dataframe(df)

#             st.divider()
#             st.subheader("📊 اختر نوع الرسوم البيانية لعرض البيانات:")

#             # إضافة مفتاح فريد للـ multiselect
#             chart_types = st.multiselect(
#                 "أنواع الرسوم:",
#                 ["📊 Bar Chart", "📈 Line Chart", "💥 Scatter Chart"],
#                 default=["📊 Bar Chart"],
#                 key="chart_types_engagement"
#             )

#             # البيانات التي تظهر عند التمرير فوق العناصر
#             hover_data = {
#                 "من": True,
#                 "إلى": True,
#                 "معدل التفاعل الوظيفي": True,
#                 "النتيجة": True,
#                 "الحالة": False  # الحالة لا تحتاج لإظهارها في hover_data
#             }

#             # إضافة الرسوم البيانية بناءً على الاختيارات
#             if "📊 Bar Chart" in chart_types:
#                 st.write("### 📊 Bar Chart")
#                 fig = px.bar(
#                     df,
#                     x="من",  # تغيير إلى "من"
#                     y="معدل التفاعل الوظيفي",  # تغيير إلى "معدل التفاعل الوظيفي"
#                     hover_data=hover_data,
#                     color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},

#                     title="Bar Chart"
#                 )
#                 st.plotly_chart(fig)

#             if "📈 Line Chart" in chart_types:
#                 st.write("### 📈 Line Chart")
#                 fig = px.line(
#                     df,
#                     x="من",  # تغيير إلى "من"
#                     y="معدل التفاعل الوظيفي",  # تغيير إلى "معدل التفاعل الوظيفي"
#                     hover_data=hover_data,
#                     markers=True,
#                     color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},

#                     title="Line Chart"
#                 )
#                 st.plotly_chart(fig)

#             if "💥 Scatter Chart" in chart_types:
#                 st.write("### 💥 Scatter Chart")
#                 fig = px.scatter(
#                     df,
#                     x="من",  # تغيير إلى "من"
#                     y="معدل التفاعل الوظيفي",  # تغيير إلى "معدل التفاعل الوظيفي"
#                     hover_data=hover_data,
#                     color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},

#                     title="Scatter Chart"
#                 )
#                 st.plotly_chart(fig)

#         else:
#             st.warning("❗ لا توجد بيانات في الفترة المحددة.")
#     else:
#         st.error(f"خطأ في الاتصال بالسيرفر: {response.status_code}")

# except Exception as e:
#     st.error(f"حدث خطأ أثناء جلب البيانات: {e}")


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
st.subheader("🚶‍♂️📉معدل غياب الموظفين")
st.markdown(
    """
هذا مؤشر السلوك الرئيسي (KBI) يقيس معدل غياب الموظفين، ويتم حسابه كنسبة مئوية لإجمالي أيام غياب الموظفين في شهر معين مقارنةً بإجمالي أيام العمل لجميع الموظفين خلال نفس الشهر. يساعد هذا المؤشر في تقييم مستوى التفاعل الوظيفي للموظفين، رفاهيتهم، واتجاهات الحضور."""
)

col1, col2 = st.columns(2)
with col1:
    start_year = st.selectbox("سنة البداية", years, index=years.index(current_year), key="start_year_absenteeism")
    start_month = st.selectbox("شهر البداية", months, index=0, key="start_month_absenteeism")

with col2:
    end_year = st.selectbox("سنة النهاية", years, index=years.index(current_year), key="end_year_absenteeism")
    end_month = st.selectbox("شهر النهاية", months, index=11, key="end_month_absenteeism")

# رابط الـ API الخاص بمعدل غياب الموظفين
employee_absenteeism_api_url = f"http://localhost:5000/api/employee_absenteeism_rate/average_by_month/?start_year={start_year}&start_month={start_month}&end_year={end_year}&end_month={end_month}"

try:
    # طلب البيانات من الـ API
    response = requests.get(employee_absenteeism_api_url)

    if response.status_code == 200:
        data = response.json()

        if data:
            df = pd.DataFrame(data)

            # تغيير تنسيق التاريخ ليعرض السنة والشهر فقط (بدون اليوم والساعة)
            df["month"] = pd.to_datetime(df["month"], format="%Y-%m").dt.strftime('%Y-%m')

            # إضافة % إلى calculated_value لعرضها بشكل مئوي
            df["calculated_value_with_percent"] = df["calculated_value"].apply(lambda x: f"{x}%" if pd.notna(x) else "0%")

            # تلوين حسب القيم وتغيير كلمة color إلى status
            df["الحالة"] = df["calculated_value"].apply(lambda x: 'معدل طبيعي' if x < 4 else 'تحت الطبيعي')

            # تعديل الأسماء الإنجليزية الطويلة إلى أسماء مختصرة بالعربية
            df["عدد أيام الغياب"] = df["total_number_of_days_absent_per_month"]
            df["عدد الموظفين"] = df["total_number_of_employees"]

            # حذف الأعمدة الأصلية التي تحتوي على الأسماء الطويلة
            df = df.drop(columns=["total_number_of_days_absent_per_month", "total_number_of_employees", "calculated_value"])

            # إعادة تعيين الفهرس ليبدأ من 1
            df.index = df.index + 1

            # تعديل اسم العمود من 'month' إلى 'التاريخ'
            df.rename(columns={'month': 'التاريخ', 'calculated_value_with_percent': 'النتيجة'}, inplace=True)

            # عرض البيانات في جدول
            st.write("### البيانات المحدثة:")
            st.dataframe(df)

            st.divider()
            st.subheader("📊 اختر نوع الرسوم البيانية لعرض البيانات:")

            # إضافة مفتاح فريد للـ multiselect
            chart_types = st.multiselect(
                "أنواع الرسوم:",
                ["📊 Bar Chart", "📈 Line Chart", "💥 Scatter Chart"],
                default=["📊 Bar Chart"],
                key="chart_types_absenteeism"  # مفتاح فريد لهذا العنصر
            )

            # البيانات التي تظهر عند التمرير فوق العناصر
            hover_data = {
                "التاريخ": True,
                "النتيجة": True,
                "عدد أيام الغياب": True,
                "عدد الموظفين": True,
                "الحالة": False  # الحالة لا تحتاج لإظهارها في hover_data
            }

            # إضافة الرسوم البيانية بناءً على الاختيارات
            if "📊 Bar Chart" in chart_types:
                st.write("### 📊 Bar Chart")
                fig = px.bar(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Bar Chart"
                )
                st.plotly_chart(fig)

            if "📈 Line Chart" in chart_types:
                st.write("### 📈 Line Chart")
                fig = px.line(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    markers=True,
                    title="Line Chart"
                )
                st.plotly_chart(fig)

            if "💥 Scatter Chart" in chart_types:
                st.write("### 💥 Scatter Chart")
                fig = px.scatter(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Scatter Chart"
                )
                st.plotly_chart(fig)

        else:
            st.warning("❗ لا توجد بيانات في الفترة المحددة.")
    else:
        st.error(f"خطأ في الاتصال بالسيرفر: {response.status_code}")

except Exception as e:
    st.error(f"حدث خطأ أثناء جلب البيانات: {e}")


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
st.subheader("نسبة تقييم أداء الموظفين")
st.markdown(
    """
ذا مؤشر السلوك الرئيسي (KBI) يقيس نسبة الموظفين الذين تم تقييم أدائهم خلال فترة معينة، ويتم حسابه عن طريق قسمة عدد الموظفين الذين تم تقييمهم على إجمالي عدد الموظفين في تلك الفترة. يساعد هذا المؤشر في تقييم مدى إجراء التقييمات للأداء وتغطيتها عبر القوى العاملة.
"""
)

col1, col2 = st.columns(2)
with col1:
    start_year = st.selectbox("سنة البداية", years, index=years.index(current_year), key="start_year_performance")
    start_month = st.selectbox("شهر البداية", months, index=0, key="start_month_performance")

with col2:
    end_year = st.selectbox("سنة النهاية", years, index=years.index(current_year), key="end_year_performance")
    end_month = st.selectbox("شهر النهاية", months, index=11, key="end_month_performance")

# رابط الـ API الخاص بمعدل تقييم أداء الموظفين
employee_performance_api_url = f"http://localhost:5000/api/employee_performance_evaluation_percentage/average_by_month/?start_year={start_year}&start_month={start_month}&end_year={end_year}&end_month={end_month}"

try:
    # طلب البيانات من الـ API
    response = requests.get(employee_performance_api_url)

    if response.status_code == 200:
        data = response.json()

        if data:
            df = pd.DataFrame(data)

            # تغيير تنسيق التاريخ ليعرض السنة والشهر فقط (بدون اليوم والساعة)
            df["month"] = pd.to_datetime(df["month"], format="%Y-%m").dt.strftime('%Y-%m')

            # إضافة % إلى calculated_value لعرضها بشكل مئوي
            df["calculated_value_with_percent"] = df["calculated_value"].apply(lambda x: f"{x}%" if pd.notna(x) else "0%")

            # تلوين حسب القيم وتغيير كلمة color إلى status
            df["الحالة"] = df["calculated_value"].apply(lambda x: 'معدل طبيعي' if x >= 100 else 'تحت الطبيعي')

            # تعديل الأسماء الإنجليزية الطويلة إلى أسماء مختصرة بالعربية
            df["عدد الموظفين الذين تم تقييمهم"] = df["number_of_employees_evaluated"]
            df["عدد الموظفين الإجمالي"] = df["total_number_of_employees"]

            # حذف الأعمدة الأصلية التي تحتوي على الأسماء الطويلة
            df = df.drop(columns=["number_of_employees_evaluated", "total_number_of_employees", "calculated_value"])

            # إعادة تعيين الفهرس ليبدأ من 1
            df.index = df.index + 1

            # تعديل اسم العمود من 'month' إلى 'التاريخ'
            df.rename(columns={'month': 'التاريخ', 'calculated_value_with_percent': 'النتيجة'}, inplace=True)

            # عرض البيانات في جدول
            st.write("### البيانات المحدثة:")
            st.dataframe(df)

            st.divider()
            st.subheader("📊 اختر نوع الرسوم البيانية لعرض البيانات:")

            # إضافة مفتاح فريد للـ multiselect
            chart_types = st.multiselect(
                "أنواع الرسوم:",
                ["📊 Bar Chart", "📈 Line Chart", "💥 Scatter Chart"],
                default=["📊 Bar Chart"],
                key="chart_types_performance"  # مفتاح فريد لهذا العنصر
            )

            # البيانات التي تظهر عند التمرير فوق العناصر
            hover_data = {
                "التاريخ": True,
                "النتيجة": True,
                "عدد الموظفين الذين تم تقييمهم": True,
                "عدد الموظفين الإجمالي": True,
                "الحالة": False  # الحالة لا تحتاج لإظهارها في hover_data
            }

            # إضافة الرسوم البيانية بناءً على الاختيارات
            if "📊 Bar Chart" in chart_types:
                st.write("### 📊 Bar Chart")
                fig = px.bar(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Bar Chart"
                )
                st.plotly_chart(fig)

            if "📈 Line Chart" in chart_types:
                st.write("### 📈 Line Chart")
                fig = px.line(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    markers=True,
                    title="Line Chart"
                )
                st.plotly_chart(fig)

            if "💥 Scatter Chart" in chart_types:
                st.write("### 💥 Scatter Chart")
                fig = px.scatter(
                    df,
                    x="التاريخ",  # تغيير إلى 'التاريخ'
                    y="النتيجة",  # تغيير إلى 'النتيجة'
                    color="الحالة",  # تغيير إلى الحالة بدلاً من color
                    hover_data=hover_data,
                    color_discrete_map={"معدل طبيعي": "blue", "تحت الطبيعي": "red"},
                    title="Scatter Chart"
                )
                st.plotly_chart(fig)

        else:
            st.warning("❗ لا توجد بيانات في الفترة المحددة.")
    else:
        st.error(f"خطأ في الاتصال بالسيرفر: {response.status_code}")

except Exception as e:
    st.error(f"حدث خطأ أثناء جلب البيانات: {e}")
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