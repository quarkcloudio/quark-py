from ..config import config

def index_render(resource: str):
    return config["MODULE_PATH"]+resource

def action_render():
    return "index"