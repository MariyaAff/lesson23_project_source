from flask import Blueprint, jsonify, request
from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json

    validated_data = BatchRequestSchema().load(data)
    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=FILE_NAME,
            data=result,
        )

    return jsonify(result)
