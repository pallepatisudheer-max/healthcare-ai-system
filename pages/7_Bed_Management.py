import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Bed Management",
    page_icon="🛏️",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div style="
padding:25px;
border-radius:15px;
background:linear-gradient(135deg,#0f172a,#1e293b);
text-align:center;
margin-bottom:20px;
">
<h1 style="color:white;">🛏️ Smart Bed Management System</h1>
<p style="color:#cbd5e1;">
Real-Time Hospital Bed Monitoring & Resource Allocation
</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SAMPLE DATA
# ==========================================

bed_data = pd.DataFrame({
    "Bed ID":[
        "BED-101","BED-102","BED-103",
        "BED-104","BED-105","BED-106",
        "BED-107","BED-108","BED-109",
        "BED-110"
    ],
    "Type":[
        "General","ICU","General",
        "Emergency","ICU","General",
        "Emergency","ICU","General",
        "General"
    ],
    "Status":[
        "Occupied","Available","Occupied",
        "Available","Occupied","Available",
        "Occupied","Available","Occupied",
        "Available"
    ]
})

# ==========================================
# METRICS
# ==========================================

total_beds = len(bed_data)
occupied = len(
    bed_data[bed_data["Status"]=="Occupied"]
)
available = len(
    bed_data[bed_data["Status"]=="Available"]
)
icu = len(
    bed_data[bed_data["Type"]=="ICU"]
)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("🛏️ Total Beds", total_beds)

with c2:
    st.metric("✅ Available", available)

with c3:
    st.metric("❌ Occupied", occupied)

with c4:
    st.metric("🏥 ICU Beds", icu)

st.markdown("---")

# ==========================================
# OCCUPANCY RATE
# ==========================================

occupancy_rate = round(
    (occupied/total_beds)*100,
    1
)

st.subheader("📊 Bed Occupancy Rate")

st.progress(occupancy_rate/100)

st.metric(
    "Occupancy Rate",
    f"{occupancy_rate}%"
)

# ==========================================
# PIE CHART
# ==========================================

st.subheader("📈 Bed Status Distribution")

fig = px.pie(
    bed_data,
    names="Status",
    title="Hospital Bed Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# BED TABLE
# ==========================================

st.subheader("📋 Bed Information")

st.dataframe(
    bed_data,
    use_container_width=True
)

# ==========================================
# BED SEARCH
# ==========================================

st.subheader("🔍 Search Bed")

search = st.text_input(
    "Enter Bed ID"
)

if search:

    result = bed_data[
        bed_data["Bed ID"]
        .str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )

# ==========================================
# EMERGENCY ALERTS
# ==========================================

st.subheader("🚨 Emergency Status")

if available < 3:

    st.error(
        "Critical Alert: Low Bed Availability!"
    )

else:

    st.success(
        "Sufficient Beds Available"
    )

# ==========================================
# REPORT DOWNLOAD
# ==========================================

report = f"""
Hospital Bed Report

Total Beds: {total_beds}
Available Beds: {available}
Occupied Beds: {occupied}
ICU Beds: {icu}

Occupancy Rate: {occupancy_rate}%
"""

st.download_button(
    "📄 Download Bed Report",
    report,
    file_name="bed_report.txt"
)