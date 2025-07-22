import pandas as pd
import sqlite3

def load_all_csvs():
    conn = sqlite3.connect(":memory:")

    pd.read_csv("ad_sales.csv").to_sql("ad_sales", conn, index=False, if_exists="replace")
    pd.read_csv("total_sales.csv").to_sql("total_sales", conn, index=False, if_exists="replace")
    pd.read_csv("eligibility.csv").to_sql("eligibility", conn, index=False, if_exists="replace")

    return conn

