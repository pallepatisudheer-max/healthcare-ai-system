import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Appointment Management",
    page_icon="📅",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

patients = pd.read_csv("datasets/patients.csv")
staff = pd.read_csv("datasets/staff.csv")

doctors = staff[staff["role"] == "doctor"]

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
}

.hero{
    padding:25px;
    border-radius:20px;
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    color:white;
    text-align:center;
    margin-bottom:20px;
}

.card{
    background:rgba(255,255,255,0.05);
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
}

.metric{
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
<h1>📅 Appointment Management System</h1>
<h4>Smart Scheduling & Healthcare Coordination</h4>
</div>
""", unsafe_allow_html=True)

# ==========================================
# KPI CARDS
# ==========================================
st.subheader("📈 Appointment Overview")

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric("📅 Today's Appointments", 48, "+12")

with k2:
    st.metric("⏳ Pending", 12, "-2")

with k3:
    st.metric("✅ Completed", 28, "+8")

with k4:
    st.metric("❌ Cancelled", 8, "+1")


st.markdown("---")

# ==========================================
# FILTERS
# ==========================================

st.subheader("🔍 Appointment Filters")

f1,f2,f3 = st.columns(3)

with f1:
    selected_department = st.selectbox(
        "Department",
        ["All"] + list(doctors["service"].unique())
    )

with f2:
    selected_date = st.date_input(
        "Appointment Date",
        value=date.today()
    )

search_all = st.text_input(
    "🔎 Search Patient, Doctor or Department"
)

st.markdown("---")

# ==========================================
# BOOK APPOINTMENT
# ==========================================

st.subheader("📝 Book New Appointment")

with st.form("appointment_form"):

    col1,col2 = st.columns(2)

    with col1:
        patient = st.selectbox(
            "Select Patient",
            patients["name"]
        )

        doctor = st.selectbox(
            "Select Doctor",
            doctors["staff_name"]
        )

    with col2:
        department = st.selectbox(
            "Department",
            doctors["service"].unique()
        )

        appointment_date = st.date_input(
            "Appointment Date",
            min_value=date.today()
        )
        appointment_time = st.selectbox(
    "🕒 Time Slot",
    [
        "09:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM",
        "02:00 PM",
        "03:00 PM",
        "04:00 PM"
    ]
)
    notes = st.text_area(
        "Additional Notes"
    )

    submit = st.form_submit_button(
        "📅 Book Appointment"
    )

    if submit:
        st.success(
            f"Appointment booked successfully for {patient}"
        )

st.markdown("---")

# ==========================================
# ANALYTICS
# ==========================================

st.subheader("📊 Appointment Analytics")

col1,col2 = st.columns(2)

with col1:

    dept_counts = doctors["service"].value_counts()

    fig1 = px.pie(
        values=dept_counts.values,
        names=dept_counts.index,
        hole=0.5,
        title="Department Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = px.bar(
        x=dept_counts.index,
        y=dept_counts.values,
        title="Doctors Per Department"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

# ==========================================
# UPCOMING APPOINTMENTS
# ==========================================

st.subheader("📋 Upcoming Appointments")

appointment_df = pd.DataFrame({
    "Patient": patients["name"].head(10),
    "Doctor": doctors["staff_name"].sample(
        n=10,
        replace=True,
        random_state=42
    ).values,
    "Department": doctors["service"].sample(
        n=10,
        replace=True,
        random_state=42
    ).values
})

st.dataframe(
    appointment_df,
    use_container_width=True,
    height=350
)

st.markdown("---")

# ==========================================
# QUICK ACTIONS
# ==========================================

st.subheader("⚡ Quick Actions")

a1,a2,a3,a4 = st.columns(4)

with a1:
    st.button(
        "➕ New Appointment",
        use_container_width=True
    )

with a2:
    st.button(
        "📄 Generate Report",
        use_container_width=True
    )

with a3:
    st.button(
        "📥 Export Data",
        use_container_width=True
    )

with a4:
    st.button(
        "📧 Send Reminder",
        use_container_width=True
    )

st.markdown("---")

# ==========================================
# RECENT ACTIVITY
# ==========================================

st.subheader("🔔 Recent Activity")

st.success("Appointment booked for Richard Rodriguez")
st.info("Doctor assigned successfully")
st.warning("2 appointments awaiting confirmation")
st.success("Reminder notifications sent")

st.markdown("---")
st.subheader("🕒 Today's Schedule")

timeline_df = pd.DataFrame({
    "Time": [
        "09:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM"
    ],
    "Patient": [
        "Richard Rodriguez",
        "Julia Torres",
        "William Herrera",
        "Ashley Walker"
    ],
    "Doctor": [
        "Dr. James",
        "Dr. Crystal",
        "Dr. Daniel",
        "Dr. Rebecca"
    ]
})

st.dataframe(
    timeline_df,
    use_container_width=True
)
st.success("✅ Appointment Management System Active")


st.subheader("🧠 AI Scheduling Insights")

st.success(
    "Peak booking hours detected between 10 AM and 12 PM"
)

st.info(
    "Cardiology remains the most requested department."
)

st.warning(
    "Doctor utilization exceeded 90% today."
)