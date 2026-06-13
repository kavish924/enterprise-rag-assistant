from app.services.database import engine
from sqlalchemy import text

with engine.connect() as conn:

    result = conn.execute(
        text("SELECT * FROM employees")
    )

    for row in result:
        print(row)