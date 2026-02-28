import threading
import queue
from flask import current_app
from .ollama_client import analyze_log
from ..storage.redis_store import store_anomaly

log_queue = queue.Queue()

def enqueue_log(log):
    log_queue.put(log)

def start_llm_worker(app):
    def worker():
        with app.app_context():
            while True:
                log = log_queue.get()
                try:
                    result = analyze_log(log)
                    log.update(result)
                    if result["anomaly"]:
                        store_anomaly(log)
                except Exception as e:
                    print("LLM error:", e)

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()