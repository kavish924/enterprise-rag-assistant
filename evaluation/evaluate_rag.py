from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall
)

data = {
    "question": [
        "What is machine learning?"
    ],

    "answer": [
        "Machine learning is a field of AI that allows systems to learn from data."
    ],

    "contexts": [[
        "Machine learning is the science of programming computers so they can learn from data."
    ]],

    "ground_truth": [
        "Machine learning allows computers to learn from data without explicit programming."
    ]
}

dataset = Dataset.from_dict(data)

result = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_recall
    ]
)

print(result)