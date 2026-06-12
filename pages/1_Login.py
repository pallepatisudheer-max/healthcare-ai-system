import streamlit as st

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🏥",
    layout="wide"
)

# ==================================
# CSS
# ==================================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #0f172a
    );
}

/* TITLE */

.title{
    text-align:center;
    color:white;
    font-size:52px;
    font-weight:800;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:25px;
}

/* KPI */

.kpi{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    border:1px solid rgba(255,255,255,0.1);
}

.kpi h1{
    margin:0;
}

.kpi p{
    margin:0;
}

/* FEATURE */

.feature{
    background:rgba(255,255,255,0.08);
    padding:18px;
    border-radius:15px;
    color:white;
    margin-bottom:15px;
    border:1px solid rgba(255,255,255,0.1);
}

/* LOGIN CARD */

.login-card{
    background:rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.15);
}

/* BUTTON */

.stButton > button{
    width:100%;
    height:50px;
    font-size:18px;
    border-radius:12px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# HEADER
# ==================================

st.markdown("""
<div class="title">
🏥 AI Healthcare System
</div>

<div class="subtitle">
Healthcare Prediction & Resource Management Platform
</div>
""", unsafe_allow_html=True)

# ==================================
# KPI SECTION
# ==================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="kpi">
    <h1>55K+</h1>
    <p>Patients</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="kpi">
    <h1>450+</h1>
    <p>Doctors</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="kpi">
    <h1>120+</h1>
    <p>Hospitals</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="kpi">
    <h1>98%</h1>
    <p>AI Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==================================
# MAIN AREA
# ==================================

left,right = st.columns([1.4,1])

# ==================================
# FEATURES
# ==================================

with left:

    st.markdown("""
    <div class="feature">
    <h3>🤖 AI Disease Prediction</h3>
    Predict Diabetes, Heart Disease and Kidney Disease using Machine Learning.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature">
    <h3>📊 Smart Analytics Dashboard</h3>
    Visualize healthcare trends and patient insights.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature">
    <h3>🛏️ Bed & Resource Management</h3>
    Monitor bed occupancy and hospital resources.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature">
    <h3>👨‍⚕️ Doctor & Patient Management</h3>
    Manage appointments, schedules and records.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature">
    <h3>💬 AI Healthcare Assistant</h3>
    Intelligent chatbot support for patients and doctors.
    </div>
    """, unsafe_allow_html=True)

# ==================================
# LOGIN
# ==================================

with right:

    
    st.subheader("🔐 Secure Login")

    role = st.selectbox(
        "Select Role",
        ["Patient","Doctor","Admin"]
    )

    username = st.text_input(
        "Username",
        placeholder="Enter Username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter Password"
    )

    st.checkbox("Remember Me")

    if st.button("🚀 Login"):

        if role == "Admin":

            st.success("Welcome Admin")
            st.switch_page("pages/9_Analytics_Dashboard.py")

        elif role == "Doctor":

            st.success("Welcome Doctor")
            st.switch_page("pages/3_Doctor_Management.py")

        elif role == "Patient":

            st.success("Welcome Patient")
            st.switch_page("pages/2_patient_Management.py")

    st.markdown("""
    <br>
    <center>
    Demo Role-Based Authentication
    </center>
    """, unsafe_allow_html=True)

    
# ==================================
# FOOTER
# ==================================



st.markdown("""
<center style="color:#94a3b8;">
© 2026 AI-Powered Healthcare Prediction & Resource Management System
</center>
""", unsafe_allow_html=True)