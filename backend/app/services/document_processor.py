from app.services.pdf_loader import load_pdf
from app.services.chunker import chunk_documents
from app.services.vector_store import create_vector_store
import os

def process_pdf(pdf_path):

    docs = load_pdf(pdf_path)

    filename = os.path.basename(pdf_path)

    for doc in docs:
        doc.metadata["source"] = filename

    chunks = chunk_documents(docs)

    create_vector_store(chunks)

    return len(chunks)