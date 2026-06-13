from app.services.rag import generate_answer

def retrieval_agent(query):
    return generate_answer(query)