import pandas as pd

print("🔥 ETL STARTED")

def build():

    df = pd.DataFrame({
        "zip": ["13210", "13211", "13212", "10001", "10002", "14201"],
        "city": ["Syracuse", "Syracuse", "Syracuse", "New York", "New York", "Buffalo"],
        "income": [50000, 60000, 45000, 90000, 85000, 55000],
        "lat": [43.0481, 43.0600, 43.0700, 40.7500, 40.7200, 42.8800],
        "lng": [-76.1474, -76.1600, -76.1800, -73.9960, -73.9900, -78.8800],
        "rent": [1200, 1300, 1100, 2500, 2300, 1400]
    })

    # affordability score
    df["affordability_score"] = (df["rent"] * 12) / df["income"]

    # categories (expanded)
    def label(x):
        if x < 0.20:
            return "Very Affordable"
        elif x < 0.30:
            return "Affordable"
        elif x < 0.40:
            return "Moderate"
        elif x < 0.55:
            return "Somewhat Unaffordable"
        elif x < 0.75:
            return "Expensive"
        else:
            return "Severely Unaffordable"

    df["category"] = df["affordability_score"].apply(label)

    df.to_csv("data/final.csv", index=False)

    print("✅ DONE")

build()