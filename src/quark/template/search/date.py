from .search import Search


class Date(Search):
    """日期组件"""

    def __init__(self, column: str = "", name: str = ""):
        self.component = "dateField"
        return self
