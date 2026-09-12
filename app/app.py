from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Qatar Airways Operations Intelligence",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

@st.cache_data
def load_data():
    return pd.read_csv(BASE_DIR / "dashboard" / "flights_clean.csv")

flights = load_data()

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.title("✈️ Network Filters")

airport = st.sidebar.selectbox(
    "Origin Airport",
    ["All"] + sorted(flights["origin"].unique().tolist())
)

month = st.sidebar.selectbox(
    "Month",
    ["All"] + sorted(flights["month"].unique().tolist())
)

filtered = flights.copy()

if airport != "All":
    filtered = filtered[filtered["origin"] == airport]

if month != "All":
    filtered = filtered[filtered["month"] == month]

# -----------------------------
# KPI calculations
# -----------------------------
total = len(filtered)
otp = round((filtered["dep_delay"] <= 15).mean() * 100, 1)
avg_dep = round(filtered["dep_delay"].mean(), 1)
avg_arr = round(filtered["arr_delay"].mean(), 1)

# -----------------------------
# Dashboard title
# -----------------------------
st.title("✈️ Qatar Airways Operations Intelligence Platform")
st.markdown("### Executive Flight Operations Dashboard")

# -----------------------------
# KPI Cards
# -----------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Flights", f"{total:,}")
c2.metric("On-Time Performance", f"{otp}%")
c3.metric("Avg Departure Delay", f"{avg_dep} min")
c4.metric("Avg Arrival Delay", f"{avg_arr} min")

st.divider()

# -----------------------------
# Airport Performance
# -----------------------------
airport_summary = (
    filtered
    .groupby("origin", as_index=False)
    .agg(
        average_delay=("dep_delay", "mean"),
        flights=("origin", "count")
    )
)

fig1 = px.bar(
    airport_summary,
    x="origin",
    y="average_delay",
    color="average_delay",
    hover_data=["flights"],
    title="Average Departure Delay by Airport",
    color_continuous_scale="Burg"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Monthly Trend
# -----------------------------
monthly = (
    filtered
    .groupby("month", as_index=False)
    .agg(
        average_delay=("dep_delay", "mean")
    )
)

fig2 = px.line(
    monthly,
    x="month",
    y="average_delay",
    markers=True,
    title="Monthly Average Departure Delay"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Delay Distribution
# -----------------------------
fig3 = px.histogram(
    filtered,
    x="dep_delay",
    nbins=60,
    title="Distribution of Departure Delays",
    color_discrete_sequence=["#6D0F3C"]
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()
st.caption("Built with Python • SQL • Plotly • Streamlit")

import streamlit as st

st.set_page_config(
    page_title="Qatar Airways Operations Intelligence",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Qatar Airways Operations Intelligence Platform")

st.markdown("""
### End-to-End Aviation Analytics Platform

Built using:

- Python
- SQL & SQLite
- Plotly
- Streamlit
- Machine Learning

Use the navigation sidebar to explore the analytics.
""")

st.info("Select a page from the sidebar ←")
import streamlit as st

st.set_page_config(
    page_title="Qatar Airways Operations Intelligence",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
# ✈️ Qatar Airways Operations Intelligence Platform

### End-to-End Aviation Analytics & Network Planning System
""")

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric("Flight Records", "336,776")
c2.metric("Analytics Pages", "4")
c3.metric("Machine Learning", "Random Forest")

st.markdown("""
## Platform Overview

This platform demonstrates an airline operations workflow:

- **Executive Dashboard** — KPIs & operational performance
- **Network Map** — Global airport network
- **Airport Analytics** — Delay and reliability analysis
- **Delay Predictor** — Machine learning risk estimation

Use the **sidebar** to navigate between pages.
""")

st.info("Built with Python • SQL • Plotly • Streamlit")
