from typing import Any
from fastapi import Request
from tortoise.models import Model
from quark.template.search import DatetimeRange


class DatetimeRange(DatetimeRange):
    """日期范围组件"""

    def __init__(self, column: str = "", name: str = ""):
        self.column = column
        self.name = name

    def apply(self, request: Request, query: Model, value: Any) -> Model:
        filters = {
            f"{self.column}__gte": value[0],
            f"{self.column}__lte": value[1],
        }
        return query.filter(**filters)
