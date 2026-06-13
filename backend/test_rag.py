from app.services.rag import load_vector_store

db = load_vector_store()

print("Vector store loaded successfully")