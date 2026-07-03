# 🤖 Enterprise RAG Assistant

An intelligent document processing system that combines **Retrieval-Augmented Generation (RAG)**, **LLMs**, and **SQL agents** to provide enterprise-grade AI-powered answers from documents and databases.

## 🎯 Features

- **PDF Document Processing**: Upload and process PDF documents into chunks for vector storage
- **Hybrid Retrieval**: Combines semantic search (Chroma) + BM25 keyword search for optimal context retrieval
- **Multi-Agent System**: 
  - Retrieval Agent: Answer questions from documents
  - SQL Agent: Query structured data from PostgreSQL
  - Summarizer Agent: Generate summaries of documents
  - Supervisor Agent: Route queries to appropriate handler
- **LLM Integration**: Uses Ollama with Llama 3 for local LLM inference
- **Vector Database**: Chroma for semantic similarity search
- **Real-time Monitoring**: Prometheus + Grafana dashboard
- **REST API**: FastAPI backend for easy integration
- **Web UI**: Streamlit frontend for user interaction

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (Streamlit)                      │
│              http://localhost:8501                           │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Backend (FastAPI)                               │
│              http://localhost:8000                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Supervisor Agent (Query Routing)              │  │
│  └─┬──────────────┬──────────────┬─────────────────────┘  │
│    │              │              │                         │
│  ┌─▼────┐  ┌─────▼──┐  ┌──────▼────┐                      │
│  │RAG    │  │SQL     │  │Summarizer │                      │
│  │Agent  │  │Agent   │  │Agent      │                      │
│  └─┬────┘  └─────┬──┘  └──────┬────┘                      │
│    │             │             │                           │
│  ┌─▼──────────┐  │  ┌──────────▼──┐                       │
│  │Chroma DB   │  │  │PostgreSQL    │                       │
│  │(Vector)    │  │  │(Structured)  │                       │
│  └────────────┘  │  └──────────────┘                       │
│                  │                                           │
│              ┌───▼────────┐                                 │
│              │Ollama Llama3│                                 │
│              └────────────┘                                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│         Monitoring (Prometheus + Grafana)                    │
│  Prometheus: http://localhost:9090                           │
│  Grafana: http://localhost:3000                              │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

Backend:
- FastAPI - Modern async web framework
- LangChain - LLM framework and tooling
- LangGraph - Agentic workflow orchestration
- Chroma - Vector database
- SQLAlchemy - ORM for database operations
- Ollama + Llama 3 - Local LLM inference
- Prometheus - Metrics collection
- Sentence Transformers - Embedding models

Frontend:
- Streamlit - Rapid prototyping UI framework
- Requests - HTTP client

Database:
- PostgreSQL - Structured data storage
- Chroma - Vector storage

DevOps:
- Docker & Docker Compose - Containerization
- Prometheus - Time-series metrics
- Grafana - Visualization dashboards

## 📋 Requirements

- Python 3.11+
- Docker & Docker Compose
- Ollama with Llama 3 model
- PostgreSQL 12+
- 8GB RAM (minimum)
- GPU (optional but recommended)

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone <repo-url>
cd enterprise-rag-assistant
```

### 2. Environment Configuration

Create `.env` file in the root directory:

```env
OPENAI_KEY=your_key_here
DATABASE_URL=postgresql://postgres:kavish31@localhost:5432/rag_com_db
```

### 3. Start Services

**Option A: Using Docker Compose**

```bash
docker-compose up -d
```

This will start:
- Backend API (port 8000)
- Frontend UI (port 8501)
- Prometheus (port 9090)
- Grafana (port 3000)

**Option B: Manual Setup**

```bash
# Terminal 1: Start Ollama
ollama serve llama3

# Terminal 2: Start PostgreSQL
docker run -d \
  -e POSTGRES_PASSWORD=kavish31 \
  -e POSTGRES_DB=rag_com_db \
  -p 5432:5432 \
  postgres:15

# Terminal 3: Start Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 4: Start Frontend
cd frontend
pip install -r requirements.txt
streamlit run app.py

# Terminal 5: Start Monitoring
cd backend/monitoring
docker-compose up -d
```

### 4. Access Services

- **Frontend UI**: http://localhost:8501
- **API Documentation**: http://localhost:8000/docs
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)

## 📁 Project Structure

```
enterprise-rag-assistant/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── graph.py           # LangGraph workflow
│   │   │   ├── retrieval_agent.py # RAG agent
│   │   │   ├── sql_agent.py       # Database query agent
│   │   │   ├── summarizer_agent.py# Text summarization
│   │   │   └── supervisor.py      # Query routing
│   │   ├── services/
│   │   │   ├── rag.py             # RAG pipeline
│   │   │   ├── vector_store.py    # Chroma integration
│   │   │   ├── document_processor.py
│   │   │   ├── pdf_loader.py
│   │   │   ├── chunker.py
│   │   │   ├── database.py
│   │   │   └── hybrid_retriever.py
│   │   ├── monitoring/
│   │   │   ├── metrics.py         # Prometheus metrics
│   │   │   ├── prometheus.yml
│   │   │   └── docker-compose.yml
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── logger.py
│   │   └── main.py                # FastAPI app
│   ├── requirements.txt
│   ├── dockerfile
│   └── test_*.py                  # Test scripts
├── frontend/
│   ├── app.py                     # Streamlit app
│   ├── requirements.txt
│   └── dockerfile
├── evaluation/
│   ├── evaluate_rag.py            # RAGAS metrics
│   └── test_question.txt
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└── README.md
```

## 🔌 API Endpoints

### Health Check
```bash
GET /health
```

### Chat Endpoint
```bash
POST /chat
Content-Type: application/json

