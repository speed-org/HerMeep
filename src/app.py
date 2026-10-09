from flask import Flask
from src.api.llm import llm_bp

def generate_app():
    app = Flask(__name__)
    app.register_blueprint(llm_bp)
    app.json.ensure_ascii = False

    return app