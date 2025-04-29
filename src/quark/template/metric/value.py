from dataclasses import dataclass
from ...component.statistic.statistic import Component as StatisticComponent

@dataclass
class Value:
    title: str = None
    col: int = None
    precision: int = None

    # 记录条数
    def count(self) -> StatisticComponent:
        return 10

    # 包含组件的结果
    def result(self, value: int) -> StatisticComponent:
        return StatisticComponent().set_title(self.title).set_value(value)