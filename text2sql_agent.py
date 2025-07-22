from transformers import pipeline
import os

hf_token = os.getenv("HF_API_KEY")
text2sql = pipeline("text2text-generation", model="tscholak/opt-text2sql-finetuned", tokenizer="tscholak/opt-text2sql-finetuned", use_auth_token=hf_token)

def generate_sql(query):
    prompt = f"Translate this natural language question into SQL: {query}"
    output = text2sql(prompt, max_length=256, do_sample=False)
    return output[0]['generated_text']
