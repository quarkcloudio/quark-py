from dataclasses import dataclass
from quark.template.login import Login

@dataclass
class Index(Login):
    def index_render(self):
        return "xyz1"