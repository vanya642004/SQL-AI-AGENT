import streamlit as st
from db_loader import load_data
from text2sql_agent import generate_sql

st.set_page_config(page_title="Text2SQL CSV Agent", page_icon="🧠")

st.title("🧠 Text2SQL Agent for E-commerce CSV Data")

query = st.text_input("Ask your question in plain English:")

if query:
    sql = generate_sql(query)
    st.subheader("🔄 Generated SQL")
    st.code(sql, language='sql')

    con = load_data()

    try:
        result = con.execute(sql).fetchdf()

        if result.empty:
            st.warning("No results found.")
        else:
            st.subheader("✅ Answer")
            st.dataframe(result)

            if len(result.columns) == 1:
                st.success(f"{result.columns[0]}: {result.iloc[0, 0]}")
            elif result.shape == (1, 2):
                st.success(f"{result.columns[0]}: {result.iloc[0, 0]}, {result.columns[1]}: {result.iloc[0, 1]}")

    except Exception as e:
        st.error(f"❌ SQL Error: {e}")
