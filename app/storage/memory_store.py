logs = []
anomalies = []

def store_log(log):
    logs.append(log)

def store_anomaly(log):
    anomalies.append(log)

def get_recent_logs(n=20):
    return logs[-n:]

def get_recent_anomalies(n=10):
    return anomalies[-n:]