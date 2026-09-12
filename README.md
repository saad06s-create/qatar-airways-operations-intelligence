# ✈️ Aviation Operations Intelligence Platform

### Qatar Airways–Inspired Airline Analytics System

An end-to-end aviation analytics platform built with **Python, SQL, Streamlit, Plotly and Machine Learning**. The application analyses **336,000+ public flight records** to monitor operational performance, airport reliability, network efficiency and departure delay risk.

---

## Application Preview

### Executive Dashboard

![Executive Dashboard](figures/dashboard.png)

> Add the remaining screenshots later using:
>
> - `figures/home.png`
> - `figures/network.png`
> - `figures/predictor.png`

---

## Key Features

- 📊 Executive KPI Dashboard
- 🌍 Interactive Global Airport Network
- 🏙 Airport Performance Analytics
- 🤖 Flight Delay Prediction
- 🗃 SQL & SQLite Data Pipeline
- 📈 Interactive Plotly Visualisations
- 💻 Multi-page Streamlit Web Application

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Data analysis & engineering |
| Pandas | Data cleaning |
| SQL | Operational analytics |
| SQLite | Relational database |
| Plotly | Interactive dashboards |
| Streamlit | Web application |
| Scikit-learn | Machine learning |
| Git & GitHub | Version control |

---

## Business Questions Answered

- Which airports experience the highest departure delays?
- How does on-time performance change throughout the year?
- Which airports handle the greatest flight volume?
- What operational KPIs matter most for airline management?
- Can departure delays be predicted before take-off?

---

## Machine Learning

A **Random Forest Classifier** predicts whether a flight is likely to depart more than **15 minutes late** using operational variables:

- Month
- Day
- Distance
- Air Time

The prediction model is integrated into the Streamlit application through an interactive delay prediction page.

---

## Project Architecture

```text
Public Flight Data
        │
        ▼
Python ETL (Pandas)
        │
        ▼
SQLite Database
        │
        ▼
SQL Analytics
        │
        ▼
Plotly Visualisations
        │
        ▼
Multi-page Streamlit Dashboard
```

---

## Repository Structure

```text
aviation-operations-intelligence/

├── app/
│   ├── app.py
│   └── pages/
│       ├── 1_Executive_Dashboard.py
│       ├── 2_Network_Map.py
│       ├── 3_Airport_Analytics.py
│       └── 4_Delay_Predictor.py
│
├── dashboard/
├── data/
├── figures/
├── notebook/
├── sql/
└── README.md
```

---

## Skills Demonstrated

- Data Engineering
- SQL & Database Design
- Business Intelligence
- Geospatial Analytics
- Machine Learning
- Interactive Dashboard Development
- Version Control with Git

---

## Author

**Saad**

BSc Mathematics • Aspiring Data Analyst • Aviation Analytics
