from fastapi import FastAPI

app = FastAPI(title="Azure Docker Apps Sample", version="0.1.0")


@app.get("/health")
def health():
    """Simple health endpoint for readiness/liveness checks."""
    return {"status": "okay"}
