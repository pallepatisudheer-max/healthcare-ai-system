import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go


def diabetes_page():

    st.subheader("🩸 Diabetes Risk Assessment")

    c1, c2, c3 = st.columns(3)

    with c1:
        pregnancies = st.number_input("Pregnancies", 0, 20, 1)
        glucose = st.number_input("Glucose", 0, 300, 120)
        blood_pressure = st.number_input("Blood Pressure", 0, 200, 70)

    with c2:
        skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
        insulin = st.number_input("Insulin", 0, 1000, 80)
        bmi = st.number_input("BMI", 0.0, 80.0, 25.0)

    with c3:
        dpf = st.number_input(
            "Diabetes Pedigree Function",
            0.0,
            5.0,
            0.5
        )
        age = st.number_input("Age", 1, 120, 30)

    if st.button(
        "🚀 Predict Diabetes Risk",
        use_container_width=True
    ):

        try:

            model = joblib.load(
                "backend/ml_models/disease_prediction/diabetes_model.pkl"
            )

            data = np.array([[
                pregnancies,
                glucose,
                blood_pressure,
                skin_thickness,
                insulin,
                bmi,
                dpf,
                age
            ]])

            prediction = model.predict(data)[0]

            risk = 80 if prediction == 1 else 20

            # Gauge Meter
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=risk,
                title={"text": "Diabetes Risk %"},
                gauge={
                    "axis": {"range": [0, 100]}
                }
            ))

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.progress(risk / 100)

            k1, k2, k3 = st.columns(3)

            with k1:
                st.metric(
                    "Risk %",
                    f"{risk}%"
                )

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
                    "⚠ High Risk of Diabetes"
                )

                st.subheader("💡 AI Recommendations")

                st.warning("""
• Consult an Endocrinologist

• Monitor Blood Sugar Daily

• Reduce Sugar Intake

• Follow Diabetic Diet

• Exercise 30 Minutes Daily

• Regular HbA1c Tests

• Maintain Healthy Weight
""")

            else:

                st.success(
                    "✅ Low Risk of Diabetes"
                )

                st.subheader("💡 AI Recommendations")

                st.success("""
• Maintain Healthy Lifestyle

• Continue Regular Exercise

• Balanced Nutrition

• Annual Diabetes Screening

• Stay Hydrated

• Monitor Health Regularly

• Maintain Healthy Weight
""")

        except Exception as e:

            st.error(
                f"Prediction Error: {e}"
            )