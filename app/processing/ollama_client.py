import requests
import json
from flask import current_app

def analyze_log(log):
    prompt = f"""
Return JSON only:
{{
 "severity": "low|medium|high|critical",
 "anomaly": true|false,
 "reason": "short explanation"
}}

Log:
{log}
"""

    response = requests.post(
        current_app.config["OLLAMA_URL"],
        json={
            "model": current_app.config["MODEL_NAME"],
            "prompt": prompt,
            "stream": False
        },
        timeout=15
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except:
        return {
            "severity": "unknown",
            "anomaly": False,
            "reason": "Invalid LLM response"
        }