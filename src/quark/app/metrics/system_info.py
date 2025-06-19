import platform
import psutil
import sys
from quark.component.descriptions.fields.text import Text
from quark.template.metric.descriptions import Descriptions


class SystemInfo(Descriptions):
    title: str = "系统信息"
    col: int = 12

    async def calculate(self) -> any:
        memory = psutil.virtual_memory()
        cpu_percent = psutil.cpu_percent(interval=1)
        return self.result(
            [
                Text().set_label("应用名称").set_value("QuarkPy"),
                Text().set_label("应用版本").set_value("v0.0.1"),
                Text().set_label("Python版本").set_value(sys.version.split(" ")[0]),
                Text()
                .set_label("服务器操作系统")
                .set_value(f"{platform.system()} {platform.machine()}"),
                Text()
                .set_label("内存信息")
                .set_value(f"{memory.total // (1024 * 1024)}MB / {memory.percent}%"),
                Text().set_label("CPU使用率").set_value(f"{cpu_percent}%"),
            ]
        )
