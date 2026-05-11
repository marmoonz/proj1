This project is an interactive housing affordability dashboard built using Python, Pandas, Streamlit, and Plotly.

The dashboard helps users compare housing affordability across different cities and ZIP codes by analyzing the relationship between income and rent.

The features include:

- Interactive affordability map
- City comparison charts
- Most affordable vs least affordable rankings
- ZIP code search
- Category and city filters
- Housing affordability scoring system

---

# Project Structure


proj1/
│
├── app.py
├── etl.py
├── test_etl.py
├── requirements.txt
├── README.md
├── reflection.md
│
└── data/
    └── final.csv




# Clone Repository

```bash
git clone <your-github-repo>
cd proj1
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

# Generate Dataset

```bash
python etl.py
```

This creates:

```text
data/final.csv
```

---

# Launch Streamlit Dashboard

```bash
streamlit run app.py
```

---

# Running Tests

Install pytest:

```bash
pip install pytest
```

Run tests:

```bash
pytest
```

---

# Tech Used

- Python
- Pandas
- Streamlit
- Plotly Express
- Pytest
- CSV Data Processing

---

#Future Improvements

- Real-world housing APIs
- HUD and Census integration
- Heatmap visualizations
- Machine learning affordability predictions
- Recommendation system