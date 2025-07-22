# text2sql_agent.py
from transformers import pipeline
import os

hf_token = os.getenv("HF_API_KEY")

text2sql = pipeline(
    "text2text-generation",
    model="tscholak/opt-iml-max-1.3b",  # recommended text2sql-compatible model
    use_auth_token=hf_token
)

def generate_sql(nl_query):
    result = text2sql(nl_query, max_length=512, do_sample=False)
    return result[0]["generated_text"]
