from fastapi import FastAPI,UploadFile, File
from fastapi.responses import Response
from pydantic import BaseModel
from app.services.rag import generate_answer
from app.services.document_processor import process_pdf
from prometheus_client import generate_latest
import time
import os
import shutil
import sys
from pathlib import Path
from app.monitoring.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY
)


app = FastAPI(
    title="Enterprise RAG Assistant",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "Enterprise RAG Assistant Running"}

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "llm": "llama3",
        "vector_db": "chroma",
        "postgres": "connected"
    }

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type="text/plain"
    )

@app.post("/chat")
def chat(request: QueryRequest):

    REQUEST_COUNT.inc()

    start = time.time()

    result = generate_answer(
        request.query
    )

    REQUEST_LATENCY.observe(
        time.time() - start
    )

    return result


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    upload_dir = "../data/uploads"

    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    chunk_count = process_pdf(file_path)

    return {
        "message": "PDF processed successfully",
        "chunks": chunk_count
    }




