from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Assistant",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Enterprise RAG Assistant Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}