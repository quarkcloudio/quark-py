from typing import Any

from tortoise.models import Model

from quark import Request

from .search import Search


class Input(Search):
    """输入框组件"""

    component = "inputField"

    def __init__(self, column: str = "", name: str = ""):
        self.column = column
        self.name = name

    def apply(self, request: Request, query: Model, value: Any) -> Model:
        """执行查询逻辑，子类可重写此方法"""
        return query.filter(**{f"{self.column}__icontains": value})
