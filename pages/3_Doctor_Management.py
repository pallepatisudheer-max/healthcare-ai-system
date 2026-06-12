import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Doctor Management",
    page_icon="👨‍⚕️",
    layout="wide"
)

# ======================
# CUSTOM CSS
# ======================

st.markdown("""
<style>

.main{
    background:#0f172a;
}

.block-container{
    padding-top:1rem;
}

.metric-card{
    background:rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
}

.title{
    font-size:48px;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ======================
# LOAD DATA
# ======================

df = pd.read_csv("datasets/staff.csv")

# ======================
# HEADER
# ======================

st.markdown("""
<div class='title'>
👨‍⚕️ Doctor Management
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ======================
# KPI CARDS
# ======================

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Total Staff",
        len(df)
    )

with col2:
    doctors = len(df[df["role"]=="doctor"])
    st.metric(
        "Doctors",
        doctors
    )

with col3:
    nurses = len(df[df["role"]=="nurse"])
    st.metric(
        "Nurses",
        nurses
    )

st.markdown("---")

# ======================
# SEARCH
# ======================

search = st.text_input(
    "🔍 Search Staff"
)

filtered = df[
    df["staff_name"]
    .str.contains(search,case=False,na=False)
]

st.dataframe(
    filtered.head(50),
    use_container_width=True
)

st.markdown("---")

# ======================
# ROLE DISTRIBUTION
# ======================

st.subheader("📊 Role Distribution")

role_counts = df["role"].value_counts()

fig = px.pie(
    names=role_counts.index,
    values=role_counts.values,
    hole=0.5,
    title="Staff Roles"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# SERVICE DISTRIBUTION
# ======================

st.subheader("🏥 Service Distribution")

service_counts = df["service"].value_counts()

fig2 = px.bar(
    x=service_counts.index,
    y=service_counts.values,
    title="Department Wise Staff"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ======================
# ADD STAFF
# ======================

st.markdown("---")
st.subheader("➕ Add New Staff")

with st.form("staff_form"):

    sid = st.text_input("Staff ID")

    name = st.text_input("Name")

    role = st.selectbox(
        "Role",
        ["doctor","nurse","nursing_assistant"]
    )

    service = st.selectbox(
        "Service",
        [
            "emergency",
            "ICU",
            "general_medicine",
            "surgery"
        ]
    )

    submit = st.form_submit_button(
        "Add Staff"
    )

    if submit:
        st.success(
            f"{name} added successfully!"
        )

# ======================
# TOP DOCTORS
# ======================

st.markdown("---")

st.subheader("⭐ Doctor Directory")

doctor_df = df[df["role"]=="doctor"]

for _,row in doctor_df.head(8).iterrows():

    st.info(
        f"👨‍⚕️ {row['staff_name']} | {row['service']}"
    )