import streamlit as st
import pandas as pd
import os

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="GreenTrack AI",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------

st.title("🌱 GreenTrack AI")
st.subheader("AI-Powered Sustainability & Carbon Emissions Tracker")

st.divider()

# -----------------------------------
# Sidebar Inputs
# -----------------------------------

st.sidebar.header("Enter Usage Details")

electricity = st.sidebar.number_input(
    "Monthly Electricity Usage (kWh)",
    min_value=0,
    value=250
)

travel = st.sidebar.number_input(
    "Monthly Vehicle Travel (km)",
    min_value=0,
    value=300
)

analyze = st.sidebar.button("Analyze")

# -----------------------------------
# CSV Upload
# -----------------------------------

st.sidebar.subheader("📂 Upload Data")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:
    uploaded_data = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data")

    st.dataframe(uploaded_data)

# -----------------------------------
# Analysis
# -----------------------------------

if analyze:

    electricity_emission = electricity * 0.82
    travel_emission = travel * 0.12

    total_emission = (
        electricity_emission +
        travel_emission
    )

    # Eco Score

    if total_emission < 150:
        score = "🟢 GREEN"
        recommendation = """
Excellent sustainability performance.

• Continue current habits
• Monitor usage monthly
• Consider renewable energy
"""
    elif total_emission < 300:
        score = "🟡 YELLOW"
        recommendation = """
Moderate environmental impact.

• Reduce unnecessary electricity usage
• Switch off idle appliances
• Optimize travel routes
"""
    else:
        score = "🔴 RED"
        recommendation = """
High carbon footprint.

• Reduce power consumption
• Use public transport
• Consider solar energy solutions
"""

    # -----------------------------
    # Report
    # -----------------------------

    st.subheader("📊 Carbon Emission Report")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Electricity CO₂",
        f"{electricity_emission:.1f} kg"
    )

    col2.metric(
        "Travel CO₂",
        f"{travel_emission:.1f} kg"
    )

    col3.metric(
        "Total CO₂",
        f"{total_emission:.1f} kg"
    )

    # -----------------------------
    # Emissions Chart
    # -----------------------------

    st.subheader("📈 Emissions Breakdown")

    chart_data = pd.DataFrame({
        "Source": ["Electricity", "Travel"],
        "CO2": [
            electricity_emission,
            travel_emission
        ]
    })

    st.bar_chart(
        chart_data.set_index("Source")
    )

    # -----------------------------
    # Eco Score
    # -----------------------------

    st.subheader("🌿 Eco Score")

    st.success(score)

    # -----------------------------
    # AI Recommendations
    # -----------------------------

    st.subheader("🤖 AI Recommendations")

    st.write(recommendation)

    # -----------------------------
    # Historical Trend
    # -----------------------------

    st.subheader("📈 Historical Emission Trend")

    history = pd.DataFrame({
        "Month": [
            "Jun",
            "Jul",
            "Aug",
            "Sep"
        ],
        "CO2": [
            total_emission + 40,
            total_emission + 25,
            total_emission + 10,
            total_emission
        ]
    })

    st.line_chart(
        history.set_index("Month")
    )

    # -----------------------------
    # Sustainability Chatbot
    # -----------------------------

    st.subheader("🤖 Sustainability Assistant")

    question = st.text_input(
        "Ask GreenTrack AI"
    )

    if question:

        q = question.lower()

        if "electricity" in q:

            st.success(
                "Use LED lighting, energy-efficient appliances and switch off unused devices."
            )

        elif "travel" in q:

            st.success(
                "Reduce vehicle usage, use public transport and plan optimized routes."
            )

        elif "carbon" in q:

            st.success(
                "Lower electricity consumption and adopt sustainable transportation methods."
            )

        else:

            st.success(
                "Track usage regularly and make small sustainability improvements every month."
            )

    # -----------------------------
    # Future Roadmap
    # -----------------------------

    st.subheader("🚀 Future Roadmap")

    st.markdown("""
- Smart Meter Integration
- Real-Time Energy Monitoring
- IoT Device Connectivity
- AI-Based Energy Forecasting
- Sustainability Dashboard
- Carbon Reduction Insights
- Personalized Sustainability Goals
- Renewable Energy Suggestions
""")

else:

    st.info("Enter values and click Analyze.")