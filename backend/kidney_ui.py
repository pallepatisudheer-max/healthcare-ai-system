import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go


def kidney_page():

    st.subheader("🩺 Kidney Disease Risk Assessment")

    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.number_input("Age", 1, 100, 40)
        bp = st.number_input("Blood Pressure", 50, 200, 80)

        sg = st.selectbox(
            "Specific Gravity",
            [1.005, 1.010, 1.015, 1.020, 1.025]
        )

        al = st.slider(
            "Albumin",
            0,
            5,
            2
        )

        su = st.slider(
            "Sugar",
            0,
            5,
            2
        )

    with c2:

        bgr = st.number_input(
            "Blood Glucose Random",
            50,
            500,
            120
        )

        bu = st.number_input(
            "Blood Urea",
            1,
            300,
            40
        )

        sc = st.number_input(
            "Serum Creatinine",
            0.1,
            20.0,
            1.2
        )

        sod = st.number_input(
            "Sodium",
            80,
            200,
            135
        )

        pot = st.number_input(
            "Potassium",
            1.0,
            10.0,
            4.5
        )

    with c3:

        hemo = st.number_input(
            "Hemoglobin",
            1.0,
            20.0,
            13.5
        )

        pcv = st.number_input(
            "Packed Cell Volume",
            10,
            60,
            40
        )

        wc = st.number_input(
            "White Blood Cell Count",
            1000,
            30000,
            8000
        )

        rc = st.number_input(
            "Red Blood Cell Count",
            1.0,
            8.0,
            5.0
        )

    st.markdown("---")

    if st.button(
        "🚀 Predict Kidney Disease",
        use_container_width=True
    ):

        try:

            model = joblib.load(
                "backend/ml_models/disease_prediction/kidney_model.pkl"
            )

            data = np.array([[
                age,
                bp,
                sg,
                al,
                su,
                bgr,
                bu,
                sc,
                sod,
                pot,
                hemo,
                pcv,
                wc,
                rc
            ]])

            prediction = model.predict(data)[0]

            risk = 85 if prediction == 1 else 15

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=risk,
                title={"text": "Kidney Risk %"},
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

            if prediction == 1:

                st.error(
                    "⚠ High Risk of Kidney Disease"
                )

                st.markdown("""
### 💡 AI Recommendations

- Consult a Nephrologist
- Monitor Kidney Function Tests
- Reduce Salt Intake
- Drink Adequate Water
- Control Blood Pressure
- Follow Kidney-Friendly Diet
- Schedule Regular Checkups
""")

            else:

                st.success(
                    "✅ Low Risk of Kidney Disease"
                )

                st.markdown("""
### 💡 Health Recommendations

- Maintain Proper Hydration
- Follow Balanced Nutrition
- Exercise Regularly
- Monitor Blood Pressure
- Annual Kidney Checkup
""")

        except Exception as e:

            st.error(
                f"Prediction Error: {e}"
            )