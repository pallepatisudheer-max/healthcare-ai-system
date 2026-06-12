import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Patient Management",
    page_icon="👨‍⚕️",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("datasets/patients.csv")

st.title("👨‍⚕️ Patient Management")

# KPI CARDS
c1,c2,c3 = st.columns(3)

with c1:
    st.metric(
        "Total Patients",
        len(df)
    )

with c2:
    st.metric(
        "Average Age",
        round(df["age"].mean(),1)
    )

with c3:
    st.metric(
        "Average Satisfaction",
        round(df["satisfaction"].mean(),1)
    )

st.divider()

# SEARCH

search = st.text_input(
    "🔍 Search Patient"
)

if search:
    filtered = df[
        df["name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]
else:
    filtered = df

st.dataframe(
    filtered,
    use_container_width=True
)

st.divider()

# SERVICE CHART

st.subheader("📊 Service Distribution")

service_counts = (
    df["service"]
    .value_counts()
)

st.bar_chart(service_counts)

# SATISFACTION CHART

st.subheader("😊 Satisfaction Analysis")

st.line_chart(
    df["satisfaction"]
)

st.divider()

# ADD PATIENT

st.subheader("➕ Add New Patient")

with st.form("patient_form"):

    patient_id = st.text_input("Patient ID")

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        0,
        120
    )

    service = st.selectbox(
        "Service",
        [
            "ICU",
            "Emergency",
            "General Medicine",
            "Surgery"
        ]
    )

    submit = st.form_submit_button(
        "Add Patient"
    )

    if submit:

        st.success(
            f"{name} added successfully!"
        )