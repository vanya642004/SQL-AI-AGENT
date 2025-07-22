import streamlit as st
from db_loader import load_all_csvs
from text2sql_agent import generate_sql

st.set_page_config(page_title="CSV Text2SQL Agent", page_icon="🧠")
st.title("🧠 Text2SQL Agent for E-commerce CSVs")
st.write("Ask questions about your data in plain English.")

query = st.text_input("Ask your question:")

if query:
    st.write(f"🔎 Interpreting: **{query}**")
    sql = generate_sql(query)
    st.code(sql, language="sql")

    try:
        conn = load_all_csvs()
        result = conn.execute(sql).fetchall()
        columns = [desc[0] for desc in conn.execute(sql).description]
        st.success("✅ Query executed successfully!")
        st.dataframe(result, use_container_width=True)
    except Exception as e:
        st.error(f"❌ SQL Execution Error: {e}")
