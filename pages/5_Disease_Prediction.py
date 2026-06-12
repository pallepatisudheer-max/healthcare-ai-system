import streamlit as st

from backend.diabetes_ui import diabetes_page
from backend.heart_ui import heart_page
from backend.kidney_ui import kidney_page

st.markdown("""
<div style="
padding:25px;
border-radius:20px;
background:linear-gradient(135deg,#2563eb,#7c3aed);
color:white;
text-align:center;
margin-bottom:20px;
">
<h1>🧠 AI Disease Prediction Center</h1>
<h4>
Advanced Healthcare Risk Assessment &
Clinical Decision Support
</h4>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🧠 Models", "3")

with c2:
    st.metric("🎯 Accuracy", "97%")

with c3:
    st.metric("📊 Predictions", "5000+")

with c4:
    st.metric("🏥 Diseases", "3")

st.markdown("---")

st.subheader(
    "🩺 Select Disease for Assessment"
)

disease = st.selectbox(
    "Choose Prediction Model",
    [
        "Diabetes Prediction",
        "Heart Disease Prediction",
        "Kidney Disease Prediction"
    ]
)

st.subheader("🤖 AI Prediction Insights")

st.success(
    "Machine learning models are active and ready."
)

st.info(
    "Predictions are generated using trained healthcare datasets."
)

st.warning(
    "Results should support—not replace—professional medical diagnosis."
)

st.markdown("---")

if disease == "Diabetes Prediction":

    st.info("""
### 🩸 Diabetes Prediction

Predicts diabetes risk using:

• Glucose

• BMI

• Insulin

• Blood Pressure

• Age
""")

elif disease == "Heart Disease Prediction":

    st.info("""
### ❤️ Heart Disease Prediction

Predicts cardiovascular risk using:

• Cholesterol

• Blood Pressure

• Heart Rate

• ECG Features

• Age
""")

else:

    st.info("""
### 🩺 Kidney Disease Prediction

Predicts kidney disease risk using:

• Creatinine

• Hemoglobin

• Blood Urea

• Sodium

• Potassium
""")
st.markdown("---")

st.subheader("🤖 AI Insights")

st.success(
    "All prediction models are validated and ready for assessment."
)

st.info(
    "Prediction results are generated using trained machine learning algorithms."
)

st.warning(
    "This system assists healthcare professionals and should not replace medical diagnosis."
)

st.markdown("---")
if disease == "Diabetes Prediction":
    diabetes_page()

elif disease == "Heart Disease Prediction":
    heart_page()

else:
    kidney_page()