
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Network Map", layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]

flights = pd.read_csv(BASE_DIR / "dashboard" / "flights_clean.csv")
airports = pd.read_csv(BASE_DIR / "data" / "airports.csv")

airport_counts = (
    flights
    .groupby("origin", as_index=False)
    .agg(flights=("origin","count"))
)

map_df = airport_counts.merge(
    airports,
    left_on="origin",
    right_on="faa"
)

st.title("🌍 Global Network Map")

fig = px.scatter_geo(
    map_df,
    lat="lat",
    lon="lon",
    size="flights",
    hover_name="name",
    projection="natural earth",
    title="Airport Network by Flight Volume"
)

st.plotly_chart(fig, use_container_width=True)