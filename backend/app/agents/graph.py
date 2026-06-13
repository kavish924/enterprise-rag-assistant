from typing import TypedDict
from langgraph.graph import StateGraph

from app.agents.retrieval_agent import retrieval_agent


class AgentState(TypedDict):
    query: str
    answer: str


def retrieval_node(state):

    result = retrieval_agent(
        state["query"]
    )

    return {
        "answer": result["answer"]
    }


builder = StateGraph(AgentState)

builder.add_node(
    "retrieval",
    retrieval_node
)

builder.set_entry_point(
    "retrieval"
)

builder.set_finish_point(
    "retrieval"
)

graph = builder.compile()