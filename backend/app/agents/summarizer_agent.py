from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

def summarizer_agent(text):

    prompt = f"""
    Summarize the following:

    {text}
    """

    response = llm.invoke(prompt)

    return response.content