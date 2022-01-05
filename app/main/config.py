import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

class Config:
    FLASK_APP = os.environ.get("FLASK_APP")
    TITLE = os.environ.get("TITLE")
    VERSION = os.environ.get("VERSION")
    DESCRIPTION = os.environ.get("DESCRIPTION")
    DEBUG = True
    SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post"]
    CONFIG_DOC = os.environ.get("DOC")
    DOC = True if CONFIG_DOC == 'true' else False
