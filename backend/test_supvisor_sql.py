# test_supervisor_sql.py

from app.agents.supervisor import supervisor

query = "what is machine learning"

result = supervisor(query)

print(result)