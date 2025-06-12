# 🌍 CO₂ Emissions Dashboard Project

An interactive data dashboard built with **Python** and **Streamlit** to explore global CO₂ emissions across countries and over time. The project focuses on data cleaning, exploratory data analysis (EDA), and interactive visualizations to gain insights into emission trends.

---

## 📊 Features

- Data cleaning and preprocessing with `pandas`
- Interactive dashboard using `Streamlit`
- Visualizations with `matplotlib` and `plotly`
- Country-level emissions analysis over time
- Top 10 CO₂ emitters chart
- Animated trends by continent
- Choropleth map of CO₂ emissions by country

---

## 🗂️ Project Structure

data-analysis-and-dashboard-with-python/
│
├── data/
│ ├── owid-co2-data.csv
│ ├── owid-co2-codebook.csv
│ └── cleaned_co2.csv
│
├── notebooks/
│ └── eda.ipynb # Exploratory Data Analysis and Data cleaning steps
│
├── app/
│ └── dashboard.py # Streamlit dashboard app
│
└── README.md # Project documentation

---

## 🧹 Data Cleaning

The EDA notebook (`notebooks/eda.ipynb`) includes:

- Removing null and invalid values
- Renaming columns for clarity
- Converting units to float
- Standardizing country names

---

## 🔎 Exploratory Data Analysis (EDA)

- CO₂ emissions over time
- Emissions by continent and country
- Correlation between emissions and population/GDP

---

## 📈 Interactive Dashboard

To launch the dashboard:

```bash
cd app
streamlit run dashboard.py
