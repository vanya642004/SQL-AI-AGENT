import os
import google.generativeai as genai

# Load Gemini API key from Streamlit Secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def generate_sql(query):
    prompt = f"Convert this natural language question into SQL: {query}"
    response = model.generate_content(prompt)
    return response.text
