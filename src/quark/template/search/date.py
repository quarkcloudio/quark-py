from pydantic import model_validator
from .search import Search


class Date(Search):
    """日期组件"""

    @model_validator(mode="after")
    def init(self):
        self.component = "dateField"
        return self
