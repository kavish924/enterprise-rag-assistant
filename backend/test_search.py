from app.services.pdf_loader import load_pdf
from app.services.chunker import chunk_documents
from app.services.vector_store import (
    create_vector_store,
    search_documents
)

docs = load_pdf(
    r"C:\Users\kavis\enterprise-rag-assistant\data\raw\mlnotes.pdf"
)

chunks = chunk_documents(docs)

db = create_vector_store(chunks)

results = search_documents(
    db,
    "What is machine learning?"
)

print("\nTop Results:\n")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print(result.page_content[:300])