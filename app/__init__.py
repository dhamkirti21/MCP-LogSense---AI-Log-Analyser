from flask import Flask,render_template
from .config import Config
from .pipelines.streaming_pipelines import start_pipeline
from .processing.llm_worker import start_llm_worker

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .api.routes import api_bp
    app.register_blueprint(api_bp)
    @app.route("/")
    def dashboard():
        return render_template("dashboard.html")

    start_pipeline(app)
    start_llm_worker(app)

    return app