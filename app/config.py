import os


BASE_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))
)


class Config:

    # -------- LOG FILE --------
    LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")

    # -------- REDIS --------
    # From docker-compose:
    # REDIS_URL=redis://redis:6379/0
    REDIS_URL = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0"
    )

    # -------- OLLAMA --------
    # From docker-compose:
    # OLLAMA_URL=http://host.docker.internal:11434/api/generate
    OLLAMA_URL = os.getenv(
        "OLLAMA_URL",
        "http://localhost:11434/api/generate"
    )

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama3.2"
    )

    # -------- PIPELINE SETTINGS --------
    LOG_BUFFER_LIMIT = 1000
    ANOMALY_BUFFER_LIMIT = 200

    # -------- LLM SETTINGS --------
    LLM_TIMEOUT = int(
        os.getenv("LLM_TIMEOUT", 15)
    )

    # -------- DEBUG --------
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"