from dataclasses import dataclass
from quark.component.statistic.statistic import Component as StatisticComponent
from quark.template.metric.value import Value
from quark.service.action_log import ActionLogService

@dataclass
class TotalLog(Value):
    title: str = "日志数量"
    col: int = 6

    def calculate(self) -> StatisticComponent:
        """计算数值"""
        count = ActionLogService().count()
        return (self
                .count(count)
                .set_value_style({"color": "#999999"}))