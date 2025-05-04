from dataclasses import dataclass
from quark.component.statistic.statistic import Statistic
from quark.template.metric.value import Value
from quark.service.user import UserService

@dataclass
class TotalAdmin(Value):
    title: str = "用户数量"
    col: int = 6

    def calculate(self) -> Statistic:
        """计算数值"""
        count = UserService().count()
        return (self
                .count(count)
                .set_value_style({"color": "#3f8600"}))