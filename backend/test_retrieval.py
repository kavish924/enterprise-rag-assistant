from app.services.rag import retrieve_context

results = retrieve_context(
    "What is machine learning?"
)

print("\nTop Results:\n")

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print(doc.page_content[:300])