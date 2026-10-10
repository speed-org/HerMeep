from flask import Flask, jsonify
from ..exceptions.schema import RequestSchemaError

def register_error_handlers(app: Flask):
    @app.errorhandler(RequestSchemaError)
    def handle_schema_error(error: RequestSchemaError):
        return jsonify({
            "message": "The request body doesn't have the structure agreed in the schema"
        }), 400