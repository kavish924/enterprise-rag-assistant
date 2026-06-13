from sqlalchemy import create_engine, text
from langchain_ollama import ChatOllama

DATABASE_URL = (
    "postgresql://postgres:kavish31@localhost:5432/rag_com_db"
)

engine = create_engine(DATABASE_URL)

llm = ChatOllama(model="llama3")


def sql_agent(query):

    prompt = f"""
    Convert the user question into SQL.

    Table:
    employees(id, name, department, salary)

    Question:
    {query}

    Return ONLY SQL.
    """

    sql_query = llm.invoke(prompt).content.strip()

    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            rows = result.fetchall()

        return {
            "sql": sql_query,
            "result": str(rows)
        }

    except Exception as e:
        return {
            "error": str(e),
            "sql": sql_query
        }