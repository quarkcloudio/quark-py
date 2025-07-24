from pydantic import model_validator
from quark import Layout


class Index(Layout):
    """后台布局"""

    @model_validator(mode="after")
    def init(self):
        return self
