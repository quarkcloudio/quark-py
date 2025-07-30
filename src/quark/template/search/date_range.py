from .search import Search


class DateRange(Search):
    """日期范围组件"""

    def __init__(self, column: str = "", name: str = ""):
        self.component = "dateRangeField"
        return self
