from flask import Flask
from src.core.api.llm import llm_bp
from src.core.handlers.error_handlers import register_error_handlers

def generate_app():
    app = Flask(__name__)
    app.register_blueprint(llm_bp)
    register_error_handlers(app)

    app.json.ensure_ascii = False

    return app