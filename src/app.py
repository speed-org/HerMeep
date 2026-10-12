from flask import Flask
from src.core.api.llm import llm_bp
from src.core.handlers.error_handlers import register_error_handlers
import logging

def generate_app():
    app = Flask(__name__)
    app.register_blueprint(llm_bp)
    register_error_handlers(app)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    app.json.ensure_ascii = False

    return app