import google.generativeai as genai
import os
import sqlite3


# Add your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Replace with a supported model
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # safe and supported

def generate_sql(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"-- Gemini API Error: {e}"
