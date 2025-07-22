import streamlit as st
import sqlite3
import pandas as pd
from text2sql_agent import generate_sql

# Connect to SQLite DB
db_path = "ecom.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

st.title("🧠 Text2SQL E-commerce Agent")

query = st.text_input("Ask a question about your sales data:")

if st.button("Generate Answer") and query:
    sql = generate_sql(query)
    st.markdown(f"**Generated SQL:** `{sql}`")
    try:
        result = pd.read_sql_query(sql, conn)
        st.dataframe(result)
    except Exception as e:
        st.error(f"Error running SQL: {e}")
