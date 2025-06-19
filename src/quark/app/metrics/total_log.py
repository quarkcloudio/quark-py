from quark.component.statistic.statistic import Statistic
from quark.template.metric.value import Value
from quark.services.action_log import ActionLogService


class TotalLog(Value):
    title: str = "日志数量"
    col: int = 6

    async def calculate(self) -> Statistic:
        """计算数值"""
        count = await ActionLogService().count()
        return self.count(count).set_value_style({"color": "#999999"})
