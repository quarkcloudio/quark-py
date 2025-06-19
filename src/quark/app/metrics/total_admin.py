from quark.component.statistic.statistic import Statistic
from quark.template.metric.value import Value
from quark.services.user import UserService


class TotalAdmin(Value):
    title: str = "用户数量"
    col: int = 6

    async def calculate(self) -> Statistic:
        """计算数值"""
        count = await UserService().count()
        return self.count(count).set_value_style({"color": "#3f8600"})
