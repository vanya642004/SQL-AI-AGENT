import duckdb
import pandas as pd

def load_data():
    con = duckdb.connect(database='ecom.duckdb', read_only=False)

    ad = pd.read_csv('ad_sales.csv')
    total = pd.read_csv('total_sales.csv')
    eligibility = pd.read_csv('eligibility.csv')

    con.execute("CREATE OR REPLACE TABLE ad_sales AS SELECT * FROM ad")
    con.execute("CREATE OR REPLACE TABLE total_sales AS SELECT * FROM total")
    con.execute("CREATE OR REPLACE TABLE eligibility AS SELECT * FROM eligibility")

    return con
