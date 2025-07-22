from transformers import pipeline

generator = pipeline(
    "text2text-generation", 
    model="nsi319/legal-text-to-sql-t5-small"
)

def generate_sql(query):
    prompt = f"Translate to SQL: {query}"
    result = generator(prompt, max_length=256, do_sample=False)
    return result[0]['generated_text']
