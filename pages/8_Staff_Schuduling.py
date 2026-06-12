import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Staff Scheduling",
    page_icon="👨‍⚕️",
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
<h1 style="color:white;">👨‍⚕️ Smart Staff Scheduling System</h1>
<p style="color:#cbd5e1;">
AI Powered Workforce Management & Shift Monitoring
</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# SAMPLE DATA
# =====================================

staff_data = pd.DataFrame({
    "Staff ID":[
        "DOC101","DOC102","DOC103",
        "NUR201","NUR202","NUR203",
        "DOC104","NUR204"
    ],

    "Name":[
        "Dr. Sharma",
        "Dr. Rao",
        "Dr. Kumar",
        "Nurse Priya",
        "Nurse Anjali",
        "Nurse Meena",
        "Dr. Reddy",
        "Nurse Kavya"
    ],

    "Role":[
        "Doctor",
        "Doctor",
        "Doctor",
        "Nurse",
        "Nurse",
        "Nurse",
        "Doctor",
        "Nurse"
    ],

    "Shift":[
        "Morning",
        "Evening",
        "Night",
        "Morning",
        "Evening",
        "Night",
        "Morning",
        "Night"
    ],

    "Status":[
        "Available",
        "Available",
        "Busy",
        "Available",
        "Busy",
        "Available",
        "Available",
        "Busy"
    ]
})

# =====================================
# KPI CARDS
# =====================================

total_staff = len(staff_data)

doctors = len(
    staff_data[staff_data["Role"]=="Doctor"]
)

nurses = len(
    staff_data[staff_data["Role"]=="Nurse"]
)

available = len(
    staff_data[staff_data["Status"]=="Available"]
)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("👨‍⚕️ Total Staff", total_staff)

with c2:
    st.metric("🩺 Doctors", doctors)

with c3:
    st.metric("👩‍⚕️ Nurses", nurses)

with c4:
    st.metric("✅ Available", available)

st.markdown("---")

# =====================================
# SHIFT DISTRIBUTION
# =====================================

st.subheader("📊 Shift Distribution")

fig = px.pie(
    staff_data,
    names="Shift",
    title="Staff Shift Allocation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# STAFF TABLE
# =====================================

st.subheader("📋 Staff Schedule")

st.dataframe(
    staff_data,
    use_container_width=True
)

# =====================================
# SEARCH STAFF
# =====================================

st.subheader("🔍 Search Staff")

search = st.text_input(
    "Enter Staff Name"
)

if search:

    result = staff_data[
        staff_data["Name"]
        .str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )

# =====================================
# SHIFT SUMMARY
# =====================================

st.subheader("⏰ Shift Summary")

morning = len(
    staff_data[staff_data["Shift"]=="Morning"]
)

evening = len(
    staff_data[staff_data["Shift"]=="Evening"]
)

night = len(
    staff_data[staff_data["Shift"]=="Night"]
)

a,b,c = st.columns(3)

with a:
    st.info(f"🌅 Morning Shift: {morning}")

with b:
    st.warning(f"🌇 Evening Shift: {evening}")

with c:
    st.error(f"🌙 Night Shift: {night}")

# =====================================
# AI INSIGHTS
# =====================================

st.subheader("🤖 AI Workforce Insights")

if night < 2:
    st.warning(
        "Night shift staffing is low. Consider assigning additional staff."
    )
else:
    st.success(
        "Staff distribution looks balanced."
    )

# =====================================
# REPORT DOWNLOAD
# =====================================

report = f"""
Hospital Staff Report

Total Staff: {total_staff}
Doctors: {doctors}
Nurses: {nurses}
Available Staff: {available}

Morning Shift: {morning}
Evening Shift: {evening}
Night Shift: {night}
"""

st.download_button(
    "📄 Download Staff Report",
    report,
    file_name="staff_report.txt"
)