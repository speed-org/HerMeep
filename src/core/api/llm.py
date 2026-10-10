from flask import Blueprint, request, make_response, Response
from ollama import chat, Message  # pyright: ignore[reportUnknownVariableType]  (ollama types `tools` loosely)
from typing import Any

from src.config import Config
from src.core.schemes.generate import GenerateRequest, InjectRequest
from src.constants import SYSTEM_PROMPT, APP_ROLE
from src.core.factories.cache_factory import CacheFactory
from src.constants import CACHE_TYPE
from src.core.utils.api_helpers import generate_schema_from_request

llm_bp = Blueprint('llm', __name__, url_prefix='/llm')
_cache = CacheFactory().get_instance(CACHE_TYPE.LOCAL)

@llm_bp.route('/status')
def llm_status():
    return {"status": "ok"}, 200

@llm_bp.route('/generate', methods=['POST'])
def generate_translation() -> Any:
    data = generate_schema_from_request(request, Schema=GenerateRequest)

    messages = [
        Message(role=APP_ROLE.SYSTEM, content=SYSTEM_PROMPT),
        Message(role=APP_ROLE.USER, content=data.selection),
    ]

    resp = chat(model=Config.MODEL_NAME, messages=messages, think=False)

    return make_response({"resp": resp.message.content}, 200)

@llm_bp.route("/inject", methods=["POST"])
def inject_context() -> Response:
    data = generate_schema_from_request(request, Schema=InjectRequest)


    _cache.set_cache(data.userAlias, data.context)

    return make_response({"newCache":_cache.get_cache(data.userAlias)}, 200)
