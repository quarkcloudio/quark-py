from dataclasses import dataclass
from quark.component.statistic.statistic import Component as StatisticComponent
from quark.template.metric.value import Value
from quark.service.attachment import AttachmentService

@dataclass
class TotalImage(Value):
    title: str = "图片数量"
    col: int = 6

    def calculate(self) -> StatisticComponent:
        """计算数值"""
        count = AttachmentService().count_by_type("IMAGE")
        return (self
                .count(count)
                .set_value_style({"color": "#cf1322"}))