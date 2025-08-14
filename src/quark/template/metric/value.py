from typing import Optional

from pydantic import BaseModel

from ...component.statistic.statistic import Statistic


class Value(BaseModel):
    title: Optional[str] = None
    col: Optional[int] = None
    precision: Optional[int] = None

    # 记录条数
    def count(self, value: int) -> Statistic:
        return self.result(value)

    # 包含组件的结果
    def result(self, value: int) -> Statistic:
        return Statistic().set_title(self.title).set_value(value)
