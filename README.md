# Azure Docker Apps — Single Endpoint Sample

A minimal, production‑minded template that exposes a single HTTP endpoint and runs in Docker. Intended as a clean starting point for deploying to Azure Container Apps.

- Stack: Python 3.12 + FastAPI + Uvicorn
- Endpoint: GET /health → { "status": "ok" }
- Container: Small slim image, non‑root user

## Project structure
```
.
├─ app/
│  └─ main.py           # FastAPI app with one endpoint (/health)
├─ requirements.txt     # Pinned runtime dependencies
├─ Dockerfile           # Production container (Python slim, non-root)
├─ .gitignore           # Git hygiene
├─ .dockerignore        # Smaller/cleaner Docker build context
└─ .env.example         # Example env file (not required)
```

## Prerequisites
- Python 3.12+
- Docker (optional, for containerized run)

## Run locally (without Docker)
```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Start server on port 8080
uvicorn app.main:app --host 0.0.0.0 --port 8080
```
Test it:
```
curl http://localhost:8080/health
# => {"status":"ok"}
```

## Run with Docker
Build the image:
```
docker build -t hello-aca:local .
```
Run the container:
```
docker run --rm -p 8080:8080 hello-aca:local
```
Test it:
```
curl http://localhost:8080/health
# => {"status":"ok"}
```

## Notes for Azure Container Apps
- Exposed port is 8080 (Dockerfile EXPOSE 8080). Use --target-port 8080 when creating the app.
- Use ACR to build/push images, and deploy to ACA with Azure CLI (identity + AcrPull role recommended).
- For a full walkthrough (resource creation, build, deploy, CI), see the instructions you plan to apply for your environment.

## Scope: single endpoint only
This template intentionally includes only one endpoint (/health). Add more only when needed; for learning and deployment practice, this keeps the surface minimal and easy to reason about.

## Git hygiene
- .gitignore and .dockerignore are set up to keep the repo clean and Docker contexts small.
- Do not commit secrets. Use environment variables or Azure secrets; .env is ignored by default.
