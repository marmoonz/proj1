import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Housing Affordability in Top East Coast Cities")

# LOAD DATA
df = pd.read_csv("data/final.csv")

# SIDEBAR FILTERS
st.sidebar.title("Filters")

cities = st.sidebar.multiselect(
    "Select Cities",
    df["city"].unique(),
    df["city"].unique()
)

categories = st.sidebar.multiselect(
    "Select Category",
    df["category"].unique(),
    df["category"].unique()
)

# USER INCOME SIMULATOR 
st.sidebar.title("Your Profile")

user_income = st.sidebar.slider(
    "Annual Income",
    20000,
    200000,
    60000,
    step=5000
)

# FILTER DATA
filtered = df[
    (df["city"].isin(cities)) &
    (df["category"].isin(categories))
].copy()

# SAFETY CHECK
if filtered.empty:
    st.warning("No data matches your filters.")
    st.stop()

# ---------------- AFFORDABILITY CALC ----------------
filtered["can_afford"] = (filtered["rent"] * 12) / user_income < 0.30

# KPI METRICS
st.subheader("Summary Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Rent", f"${filtered['rent'].mean():.0f}")
col2.metric("Avg Income", f"${filtered['income'].mean():.0f}")
col3.metric("Avg Burden", f"{filtered['affordability_score'].mean():.2f}")

# AFFORDABILITY INSIGHT
st.subheader(" Your Affordability Insight")

affordable_count = filtered["can_afford"].sum()
total = len(filtered)

st.metric("Affordable Options for You", f"{affordable_count} / {total}")

# MAP
st.subheader("Housing Affordability Map")

fig_map = px.scatter_mapbox(
    filtered,
    lat="lat",
    lon="lng",
    color="category",
    size="rent",
    hover_name="city",
    zoom=4,
    height=500
)

fig_map.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig_map, use_container_width=True)

# HEATMAP
st.subheader(" Housing Density Heatmap")

fig_heat = px.density_mapbox(
    filtered,
    lat="lat",
    lon="lng",
    z="rent",
    radius=25,
    center=dict(lat=42.9, lon=-75),
    zoom=4,
    mapbox_style="open-street-map"
)

st.plotly_chart(fig_heat, use_container_width=True)

# SCATTER
st.subheader("Income vs Rent Analysis")

fig_scatter = px.scatter(
    filtered,
    x="income",
    y="rent",
    color="category",
    size="affordability_score",
    hover_name="city"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# PIE CHART
st.subheader(" Affordability Breakdown")

fig_pie = px.pie(
    filtered,
    names="category"
)

st.plotly_chart(fig_pie, use_container_width=True)

# BOX PLOT
st.subheader(" Rent Distribution by City")

fig_box = px.box(
    filtered,
    x="city",
    y="rent",
    color="city"
)

st.plotly_chart(fig_box, use_container_width=True)

# CITY RANKING 
st.subheader(" City Affordability Ranking")

ranked = df.groupby("city")["affordability_score"].mean().reset_index()
ranked = ranked.sort_values("affordability_score")

fig_rank = px.bar(
    ranked,
    x="city",
    y="affordability_score",
    color="affordability_score",
    title="Lower Score = More Affordable"
)

st.plotly_chart(fig_rank, use_container_width=True)

# TABLE 
st.subheader(" Data Table")

st.dataframe(
    filtered.sort_values("affordability_score")
)