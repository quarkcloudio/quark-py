from pydantic import model_validator
from quark.template.layout import Layout


class Index(Layout):
    """后台布局"""

    @model_validator(mode="after")
    def init(self):
        return self
