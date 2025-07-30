from typing import Any
from quark import Request
from tortoise.models import Model
from quark.template.search import Select


class Status(Select):
    """状态组件"""

    def __init__(self):
        super().__init__("status", "状态")

    def apply(self, request: Request, query: Model, value: Any) -> Model:
        return query.filter(**{f"{self.column}": value})

    def options(self, request: Request):
        return [
            self.option("正常", 1),
            self.option("禁用", 0),
        ]
