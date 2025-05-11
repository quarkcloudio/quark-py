from dataclasses import dataclass
from ...component.statistic.statistic import Statistic

@dataclass
class Value:
    title: str = None
    col: int = None
    precision: int = None

    # 记录条数
    def count(self, value: int) -> Statistic:
        return self.result(value)

    # 包含组件的结果
    def result(self, value: int) -> Statistic:
        return Statistic().set_title(self.title).set_value(value)