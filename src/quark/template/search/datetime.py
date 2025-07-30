from .search import Search


class Datetime(Search):
    """日期组件"""

    def __init__(self, column: str = "", name: str = ""):
        self.component = "datetimeField"
        return self
