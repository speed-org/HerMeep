from flask import Blueprint, request, make_response, Response
from typing import Any

from src.core.schemes.generate import GenerateRequest, InjectRequest
from src.core.factories.cache_factory import CacheFactory
from src.constants import CACHE_TYPE
from src.core.helpers.llm import generate_schema_from_request
from src.core.controllers.llm import generate_controller
import logging

llm_bp = Blueprint('llm', __name__, url_prefix='/llm')
cache = CacheFactory().get_instance(CACHE_TYPE.LOCAL)
logger = logging.getLogger(__name__)

@llm_bp.route('/status')
def llm_status():
    return {"status": "ok"}, 200

@llm_bp.route('/generate', methods=['POST'])
def generate_translation() -> Any:
    logger.info("Generate Endpoint hit, starting process")

    data = generate_schema_from_request(request, Schema=GenerateRequest)
    return generate_controller(data, cache)

    

@llm_bp.route("/inject", methods=["POST"])
def inject_context() -> Response:
    data = generate_schema_from_request(request, Schema=InjectRequest)


    cache.set_cache(data.userAlias, data.context)

    return make_response({"newCache":cache.get_cache(data.userAlias)}, 200)
