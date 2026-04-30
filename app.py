import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("⌂ Housing Affordability in Syracuse")

df = pd.read_csv("data/final.csv")


df["affordability_score"] = df["income"] / (df["rent"] * 12)


st.sidebar.header("Filters")

category_options = df["category"].unique()

category_filter = st.sidebar.multiselect(
    "Category",
    category_options,
    default=category_options
)

zip_search = st.sidebar.text_input("Search ZIP Code")


filtered = df[df["category"].isin(category_filter)].copy()

if zip_search:
    filtered = filtered[filtered["zip"].astype(str).str.contains(zip_search)]


if len(filtered) == 0:
    st.warning("No results found. Try changing filters.")
    st.stop()


col1, col2, col3 = st.columns(3)

col1.metric("Avg Income", f"${int(filtered['income'].mean()):,}")
col2.metric("Avg Rent", f"${int(filtered['rent'].mean()):,}")
col3.metric("Avg Affordability Score", f"{filtered['affordability_score'].mean():.2f}")


st.subheader("Affordability Heatmap")

fig = px.density_mapbox(
    filtered,
    lat="lat",
    lon="lng",
    z="affordability_score",
    radius=25,
    center=dict(lat=43.05, lon=-76.15),  # Syracuse default
    zoom=9,
    mapbox_style="open-street-map"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Top Affordable Areas")

top_affordable = filtered.sort_values(
    "affordability_score",
    ascending=False
).head(10)

st.dataframe(top_affordable[[
    "zip", "income", "rent", "affordability_score", "category"
]])


st.subheader("Category Distribution")

fig2 = px.histogram(
    filtered,
    x="category",
    color="category"
)

st.plotly_chart(fig2, use_container_width=True)


st.subheader("Full Data")

st.dataframe(filtered.sort_values("affordability_score", ascending=False))