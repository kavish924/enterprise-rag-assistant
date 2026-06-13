from app.agents.graph import graph

result = graph.invoke(
    {
        "query": "What is machine learning?"
    }
)

print(result)