import streamlit as st
from db_loader import load_data
from text2sql_agent import generate_sql

st.set_page_config(page_title="Text2SQL Newsbot", page_icon="🧠")

st.title("🧠 Text2SQL Newsbot")
st.write("Upload your CSV and ask questions in plain English.")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df, conn = load_data(uploaded_file)
    st.dataframe(df)

    query = st.text_input("Ask a question:")
    if query:
        with st.spinner("Generating SQL..."):
            sql = generate_sql(query)
            st.code(sql, language="sql")

            try:
                result = conn.execute(sql).fetchall()
                st.success("✅ Query executed successfully!")
                st.dataframe(result)
            except Exception as e:
                st.error(f"❌ SQL Error: {e}")
