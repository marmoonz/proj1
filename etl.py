import pandas as pd

print("🔥 ETL STARTED")

def build():
    print("📊 Building dataset...")

    # STEP 1: CREATE DATAFRAME (THIS WAS MISSING OR BROKEN)
    df = pd.DataFrame({
    "zip": [
        "13210","13211","13212",
        "10001","10002",
        "14201","12207","14604",
        "02108","19103",
        "07102","07302"
    ],
    "city": [
        "Syracuse","Syracuse","Syracuse",
        "New York","New York",
        "Buffalo","Albany","Rochester",
        "Boston","Philadelphia",
        "Newark","Jersey City"
    ],
    "income": [
        50000,60000,45000,
        90000,85000,
        55000,65000,58000,
        110000,75000,
        70000,95000
    ],
    "lat": [
        43.0481,43.0600,43.0700,
        40.7500,40.7200,
        42.8800,42.6526,43.1566,
        42.3601,39.9526,
        40.7357,40.7282
    ],
    "lng": [
        -76.1474,-76.1600,-76.1800,
        -73.9960,-73.9900,
        -78.8784,-73.7562,-77.6088,
        -71.0589,-75.1652,
        -74.1724,-74.0776
    ],
    "rent": [
        1200,1300,1100,
        2500,2300,
        1400,1500,1350,
        3200,2000,
        1800,2800
    ]
})

    
    df["affordability_score"] = (df["rent"] * 12) / df["income"]

    # STEP 3: CATEGORY FUNCTION
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


if __name__ == "__main__":
    build()