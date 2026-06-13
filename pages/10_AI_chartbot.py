import streamlit as st
from datetime import datetime
from google import genai

from config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Healthcare Chatbot",
    page_icon="🤖",
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
<h1 style="color:white;">
🤖 AI Healthcare Assistant
</h1>
<p style="color:#cbd5e1;">
24/7 Smart Medical Information Assistant
</p>
</div>
""", unsafe_allow_html=True)
st.success(
    "🧠 Powered by Google Gemini 2.5 Flash AI"
)

# =====================================
# KPI CARDS
# =====================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Responses", "10K+")

with c2:
    st.metric("Accuracy", "97%")

with c3:
    st.metric("Availability", "24/7")

with c4:
    st.metric("AI Version", "v1.0")

st.markdown("---")
st.subheader("📊 AI Assistant Performance")

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "Questions Today",
        "1,245"
    )

with p2:
    st.metric(
        "Response Accuracy",
        "97%"
    )

with p3:
    st.metric(
        "Avg Response Time",
        "0.8s"
    )

with p4:
    st.metric(
        "Active Users",
        "342"
    )

st.markdown("---")

# =====================================
# SESSION STATE
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# QUICK QUESTIONS
# =====================================

st.subheader("🔥 Popular Healthcare Topics")

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.info("🩸 Diabetes")

with t2:
    st.info("❤️ Heart Health")

with t3:
    st.info("🩺 Kidney Care")

with t4:
    st.info("🥗 Nutrition")

st.markdown("---")
# =====================================
# CHAT INPUT
# =====================================

user_input = st.chat_input(
    "Ask your healthcare question..."
)

if "quick_question" in st.session_state:
    user_input = st.session_state.quick_question
    del st.session_state.quick_question

# =====================================
# SIMPLE AI RESPONSES
# =====================================

def generate_response(question):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )
        return response.text

    except Exception as e:
        return str(e)
    
# =====================================
# CHAT HISTORY
# =====================================

if user_input:

    with st.spinner("🤖 AI is thinking..."):
        response = generate_response(user_input)

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input,
            "time":datetime.now().strftime("%H:%M")
        }
    )

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response,
            "time":datetime.now().strftime("%H:%M")
        }
    )

# =====================================
# DISPLAY CHAT
# =====================================
st.subheader("📈 Chat Analytics")

a1, a2, a3 = st.columns(3)

with a1:
    st.metric(
        "Today's Chats",
        "278"
    )

with a2:
    st.metric(
        "Resolved Queries",
        "96%"
    )

with a3:
    st.metric(
        "Satisfaction",
        "4.8/5"
    )

st.markdown("---")


st.subheader("💬 Chat Conversation")

for msg in st.session_state.messages:

    if msg["role"] == "user":

        with st.chat_message("user"):
            st.write(msg["content"])

    else:

        with st.chat_message("assistant"):
            st.write(msg["content"])

st.subheader("💡 Daily Health Tips")

tips = [
    "Drink at least 2-3 liters of water daily.",
    "Exercise for 30 minutes every day.",
    "Maintain regular sleep patterns.",
    "Monitor blood pressure regularly.",
    "Reduce sugar and processed food intake."
]

for tip in tips:
    st.success(tip)

st.markdown("---")

# =====================================
# AI INSIGHTS
# =====================================

st.markdown("---")

st.subheader("🤖 AI Capabilities")

st.success("""
✔ Disease Information

✔ Health Guidance

✔ Diet Recommendations

✔ Exercise Suggestions

✔ Lifestyle Advice

✔ 24/7 Availability
""")

# =====================================
# DISCLAIMER
# =====================================

st.warning("""
⚠️ This chatbot provides educational information only.
Always consult a qualified healthcare professional
for diagnosis and treatment.
""")

st.markdown("---")

st.caption(
    "🤖 AI Healthcare Assistant | Educational Purposes Only | Version 1.0"
)