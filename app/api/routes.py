from flask import Blueprint, jsonify
from ..storage.redis_store import get_logs, get_anomalies
from ..monitoring.metrics import get_metrics
from ..monitoring.healthcheck import health

api_bp = Blueprint("api", __name__)

@api_bp.route("/logs")
def logs():
    return jsonify(get_logs())

@api_bp.route("/anomalies")
def anomalies():
    return jsonify(get_anomalies())

@api_bp.route("/metrics")
def metrics():
    return jsonify(get_metrics())

@api_bp.route("/health")
def healthcheck():
    return jsonify(health())