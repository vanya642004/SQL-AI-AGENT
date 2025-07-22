import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def generate_sql(query):
    prompt = f"""
    Convert the following natural language query into an SQL query that works with the following tables:
    - ad_sales
    - total_sales
    - eligibility

    Question: {query}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
