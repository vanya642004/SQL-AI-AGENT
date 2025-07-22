import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def generate_sql(user_query):
    prompt = f"""
You are an expert in converting natural language to SQL queries.
Generate a DuckDB SQL query based on this question:

Tables:
- ad_sales(item_id, ad_sales, impressions, ad_spend, clicks, units_sold, date)
- total_sales(item_id, total_sales, total_units_ordered, date)
- eligibility(item_id, eligibility, message, eligibility_datetime_utc)

Natural language: {user_query}

SQL:
"""
    response = model.generate_content(prompt)
    return response.text.strip()

