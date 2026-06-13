from app.agents.retrieval_agent import retrieval_agent
from app.agents.summarizer_agent import summarizer_agent
from app.agents.sql_agent import sql_agent


def supervisor(query):

    query_lower = query.lower()

    # Summarization Queries
    if any(word in query_lower for word in [
        "summary",
        "summarize",
        "overview",
        "brief"
    ]):
        return summarizer_agent(query)

    # SQL Queries
    elif any(word in query_lower for word in [
        "employee",
        "employees",
        "salary",
        "department",
        "revenue",
        "sales",
        "database",
        "table"
    ]):
        return sql_agent(query)

    # Default → RAG Retrieval
    else:
        return retrieval_agent(query)