from flask import request, Blueprint, jsonify

from document_parser.predict import make_prediction
from document_parser.utils import save_document_parse_data
from document_parser.validation import _validate_check_resume_request

document_api = Blueprint('account_api', __name__)


@document_api.route('/check/resume', methods=['POST'])
def check_document_resume_or_not():
    file_url, extension = _validate_check_resume_request(request)
    result = make_prediction(file_url, extension)
    data = {
        "fileUrl": file_url,
        "ext": extension,
        "isResume": result
    }
    save_document_parse_data(file_url, extension, is_resume=result)
    return jsonify(data)
