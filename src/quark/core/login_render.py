from ..config import config
from flask import request

def index_render():
    resource = request.view_args.get('resource')
    return config["MODULE_PATH"]+resource