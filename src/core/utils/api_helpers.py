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
