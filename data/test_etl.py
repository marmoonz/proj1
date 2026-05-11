from etl import build
import pandas as pd
import os

def test_csv_created():
    build()
    assert os.path.exists("data/final.csv")

def test_affordability_column():
    build()
    df = pd.read_csv("data/final.csv")
    assert "affordability_score" in df.columns

def test_category_column():
    build()
    df = pd.read_csv("data/final.csv")
    assert "category" in df.columns