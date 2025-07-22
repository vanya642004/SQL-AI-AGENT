import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_sql(prompt):
    response = model.generate_content(prompt)
    return response.text
