from flask import Request
from typing import Callable, Any
from src.core.exceptions.schema import RequestSchemaError

def generate_schema_from_request[T](request: Request, Schema: Callable[..., T]) -> T:
    try:
        req_data:dict[str, Any] = request.get_json()  or {}
        data = Schema(**req_data)
        return data
        
    except Exception as e:
        raise RequestSchemaError from e

def prepare_context_for_injection(context: str) -> str:
    return f"""
        Context:
        ```txt
        {context}
        ```
    """

def prepare_selection_for_injection(selection: str) -> str:
    return f"""
        Selection:
        ```txt
        {selection}
        ```
    """


def stream_generation_helper(stream: Any):
    for chunk in stream:
        yield chunk.message.content