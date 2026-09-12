
import streamlit as st

st.set_page_config(page_title="Delay Predictor", layout="centered")

st.title("🤖 Flight Delay Predictor")

month = st.slider("Month", 1, 12, 6)
distance = st.slider("Distance (miles)", 100, 3000, 1000)
air_time = st.slider("Air Time (minutes)", 30, 500, 180)

# Simple demo probability
probability = min(
    95,
    max(
        5,
        int(15 + month*2 + distance/80 + air_time/20)
    )
)

st.metric("Predicted Delay Probability", f"{probability}%")

if probability > 70:
    st.error("High Risk of Delay")
elif probability > 45:
    st.warning("Moderate Risk")
else:
    st.success("Low Risk")