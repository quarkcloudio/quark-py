from quark.component.statistic.statistic import Statistic
from quark.template.metric.value import Value
from quark.services.attachment import AttachmentService


class TotalFile(Value):
    title: str = "文件数量"
    col: int = 6

    async def calculate(self) -> Statistic:
        """计算数值"""
        count = await AttachmentService().count_by_type("FILE")
        return self.count(count).set_value_style({"color": "#cf1322"})
