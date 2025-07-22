import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_sql(query):
    model = genai.GenerativeModel("models/gemini-pro")  # ✅ Use full path
    prompt = f"""
    Convert this natural language query to a SQL query.
    Available tables: ad_sales, total_sales, eligibility.

    Query: {query}
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"-- Gemini API Error: {e}"
