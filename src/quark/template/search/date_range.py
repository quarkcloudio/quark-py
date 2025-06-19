from pydantic import model_validator
from .search import Search


class DateRange(Search):
    """日期范围组件"""

    @model_validator(mode="after")
    def init(self):
        self.component = "dateRangeField"
        return self
