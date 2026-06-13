from app.services.pdf_loader import load_pdf
from app.services.chunker import chunk_documents
from app.services.vector_store import create_vector_store

docs = load_pdf(
    r"C:\Users\kavis\enterprise-rag-assistant\data\raw\mlnotes.pdf"
)

chunks = chunk_documents(docs)

db = create_vector_store(chunks)

print("Vector database created successfully")