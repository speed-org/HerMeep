from flask import Response, stream_with_context
from src.core.schemes.generate import GenerateRequest
from ollama import chat, Message  # pyright: ignore[reportUnknownVariableType]  (ollama types `tools` loosely)
from src.config import Config
from src.constants import SYSTEM_PROMPT, APP_ROLE
from src.infrastructure.ports.cache import CacheABC
from src.core.helpers.llm import prepare_context_for_injection, prepare_selection_for_injection, stream_generation_helper
import logging

logger = logging.getLogger(__name__)


def generate_controller(data: GenerateRequest, cache: CacheABC)  -> Response:
    logger.info("new generation in progress")

    context = cache.get_cache(data.userAlias)

    messages = [
        Message(role=APP_ROLE.SYSTEM, content=SYSTEM_PROMPT),
        Message(role=APP_ROLE.USER, content=prepare_selection_for_injection(data.selection)),
    ]

    if context:
        messages.append(Message(role=APP_ROLE.USER, content=prepare_context_for_injection(context)))
        logger.info(f"{data.userAlias} context extracted and injected successfully!!!")

    logger.info("messages injected successfully")

    stream = chat(model=Config.MODEL_NAME, messages=messages, think=False, stream=True)

    logger.info(f"Translation generated successfully for {data.selection}")

    return Response(stream_with_context(stream_generation_helper(stream)), mimetype="text/plain")