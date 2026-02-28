import redis
import json
from flask import current_app

def get_client():
    return redis.Redis.from_url(current_app.config["REDIS_URL"], decode_responses=True)

def store_log(log):
    r = get_client()
    r.lpush("logs", json.dumps(log))
    r.ltrim("logs", 0, 999)

def store_anomaly(log):
    r = get_client()
    r.lpush("anomalies", json.dumps(log))
    r.ltrim("anomalies", 0, 199)

def get_logs(limit=20):
    r = get_client()
    logs = r.lrange("logs", 0, limit-1)
    return [json.loads(l) for l in logs]

def get_anomalies(limit=10):
    r = get_client()
    logs = r.lrange("anomalies", 0, limit-1)
    return [json.loads(l) for l in logs]