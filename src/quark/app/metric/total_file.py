from dataclasses import dataclass
from quark.component.statistic.statistic import Statistic
from quark.template.metric.value import Value
from quark.service.attachment import AttachmentService

@dataclass
class TotalFile(Value):
    title: str = "文件数量"
    col: int = 6

    def calculate(self) -> Statistic:
        """计算数值"""
        count = AttachmentService().count_by_type("FILE")
        return (self
                .count(count)
                .set_value_style({"color": "#cf1322"}))