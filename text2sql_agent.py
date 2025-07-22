from transformers import pipeline

# Load a lightweight Text2SQL model from Hugging Face
generator = pipeline("text2text-generation", model="tscholak/opt-1.3b-sql")

def generate_sql(query):
    prompt = f"Translate to SQL: {query}"
    result = generator(prompt, max_length=256, do_sample=False)
    return result[0]['generated_text']
