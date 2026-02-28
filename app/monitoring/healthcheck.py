def health():
    return {
        "status": "healthy",
        "redis": "connected",
        "llm_worker": "running"
    }