import sqlite3
import pandas as pd

# Load CSVs
total_sales = pd.read_csv("ecommerce/total_sales.csv")
ad_sales = pd.read_csv("ecommerce/ad_sales.csv")
eligibility = pd.read_csv("ecommerce/eligibility.csv")

# Save to SQLite
conn = sqlite3.connect("ecom.db")
total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)
ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)
conn.close()
