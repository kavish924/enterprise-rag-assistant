from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from rank_bm25 import BM25Okapi

def load_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="../vectorstore",
        embedding_function=embeddings
    )

    return db
llm = ChatOllama(
    model="llama3"
)


def retrieve_context(query):

    db = load_vector_store()

    # Chroma Retrieval
    vector_docs = db.max_marginal_relevance_search(
        query,
        k=5
    )

    # BM25 Retrieval
    all_docs = db.similarity_search(
        query,
        k=20
    )

    corpus = [
        doc.page_content.split()
        for doc in all_docs
    ]

    bm25 = BM25Okapi(corpus)

    scores = bm25.get_scores(query.split())

    top_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:5]

    bm25_docs = [
        all_docs[i]
        for i in top_indices
    ]

    # Merge + Deduplicate
    combined = vector_docs + bm25_docs

    unique_docs = []

    seen = set()

    for doc in combined:

        if doc.page_content not in seen:

            unique_docs.append(doc)

            seen.add(doc.page_content)

    return unique_docs[:5]

def generate_answer(query):

    docs = retrieve_context(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    confidence = len(docs)

    sources = list(
        set(
            [
                doc.metadata.get("source", "Unknown")
                for doc in docs
            ]
        )
    )
    prompt = f"""
You are an enterprise AI assistant.

Rules:
1. Answer only from the provided context.
2. If the answer is not in the context, say:
   "I could not find that information in the documents."
3. Be concise and factual.

Context:
{context}

Question:
{query}

Answer:
"""
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources,
        "retrieved_chucks":len(docs)
    }