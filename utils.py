import os
import re
import shutil
import tempfile
import time
import unicodedata

import gdown
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

from document_parser import constants

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def save_document_parse_data(fileUrl, ext, is_resume=None, error=False, message=None, **kwargs):
    from main import db_for_read

    document = {
        "fileUrl": fileUrl,
        "ext": ext,
        "error": error,
        "message": message,
        "updatedAt": time.time() * 1000,
        "createdAt": time.time() * 1000
    }
    if not error:
        document["category"] = 1 if is_resume else 0

    db_for_read.documentParsedEntity.insert_one(document)


def preprocess_text(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("   ", "\n")
    text = text.replace("\t\t", "\n")
    text = text.replace("\t", " ")
    text = re.sub('[:|;,_"-]+', ' ', text)

    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text


def detect_model_version():
    if not os.path.exists(constants.MODEL_ABSOLUTE_PATH):
        print(f"New Model version {constants.MODEL_VERSION} detected")
        print("Downloading document classification model ................")
        temp_file_path = tempfile.NamedTemporaryFile(prefix=constants.MODEL_DIRECTORY_NAME, suffix='.zip')
        model_zip_file_path = gdown.download(constants.MODEL_URL, temp_file_path.name, quiet=True)
        if model_zip_file_path is None:
            raise ValueError("Could not download new version of model")

        print("Model has been downloaded")
        print("Unpacking document classification model")
        shutil.unpack_archive(model_zip_file_path, constants.MODEL_ABSOLUTE_PATH)
        print(f"Model has been unpacked at location {constants.MODEL_ABSOLUTE_PATH} in system")
    else:
        print("NO model upgrade version detected")

    return constants.MODEL_ABSOLUTE_PATH
