from pydantic import model_validator
from .search import Search


class DatetimeRange(Search):
    """日期组件"""

    @model_validator(mode="after")
    def init(self):
        self.component = "datetimeRangeField"
        return self
