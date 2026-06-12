import streamlit as st

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🏥",
    layout="wide"
)


st.sidebar.markdown("""
# 🏥 Healthcare AI

### Smart Hospital Platform

---
""")

st.sidebar.markdown("""
### 📊 Core Modules

👨 Patients

👨‍⚕️ Doctors

📅 Appointments

---
""")

st.sidebar.markdown("""
### 🤖 AI Modules

🧠 Disease Prediction

💊 Treatment AI

🤖 AI Assistant

---
""")

st.sidebar.markdown("""
### 🏥 Operations

🛏 Bed Management

👩‍⚕️ Staff Scheduling

📈 Analytics

---
""")
st.markdown("""
<div style="
padding:25px;
border-radius:20px;
background:linear-gradient(135deg,#2563eb,#7c3aed);
color:white;
text-align:center;
margin-bottom:20px;
">
<h1>
🏥 AI-Powered Healthcare Management System
</h1>

<h4>
Healthcare Intelligence, Resource Optimization &
Disease Prediction Platform
</h4>

</div>
""", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👨 Patients",
        "5,240"
    )

with c2:
    st.metric(
        "👨‍⚕️ Doctors",
        "85"
    )

with c3:
    st.metric(
        "📅 Appointments",
        "1,245"
    )

with c4:
    st.metric(
        "🧠 AI Predictions",
        "5,000+"
    )

st.markdown("---")

st.subheader("🚀 Platform Capabilities")

st.success("👨 Patient Management")

st.success("👨‍⚕️ Doctor Management")

st.success("📅 Appointment Scheduling")

st.success("🧠 Disease Prediction")

st.success("💊 Treatment Recommendation")

st.success("🛏 Bed Management")

st.success("👩‍⚕️ Staff Scheduling")

st.success("📈 Healthcare Analytics")

st.success("🤖 AI Healthcare Assistant")

st.subheader("📊 System Status")

s1, s2, s3 = st.columns(3)

with s1:
    st.success(
        "🟢 AI Models Active"
    )

with s2:
    st.success(
        "🟢 Database Connected"
    )

with s3:
    st.success(
        "🟢 System Healthy"
    )

st.markdown("---")

st.caption(
    "🏥 AI Healthcare Management System | Developed by Sudheer | Version 1.0"
)