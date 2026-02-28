from ..storage.redis_store import get_logs, get_anomalies
from ..monitoring.metrics import get_metrics

def recent_logs(limit: int = 10):
    return get_logs(limit)

def recent_anomalies(limit: int = 5):
    return get_anomalies(limit)

def system_metrics():
    return get_metrics()