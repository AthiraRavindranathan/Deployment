from cloud import download_file_from_url
# from document_parser import trained_model
from document_parser.constants import DocumentCategory
from document_parser.utils import preprocess_text, save_document_parse_data
from pyresparser.utils import extract_text, delete_file


def make_prediction(file_url, extension):
    try:
        file_path = download_file_from_url(file_url, "." + extension)
        text = extract_text(file_path, "." + extension)
    except ValueError as e:
        save_document_parse_data(file_url, extension, error=True, message=str(e))
        raise ValueError(str(e))

    delete_file(file_path)
    # prediction, raw_outputs = trained_model.predict([preprocess_text(text)])
    # return True if prediction[0] == DocumentCategory.RESUME.value else False
