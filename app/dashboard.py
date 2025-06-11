# ----------------------------------------------
# 🌍 Streamlit CO₂ Emissions Dashboard
# ----------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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

# -------------------------------------------------
# 8. 📈 CO₂ Emissions Over Time by Selected Countries
# -------------------------------------------------
st.subheader("📈 Compare CO₂ Emissions Over Time")

# Let user select multiple countries
multi_countries = st.multiselect(
    "Choose countries to compare:",
    options=df['country'].unique(),
    default=["United States", "China", "India"]
)

# Filter data
multi_country_data = df[df['country'].isin(multi_countries)]

# Plotly line chart
fig5 = px.line(
    multi_country_data,
    x="year",
    y="co2",
    color="country",
    labels={"co2": "CO₂ Emissions (Million Tonnes)", "year": "Year"},
    title="CO₂ Emissions Comparison Over Time"
)
st.plotly_chart(fig5, use_container_width=True)

# -----------------------------------------
# 9. 🔝 Top 10 CO₂ Emitters for a Given Year
# -----------------------------------------
st.subheader("🔝 Top 10 CO₂ Emitting Countries (Yearly)")

# Choose a year
top_year = st.slider("Select year:", int(df['year'].min()), int(df['year'].max()), 2020)

# Filter and sort
top_emitters = (
    df[df['year'] == top_year]
    .sort_values(by='co2', ascending=False)
    .head(10)
)

# Bar chart
fig6 = px.bar(
    top_emitters,
    x='country',
    y='co2',
    labels={"co2": "CO₂ Emissions (Million Tonnes)", "country": "Country"},
    title=f"Top 10 CO₂ Emitters in {top_year}",
    color='country',
    text='co2'
)
fig6.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig6.update_layout(showlegend=False)
st.plotly_chart(fig6, use_container_width=True)

# ---------------------------------------
# 10. 🌍 Global CO₂ Emissions Choropleth Map
# ---------------------------------------
st.subheader("🌍 Global CO₂ Emissions by Country")

# Choose a year for the map
map_year = st.slider("Select year for map:", int(df['year'].min()), int(df['year'].max()), 2020, key="map_year_slider")

# Prepare map data
map_data = df[df['year'] == map_year]

fig7 = px.choropleth(
    map_data,
    locations="country",
    locationmode="country names",
    color="co2",
    hover_name="country",
    color_continuous_scale="Reds",
    title=f"Global CO₂ Emissions in {map_year}",
    labels={"co2": "CO₂ Emissions"}
)
fig7.update_layout(geo=dict(showframe=False, projection_type='natural earth'))
st.plotly_chart(fig7, use_container_width=True)