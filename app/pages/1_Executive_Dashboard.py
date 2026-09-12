from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]
flights = pd.read_csv(BASE_DIR / "dashboard" / "flights_clean.csv")

st.title("📊 Executive Dashboard")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Flights", f"{len(flights):,}")
c2.metric("OTP", f"{((flights.dep_delay<=15).mean()*100):.1f}%")
c3.metric("Dep Delay", f"{flights.dep_delay.mean():.1f} min")
c4.metric("Arr Delay", f"{flights.arr_delay.mean():.1f} min")

monthly = (
    flights.groupby("month",as_index=False)
    .agg(delay=("dep_delay","mean"))
)

fig = px.line(
    monthly,
    x="month",
    y="delay",
    markers=True,
    title="Monthly Departure Delay"
)

st.plotly_chart(fig, use_container_width=True)