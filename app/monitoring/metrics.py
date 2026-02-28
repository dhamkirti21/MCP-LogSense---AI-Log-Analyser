from ..storage.redis_store import get_logs, get_anomalies

def get_metrics():
    logs = get_logs(1000)
    anomalies = get_anomalies(1000)

    error_count = sum(1 for l in logs if l["level"] == "ERROR")

    return {
        "total_logs": len(logs),
        "total_anomalies": len(anomalies),
        "error_rate": error_count / max(len(logs), 1)
    }