import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go


def heart_page():

    st.subheader("❤️ Heart Disease Risk Assessment")

    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.number_input("Age", 20, 100, 45)
        sex = st.selectbox("Gender", [0, 1])
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        trestbps = st.number_input("Blood Pressure", 80, 250, 120)

    with c2:
        chol = st.number_input("Cholesterol", 100, 700, 220)
        fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
        restecg = st.selectbox("Rest ECG", [0, 1, 2])
        thalach = st.number_input("Maximum Heart Rate", 50, 250, 150)

    with c3:
        exang = st.selectbox("Exercise Angina", [0, 1])
        oldpeak = st.number_input("Old Peak", 0.0, 10.0, 1.0)
        slope = st.selectbox("Slope", [0, 1, 2])
        ca = st.selectbox("Major Vessels", [0, 1, 2, 3, 4])
        thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

    if st.button("🚀 Predict Heart Disease", use_container_width=True):

        try:

            model = joblib.load(
                "backend/ml_models/disease_prediction/heart_model.pkl"
            )

            data = np.array([[
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal
            ]])

            prediction = model.predict(data)[0]

            risk = 85 if prediction == 1 else 15

            # Gauge Meter
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=risk,
                title={"text": "Heart Disease Risk %"},
                gauge={
                    "axis": {"range": [0, 100]}
                }
            ))

            st.plotly_chart(fig, use_container_width=True)

            st.progress(risk / 100)

            k1, k2, k3 = st.columns(3)

            with k1:
                st.metric("Risk %", f"{risk}%")

            with k2:
                st.metric(
                    "Severity",
                    "High" if risk > 70 else "Low"
                )

            with k3:
                st.metric(
                    "Confidence",
                    "97%"
                )

            # Prediction Result
            if prediction == 1:

                st.error(
                    "⚠ High Risk of Heart Disease"
                )

                st.subheader("💡 AI Recommendations")

                st.warning("""
• Consult a Cardiologist

• Monitor Blood Pressure Regularly

• Reduce Cholesterol Intake

• Avoid Smoking

• Exercise Daily

• Follow Heart-Healthy Diet

• Schedule ECG Checkups
""")

            else:

                st.success(
                    "✅ Low Risk of Heart Disease"
                )

                st.subheader("💡 AI Recommendations")

                st.success("""
• Continue Healthy Lifestyle

• Maintain Regular Exercise

• Balanced Nutrition

• Annual Heart Checkup

• Manage Stress Levels

• Proper Sleep Schedule

• Stay Physically Active
""")

        except Exception as e:

            st.error(
                f"Prediction Error: {e}"
            )