import streamlit as st
from db_loader import load_data
from text2sql_agent import generate_sql
import os

st.set_page_config(page_title="📊 Text2SQL with Gemini", page_icon="🧠")

st.title("🧠 Text2SQL Agent with Gemini (CSV to SQL)")

query = st.text_input("Ask your question:")

if query:
    sql = generate_sql(query)
    st.subheader("🔍 Generated SQL")
    st.code(sql, language="sql")

    con = load_data()

    try:
        result = con.execute(sql).fetchdf()

        if result.empty:
            st.warning("No results found.")
        else:
            st.subheader("✅ Result")
            st.dataframe(result)

    except Exception as e:
        st.error(f"❌ SQL Error: {e}")
