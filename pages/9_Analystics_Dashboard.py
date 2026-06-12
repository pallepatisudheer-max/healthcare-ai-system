import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Healthcare Analytics",
    page_icon="📊",
    layout="wide"
)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div style="
padding:25px;
border-radius:15px;
background:linear-gradient(135deg,#0f172a,#1e293b);
text-align:center;
margin-bottom:20px;
">
<h1 style="color:white;">
📊 Healthcare Analytics Dashboard
</h1>
<p style="color:#cbd5e1;">
Real-Time Hospital Performance Monitoring
</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# KPI SECTION
# =====================================

st.subheader("🏥 Hospital Performance Overview")

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric("👨 Patients", "5,240", "+12%")

with k2:
    st.metric("👨‍⚕️ Doctors", "85", "+5")

with k3:
    st.metric("📅 Appointments", "1,245", "+8%")

with k4:
    st.metric("🛏 Occupancy", "82%", "+3%")

with k5:
    st.metric("💰 Revenue", "$32K", "+15%")

st.markdown("---")
f1, f2 = st.columns(2)

with f1:
    st.selectbox(
        "📆 Time Range",
        [
            "Today",
            "This Week",
            "This Month",
            "This Year"
        ]
    )

with f2:
    st.selectbox(
        "🏥 Department",
        [
            "All",
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Emergency"
        ]
    )

st.markdown("---")
# =====================================
# SAMPLE DATA
# =====================================

disease_data = pd.DataFrame({
    "Disease":[
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Hypertension",
        "Asthma"
    ],
    "Patients":[
        1450,
        1120,
        860,
        980,
        830
    ]
})

# =====================================
# CHART 1
# =====================================

col1,col2 = st.columns(2)

with col1:

    st.subheader("🩺 Disease Distribution")

    fig = px.pie(
        disease_data,
        names="Disease",
        values="Patients",
        hole=0.4
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# CHART 2
# =====================================

with col2:

    st.subheader("📈 Patient Statistics")

    fig2 = px.bar(
        disease_data,
        x="Disease",
        y="Patients"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# =====================================
# MONTHLY ADMISSIONS
# =====================================

st.subheader("📅 Monthly Admissions")

monthly = pd.DataFrame({
    "Month":[
        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug",
        "Sep","Oct","Nov","Dec"
    ],
    "Admissions":[
        320,350,390,420,
        450,470,500,520,
        490,510,530,560
    ]
})

fig3 = px.line(
    monthly,
    x="Month",
    y="Admissions",
    markers=True
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =====================================
# BED OCCUPANCY
# =====================================

st.subheader("🛏️ Bed Occupancy")

occupancy = 82

fig4 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=occupancy,
    title={"text":"Hospital Occupancy %"},
    gauge={
        "axis":{"range":[0,100]},
        "bar":{"color":"darkblue"}
    }
))

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =====================================
# AI INSIGHTS
# =====================================

st.subheader("🤖 AI Executive Insights")

st.success(
    "Patient admissions increased by 12% this month."
)

st.info(
    "Cardiology remains the most requested department."
)

st.warning(
    "Bed occupancy may exceed 90% next week."
)

st.success(
    "Revenue trend indicates positive growth."
)

# =====================================
# REVENUE ANALYTICS
# =====================================

st.subheader("💰 Revenue Analytics")

revenue = pd.DataFrame({
    "Month":[
        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug",
        "Sep","Oct","Nov","Dec"
    ],
    "Revenue":[
        12000,15000,17000,18000,
        21000,22000,25000,26000,
        27000,29000,30000,32000
    ]
})

fig5 = px.area(
    revenue,
    x="Month",
    y="Revenue"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)
st.subheader("📋 Executive Summary")

st.success(
    "Hospital performance is improving consistently across all departments."
)

st.info(
    "Patient growth rate increased by 12% compared to last month."
)

st.warning(
    "Bed occupancy may require expansion planning in upcoming months."
)

st.success(
    "Revenue trend indicates strong operational efficiency."
)

st.markdown("---")
# =====================================
# FORECAST
# =====================================

st.subheader("🔮 Forecast")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Expected Patients",
        "6,100"
    )

with c2:
    st.metric(
        "Expected Revenue",
        "$38K"
    )

with c3:
    st.metric(
        "Expected Occupancy",
        "88%"
    )

st.markdown("---")

# =====================================
# DOWNLOAD REPORT
# =====================================

st.subheader("📄 Smart Reports & Downloads")
r1, r2, r3 = st.columns(3)

with r1:
    st.button(
        "📊 Monthly Report",
        use_container_width=True
    )

with r2:
    st.button(
        "💰 Revenue Report",
        use_container_width=True
    )

with r3:
    st.button(
        "🏥 Hospital Summary",
        use_container_width=True
    )
    st.markdown("---")

st.caption(
    "🏥 AI Healthcare Management System | Analytics Module | Version 1.0"
)