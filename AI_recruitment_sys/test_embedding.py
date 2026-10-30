from app.services.embedding import generate_embedding

text = """
Python
FastAPI
Docker
"""

embedding = generate_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])