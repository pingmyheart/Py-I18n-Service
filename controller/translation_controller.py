from flask import Blueprint, jsonify, request

from configuration.logging_configuration import logger as log
from enumeration.response_code_enum import ResponseCodeEnum
from service import translation_service_bean

translation_bp = Blueprint('translation', __name__, url_prefix='/py-i18n-service/translation')


@translation_bp.route('', methods=['GET'])
def retrieve_translation():
    log.info("[INCOMING REQUEST] - Retrieve translation")
    log.info(request.args)
    key = request.args.get('key')
    language = request.args.get('language')
    service_response = translation_service_bean.translate(key=key,
                                                          language=language)
    return (jsonify(service_response.dict(exclude_none=True)),
            ResponseCodeEnum.get_by_code(service_response.response_code).http_status_code)
