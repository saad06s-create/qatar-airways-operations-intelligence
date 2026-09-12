
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Airport Analytics", layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]
flights = pd.read_csv(BASE_DIR / "dashboard" / "flights_clean.csv")

st.title("🏙 Airport Analytics")

airport = (
    flights
    .groupby("origin", as_index=False)
    .agg(
        average_delay=("dep_delay","mean"),
        flights=("origin","count")
    )
    .sort_values("average_delay", ascending=False)
)

fig = px.bar(
    airport,
    x="origin",
    y="average_delay",
    color="average_delay",
    hover_data=["flights"],
    title="Average Departure Delay by Airport"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(airport)