{
  "query": "What is machine learning?"
}

Response:
{
  "answer": "...",
  "sources": ["document1.pdf"],
  "retrieved_chucks": 5
}
```

### PDF Upload
```bash
POST /upload
Content-Type: multipart/form-data

file: <PDF_FILE>

Response:
{
  "message": "PDF processed successfully",
  "chunks": 45
}
```

### Metrics
```bash
GET /metrics
```

## 📊 Monitoring Dashboard

The project includes pre-configured Grafana dashboards that monitor:

Request Count: Total API requests over time
Request Latency: Response time distribution (P50, P95, P99)
-System Health: Backend, LLM, Vector DB, and PostgreSQL status
Error Rates: Failed requests tracking

**Grafana Login:**
- URL: http://localhost:3000
- Username: admin
- Password: admin

## 🎯 Query Routing Logic

The supervisor agent intelligently routes queries:

```
User Query
    ↓
Supervisor Agent
    ├─ Contains: "summary", "summarize", "overview" → Summarizer Agent
    ├─ Contains: "employee", "salary", "database" → SQL Agent
    └─ Default → Retrieval Agent (RAG)
```

## 🔍 Retrieval Strategy

The RAG system uses hybrid retrieval:

1. **Vector Search** (Semantic): Uses Chroma with HuggingFace embeddings
2. **BM25 Search** (Lexical): Keyword-based retrieval
3. **Deduplication**: Removes duplicate results
4. **Re-ranking**: Returns top 5 most relevant chunks

## 📈 Performance Optimization

- **Chunking**: 500-character chunks with 100-character overlap
- **Embeddings**: Lightweight sentence-transformers model
- **Caching**: Vector store persistence
- **Batch Processing**: Efficient PDF processing

## 🐛 Troubleshooting

### Ollama Connection Error
```bash
# Make sure Ollama is running
ollama serve llama3

# Or pull the model first
ollama pull llama3
```

### PostgreSQL Connection Error
```bash
# Check PostgreSQL is running
psql -U postgres -d rag_com_db

# Check credentials in .env file
```

### Vector Store Not Found
```bash
# Re-process PDFs through the UI
# Or manually trigger document processing
python backend/test_vectorstore.py
```

## 📚 Dependencies

See `requirements.txt` for full list. Key packages:

```
fastapi==0.104.1
langchain==0.1.0
langchain-community==0.0.10
langchain-ollama==0.1.0
chromadb==0.4.21
sentence-transformers==2.2.2
streamlit==1.45.1
prometheus-client==0.19.0
```

## 🔐 Security Considerations

- [ ] Add API authentication (JWT tokens)
- [ ] Implement rate limiting
- [ ] Add request validation
- [ ] Encrypt sensitive data in database
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS in production

## 🚀 Deployment

### Docker Deployment
```bash
docker-compose -f docker-compose.yml up -d
```

### Production Checklist
- [ ] Set strong PostgreSQL password
- [ ] Configure Grafana with authentication
- [ ] Add reverse proxy (Nginx)
- [ ] Enable SSL/TLS certificates
- [ ] Set up log aggregation
- [ ] Configure backup strategy
- [ ] Monitor resource usage

## 📖 Usage Examples

### Example 1: Ask About Documents
1. Open http://localhost:8501
2. Upload a PDF in the sidebar
3. Ask: "What is the main topic?"
4. Get answers with source citations

### Example 2: Query Database
1. Upload employee data
2. Ask: "What is the average salary?"
3. System converts to SQL and executes

### Example 3: Summarization
1. Upload a long document
2. Ask: "Summarize this document"
3. Get concise summary

## 🧪 Testing

Run test scripts to validate components:

```bash
# Test PDF loading
python backend/test_loader.py

# Test vector store
python backend/test_vectorstore.py

# Test RAG retrieval
python backend/test_retrieval.py

# Test RAG answer generation
python backend/test_rag_answer.py

# Test SQL agent
python backend/test_sql_agent.py

# Test supervisor routing
python backend/test_supervisor.py
```

## 📊 Evaluation

The project uses RAGAS metrics for RAG evaluation:

```bash
python evaluation/evaluate_rag.py
```

Metrics:
- **Faithfulness**: Does the answer match the context?
- **Answer Relevancy**: Is the answer relevant to the question?
- **Context Recall**: Is relevant context retrieved?

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Agents](https://langchain-ai.github.io/langgraph/)
- [Chroma Vector DB](https://docs.trychroma.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Ollama](https://ollama.ai/)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Kavish Kumar

## 🙏 Acknowledgments

- LangChain team for the excellent framework
- Ollama for local LLM inference
- Chroma for vector database
- FastAPI community
