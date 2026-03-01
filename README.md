# 🚀 AI-Powered Real-Time Log Intelligence Platform

A production-style AI-driven log monitoring system that ingests streaming logs, performs LLM-based anomaly detection using **Ollama (Llama 3.2)**, exposes operational intelligence via REST APIs and MCP tools, and visualizes system health in a live dashboard.

---

# 🔥 Features

- Real-time streaming log ingestion
- Historical log bootstrap on startup
- Async LLM-based anomaly detection (Ollama)
- Redis-backed shared storage (multi-process safe)
- Flask REST API
- Live analytics dashboard
- MCP server for AI-agent tool exposure
- Fully Dockerized microservice architecture

---

# 🏗️ Full Architecture With Data Flow

![WhatsApp Image 2026-02-28 at 18 16 46](https://github.com/user-attachments/assets/f7450f4f-d8ea-4433-b471-8b3005b810ec)

---

# 🧠 Internal Data Flow

```
File → Parser → Redis → Queue → LLM Worker → Redis (Anomalies)
```

### Detailed Flow

1. Logs written to `logs/app.log`
2. Pipeline loads full file on startup
3. Switches to streaming mode (tail-like behavior)
4. Logs stored in Redis
5. Logs pushed to async LLM worker queue
6. Ollama classifies anomaly & severity
7. Anomalies stored back in Redis
8. Dashboard polls Flask API
9. MCP server exposes tools for AI agents

---

# 📦 Tech Stack

- Python 3.10
- Flask
- Redis
- Ollama (Llama 3.2)
- MCP (Model Context Protocol)
- Docker & Docker Compose
- Chart.js (Dashboard)

---

# 📁 Project Structure

```
ai-log-analyzer/
│
├── app/
│   ├── ingestion/
│   ├── processing/
│   ├── storage/
│   ├── pipelines/
│   ├── monitoring/
│   ├── api/
│   ├── mcp/
│   └── templates/
│
├── logs/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── run.py
```

---

# ⚙️ Configuration

Environment-driven configuration:

- `REDIS_URL`
- `OLLAMA_URL`
- `MODEL_NAME`
- `LLM_TIMEOUT`

Defaults allow local run without Docker.

---

# 🐳 Running with Docker (Using Host Ollama)

## 1️⃣ Start Ollama Locally

```
ollama run llama3.2
```

Exit after first load.

---

## 2️⃣ Ensure logs folder exists

```
mkdir logs
touch logs/app.log
```

Add a test log:

```
echo "2026-02-28 INFO Docker test log" >> logs/app.log
```

---

## 3️⃣ Run Docker

```
docker compose up --build
```

---

## 4️⃣ Access Dashboard

```
http://localhost:5000
```

---

# 🧪 Testing Real-Time Streaming

Append logs:

```
echo "2026-02-28 ERROR Payment failure" >> logs/app.log
```

Dashboard updates automatically.

---

# 🔌 MCP Tools Exposed

- `get_recent_logs`
- `get_recent_anomalies`
- `get_system_metrics`

Enables LLM-based operational querying.

---

# 📊 REST API Endpoints

| Endpoint        | Description |
|-----------------|------------|
| `/logs`         | Recent logs |
| `/anomalies`    | Detected anomalies |
| `/metrics`      | System metrics |
| `/health`       | Health status |

---

# 🧩 Architecture Patterns Used

- Producer–Consumer (LLM queue)
- Shared cache (Redis)
- Streaming ingestion
- Microservice separation
- Async background workers
- Environment-based config
- Tool exposure via MCP

---

# 🚨 Limitations

- File-based ingestion (not distributed)
- No offset tracking on restart
- No log rotation handling
- Polling-based UI (WebSocket possible)
- No authentication
- Redis persistence not enabled

---

# 🔮 Possible Improvements

- Kafka ingestion
- WebSocket real-time push
- Prometheus metrics
- Offset tracking
- Horizontal LLM scaling
- Rate limiting
- Authentication
- Kubernetes deployment
---

# 👤 Author

Dhamkirti Sisodia

AI Log Intelligence Platform  
Production-style streaming observability system.
