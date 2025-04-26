from dataclasses import dataclass
from quark.template.layout import Layout

@dataclass
class Index(Layout):

    def __post_init__(self):
        return self