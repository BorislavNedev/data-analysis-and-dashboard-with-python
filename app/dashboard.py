# ----------------------------------------------
# 🌍 Streamlit CO₂ Emissions Dashboard
# ----------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------
# 1. Load the cleaned dataset
# ----------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("../data/cleaned_co2.csv")

df = load_data()

# ----------------------------------------------
# 2. Sidebar controls
# ----------------------------------------------
st.sidebar.title("🔧 Filters")

years = df['year'].unique()
selected_year = st.sidebar.slider("Select Year", int(df['year'].min()), int(df['year'].max()), int(df['year'].max()))

countries = sorted(df['country'].unique())
selected_country = st.sidebar.selectbox("Select Country", countries, index=countries.index("World") if "World" in countries else 0)

# ----------------------------------------------
# 3. Dashboard Title
# ----------------------------------------------
st.title("🌍 Global CO₂ Emissions Dashboard")
st.caption("Visualizing emissions data across countries and time.")

# ----------------------------------------------
# 4. Global CO₂ Emissions Over Time
# ----------------------------------------------
st.subheader("📈 Global CO₂ Emissions Over Time")
global_trend = df.groupby("year")["co2"].sum()

fig, ax = plt.subplots()
global_trend.plot(ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Total Emissions (Million Tonnes)")
ax.set_title("Global CO₂ Emissions (All Countries Combined)")
st.pyplot(fig)

# ----------------------------------------------
# 5. Top 10 Emitters in Selected Year
# ----------------------------------------------
st.subheader(f"🔥 Top 10 CO₂ Emitters in {selected_year}")
top_emitters = (
    df[df['year'] == selected_year]
    .sort_values('co2', ascending=False)
    .head(10)
)

fig2, ax2 = plt.subplots()
ax2.barh(top_emitters['country'], top_emitters['co2'], color='tomato')
ax2.set_xlabel("CO₂ Emissions (Million Tonnes)")
ax2.set_title(f"Top 10 Emitters in {selected_year}")
ax2.invert_yaxis()
st.pyplot(fig2)

# ----------------------------------------------
# 6. CO₂ Emissions Per Capita
# ----------------------------------------------
st.subheader(f"👣 Top 10 CO₂ Emitters Per Capita in {selected_year}")
top_per_capita = (
    df[df['year'] == selected_year]
    .sort_values('co2_per_capita', ascending=False)
    .head(10)
)

fig3, ax3 = plt.subplots()
ax3.barh(top_per_capita['country'], top_per_capita['co2_per_capita'], color='seagreen')
ax3.set_xlabel("Tonnes per Person")
ax3.set_title(f"Top 10 CO₂ per Capita in {selected_year}")
ax3.invert_yaxis()
st.pyplot(fig3)

# ----------------------------------------------
# 7. Emissions Trend for Selected Country
# ----------------------------------------------
st.subheader(f"📉 Emissions Trend for {selected_country}")

country_data = df[df['country'] == selected_country]

fig4, ax4 = plt.subplots()
ax4.plot(country_data['year'], country_data['co2'], marker='o')
ax4.set_xlabel("Year")
ax4.set_ylabel("CO₂ Emissions")
ax4.set_title(f"Emissions Over Time – {selected_country}")
st.pyplot(fig4)