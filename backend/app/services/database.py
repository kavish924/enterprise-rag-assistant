from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:kavish31@localhost:5432/rag_com_db"
)

engine = create_engine(DATABASE_URL)