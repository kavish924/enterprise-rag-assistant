from app.agents.supervisor import supervisor

queries = [
    "What is machine learning?",
    "Show all employees",
    "What is the highest salary?",
    "Summarize machine learning"
]

for query in queries:
    print(f"\nQuery: {query}")
    print(supervisor(query))