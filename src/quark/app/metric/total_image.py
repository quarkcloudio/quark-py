from dataclasses import dataclass
from quark.component.statistic.statistic import Component as StatisticComponent
from quark.template.metric.value import Value

@dataclass
class TotalImage(Value):
    title: str = "图片数量"
    col: int = 6

    def calculate(self) -> StatisticComponent:
        """计算数值"""
        return (self
                .count(10)
                .set_value_style({"color": "#cf1322"}))