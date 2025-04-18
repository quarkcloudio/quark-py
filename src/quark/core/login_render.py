from quark.config import config

def index_render(resource: str):
    return config["MODULE_PATH"]+resource