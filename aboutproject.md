name: mariama
email: mbarry16@syr.edu

## Project Goal

The goal of this project is to build an interactive housing affordability dashboard that helps users understand and compare the cost of housing across different cities and ZIP codes. The application allows users to explore how income relates to rent in different areas and identifies whether housing is affordable or unaffordable based on a calculated affordability score.

This project demonstrates a full data pipeline including data generation (ETL), transformation, analysis, and interactive visualization using Streamlit and Plotly.



## Data Sources

This project currently uses a **synthetic dataset** generated using Python for demonstration purposes. The dataset simulates real housing data and includes:

- ZIP codes
- Cities (Syracuse, New York, Buffalo)
- Median income
- Rent values
- Latitude and longitude coordinates

Future improvements will integrate real-world datasets such as:
- U.S. Census Bureau income data
- HUD housing affordability data
- Public real estate APIs

---

## Data Extraction & Structure

The dataset is created inside an ETL pipeline (`etl.py`) using pandas. The final dataset contains the following columns:

- `zip` – ZIP code of the area  
- `city` – City name  
- `income` – Median household income  
- `rent` – Monthly rent estimate  
- `lat`, `lng` – Geographic coordinates  
- `affordability_score` – Ratio of rent burden (rent vs income)  
- `category` – Housing affordability classification  

---



The following preprocessing steps were applied:

- Standardized dataset structure using pandas DataFrame
- Created calculated field:  
  - affordability score = (rent × 12) / income
- Converted continuous score into categorical labels:
  - Very Affordable
  - Affordable
  - Moderate
  - Somewhat Unaffordable
  - Expensive
  - Severely Unaffordable
- Ensured no missing values in generated dataset

These steps ensure consistent and meaningful comparison across locations.

---



A custom ETL pipeline was built using Python:

- Generated synthetic housing dataset
- Applied mathematical transformation for affordability score
- Created classification function to assign affordability categories
- Exported cleaned dataset to CSV (`data/final.csv`)

Key transformation function:

- affordability_score = (rent × 12) / income

---



The Streamlit dashboard includes:


- Displays housing locations using latitude and longitude
- Color-coded by affordability category
- Hover information includes ZIP, city, rent, and income


- Compares affordability across cities
- Helps identify which cities are more expensive overall


- Shows most and least affordable ZIP codes
- Sorted by affordability score


- Filter by city
- Filter by affordability category
- ZIP code search


- Cities like New York show higher rent burden compared to Syracuse and Buffalo
- Affordability varies significantly even within the same dataset
- Income-to-rent ratio is a useful metric for comparing housing affordability

---
