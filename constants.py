import glob
import os
from enum import Enum

MODEL_VERSION = "1.0.0"
MODEL_PREFIX = "outputs_v_"
MODEL_DIRECTORY_NAME = MODEL_PREFIX + MODEL_VERSION
MODEL_ABSOLUTE_PATH = os.path.join(os.getcwd(), 'document_parser/model/' + MODEL_DIRECTORY_NAME)

MODEL_URL = "https://drive.google.com/uc?id=1-F89GeORAOe53r0jB-fsP0ypUIKEkCfY"


# MODEL_OUTPUTS = os.path.join(os.getcwd(), "document_parser/model/")


class DocumentCategory(Enum):
    RESUME = 1
    OTHER = 0
