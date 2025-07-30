from typing import Any
from fastapi import Request
from tortoise.models import Model
from quark.template.search import Search


class Input(Search):
    """输入框组件"""

    def __init__(self, column: str = "", name: str = ""):
        self.column = column
        self.name = name

    def apply(self, request: Request, query: Model, value: Any) -> Model:
        return query.filter(**{f"{self.column}__icontains": value})
