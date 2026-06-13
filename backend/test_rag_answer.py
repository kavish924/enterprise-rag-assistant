from app.services.rag import generate_answer

question = "What is machine learning?"

answer = generate_answer(question)

print("\nAnswer:\n")
print(answer)