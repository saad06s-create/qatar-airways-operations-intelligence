# ✈️ Aviation Operations Intelligence Platform

### Qatar Airways–Inspired Airline Analytics System

An end-to-end aviation analytics platform built using **Python, SQL, Streamlit, Plotly and Machine Learning**. The application analyses **336,000+ public flight records** to monitor operational performance, airport reliability and delay risk through an interactive executive dashboard.

---

## Live Features

- 📊 Executive KPI Dashboard
- 🌍 Interactive Global Airport Network
- 🏙 Airport Performance Analytics
- 🤖 Flight Delay Prediction Tool
- 🗃 SQL-backed Aviation Data Pipeline

---

## Technology Stack

| Tool | Purpose |
|------|---------|
| Python | Data analysis & engineering |
| Pandas | Data cleaning |
| SQL & SQLite | Relational database |
| Plotly | Interactive visualisations |
| Streamlit | Multi-page web application |
| Scikit-learn | Delay prediction model |
| Git & GitHub | Version control |

---

## Project Architecture

data → Python ETL → SQLite Database → Streamlit Dashboard → Interactive Analytics

---

## Business Questions Answered

- Which airports experience the highest departure delays?
- How does on-time performance change throughout the year?
- Which airports handle the greatest flight volume?
- Can departure delays be predicted before take-off?
- How can airline operations be monitored through executive KPIs?

---

## Machine Learning

A Random Forest classifier predicts whether a flight is likely to depart **more than 15 minutes late** using operational variables including:

- Month
- Day
- Distance
- Air Time

The model is presented through an interactive delay prediction page within the Streamlit application.

---

## Repository Structure

```text
app/
pages/
dashboard/
figures/
notebook/
sql/
```

---

## Author

**Saad**  
BSc Mathematics | Data Analytics & Aviation Intelligence