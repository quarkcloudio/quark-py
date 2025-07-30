from .search import Search


class DatetimeRange(Search):
    """日期组件"""

    component = "datetimeRangeField"

    def __init__(self, column: str = "", name: str = ""):
        self.component = "datetimeRangeField"
        return self
