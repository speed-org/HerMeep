from flask import Blueprint, request, make_response, Response
from ollama import chat, Message  # pyright: ignore[reportUnknownVariableType]  (ollama types `tools` loosely)
from typing import Any

from src.config import Config
from src.schemes.generate import GenerateRequest
from src.constants import SYSTEM_PROMPT, APP_ROLE

llm_bp = Blueprint('llm', __name__, url_prefix='/llm')


@llm_bp.route('/status')
def llm_status():
    return {"status": "ok"}, 200

@llm_bp.route('/generate', methods=['POST'])
def generate_translation() -> Any:
    req_data = request.get_json()
    data = GenerateRequest(**req_data)

    messages = [
        Message(role=APP_ROLE.SYSTEM, content=SYSTEM_PROMPT),
        Message(role=APP_ROLE.USER, content=data.selection),
    ]

    resp = chat(model=Config.MODEL_NAME, messages=messages, think=False)

    return make_response({"resp": resp.message.content}, 200)

@llm_bp.route("/inject", methods=["POST"])
def inject_context() -> Response:
    return make_response({}, 200)
