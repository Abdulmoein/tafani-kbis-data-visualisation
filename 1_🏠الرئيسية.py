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
    st.image("assets/tafani-logo.png", width=120)


with col_title:
    
    st.title("Tafani • (KBIS) 📈")
    st.markdown(
        """
    تم تطوير هذا التطبيق لقياس أداء **شركة التفاني للإتصالات والتقنية**،
    من خلال تطبيق مؤشرات السلوك الرئيسية على جميع القطاعات والدوائر.
    يوفر المشروع رؤى فورية قائمة على البيانات، مما يدعم اتخاذ قرارات أسرع وأكثر كفاءة, 
    **ويساهم بفاعلية في تعزيز وضوح الرؤية الإستراتيجية للشركة.** 📊✨
        """
    )
    st.markdown(
        "<div class='highlight-box'>🎯💪 التفاني تحول حقيقي</div>",
        unsafe_allow_html=True,
    )

    

st.divider()

# ──────────────────────────────
# 🏢 About us
# ──────────────────────────────
st.subheader("من نحن؟! 🏢")
st.markdown(
    """
**شركة التفاني**

هي شركة رائدة في مجال التكنولوجيا المالية (**FinTech**)، متخصصة في التحول الرقمي وتطوير الأعمال، بخبرة تمتد منذ عام 2012.

🎯 **هدفنا :** نحو محيط تقني ذكي.

🚀 **مهمتنا:** تكييف التكنولوجيا الخدمية وتيسيرها لمنفعة المجتمع.

🌟 **قيمنا:**
- 💪 **التفاني**
- 🤝🏻 **الوفاء**
- 💯 **النزاهة**
- 💡 **الابتكار**
- 🎯 **الجرأة**
- 🤝 **التشارك**
    """
)

st.divider()

# ──────────────────────────────
# 🚀 KBIS at a glance
# ──────────────────────────────
st.subheader("ماهي (kbis)؟")

st.markdown(
    """
**نظام مؤشرات السلوك الرئيسية (KBIS)** هو إطار العمل الشامل في شركتنا لتحديد وتتبع والتفاعل مع السلوكيات التي تقود النجاح الفعلي للأعمال.  
من خلال دمج البيانات من جميع الأقسام (🧑🏻‍💼 الموارد البشرية، 💸 التجارية، 💻 تكنولوجيا المعلومات، ...)، وتحويلها إلى مقاييس واضحة تعتمد على السلوكيات،  
يحول **KBIS** الأنشطة المتفرقة إلى رؤى قابلة للتنفيذ، مما يعزز القدرة على اتخاذ قرارات استراتيجية مدعومة بالبيانات.

**لماذا يُعتبر KBIS مهمًا — الفوائد الرئيسية**  
- 📏 **قياس الأداء بدقة** — تحديد كيف يتصرف الفرق والأفراد مقارنةً بالأهداف الاستراتيجية.  
- 🧭 **إرشاد القرارات الاستراتيجية والإدارية** — توجيه القيادة للتركيز على السلوكيات التي تحدث فرقًا، وليس فقط على النتائج.  
- ⚡ **تسريع المرونة التشغيلية** — اكتشاف التغيرات الناشئة حتى يتمكن المديرون من التكيف في الوقت الفعلي.  
- 🔄 **تعزيز التحسين المستمر** — توفير حلقة قياس ومتابعة راجعة لكل قسم لتجربة واختبار وتحسين العمليات.  
- 🎯 **مواءمة جميع أقسام المنظمة** — خلق لغة مشتركة حيث تتجه الأهداف والحوافز والإجراءات اليومية في نفس الاتجاه.  
    """
)


st.link_button("الانتقال الى واجهة ادخال البيانات »", "http://localhost:5000/main/en/")

st.divider()


# ──────────────────────────────
# 📬 Contact
# ──────────────────────────────
st.subheader("لأي استفسار؟ تواصل معنا 📬")
contact_cols = st.columns(2)
with contact_cols[0]:
    st.markdown(
        """
        ** 📧الايميل**  
        it@tafani.ly 


        """
    )
with contact_cols[1]:
    st.markdown(
        """
        **📞الهاتاف الأرضي**  
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
            background: #fff;
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