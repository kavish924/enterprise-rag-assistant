from app.services.pdf_loader import load_pdf

docs = load_pdf("C:\\Users\\kavis\\enterprise-rag-assistant\\data\\raw\\mlnotes.pdf")

print(f"Pages: {len(docs)}")
print(docs[0].page_content[:500])