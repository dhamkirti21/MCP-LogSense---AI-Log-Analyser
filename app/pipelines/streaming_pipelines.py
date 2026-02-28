import threading
import os
import time
from flask import current_app

from ..ingestion.file_listener import follow
from ..ingestion.parser import parse_log
from ..storage.redis_store import store_log
from ..processing.llm_worker import enqueue_log


def start_pipeline(app):

    def run():
        with app.app_context():

            log_file_path = current_app.config["LOG_FILE"]

            # Wait until file exists
            while not os.path.exists(log_file_path):
                print("Waiting for log file...")
                time.sleep(1)

            print("Log file found. Starting ingestion...")

            with open(log_file_path, "r") as f:

                # 🔹 STEP 1 — Read entire file once (historical load)
                for line in f:
                    try:
                        parsed = parse_log(line)
                        if parsed:
                            store_log(parsed)
                            enqueue_log(parsed)
                    except Exception as e:
                        print("Historical load error:", e)

                print("Historical logs loaded. Switching to streaming mode...")

                # 🔹 STEP 2 — Stream new lines
                for line in follow(f):
                    try:
                        parsed = parse_log(line)
                        if not parsed:
                            continue

                        store_log(parsed)
                        enqueue_log(parsed)

                    except Exception as e:
                        print("Streaming error:", e)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()