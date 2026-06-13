from app.agents.sql_agent import sql_agent

query = "Show all employees"

result = sql_agent(query)

print(result)