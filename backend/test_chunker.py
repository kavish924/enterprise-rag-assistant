from app.services.pdf_loader import load_pdf
from app.services.chunker import chunk_documents

docs = load_pdf(r"C:\Users\kavis\enterprise-rag-assistant\data\raw\mlnotes.pdf")

chunks = chunk_documents(docs)

print("Chunks:", len(chunks))
print("\nFirst Chunk:\n")
print(chunks[0].page_content[:300])