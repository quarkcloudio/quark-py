from dataclasses import dataclass
from quark.template.dashboard import Dashboard

@dataclass
class Index(Dashboard):

    def __post_init__(self):
        return self