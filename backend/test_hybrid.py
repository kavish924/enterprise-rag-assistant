from app.services.rag import retrieve_context

docs = retrieve_context(
    "What is machine learning?"
)

print("Retrieved:", len(docs))

for i, doc in enumerate(docs):

    print(f"\nResult {i+1}")

    print(doc.page_content[:300])