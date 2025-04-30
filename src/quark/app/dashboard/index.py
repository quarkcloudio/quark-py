from dataclasses import dataclass
from typing import List, Any
from quark.template.dashboard import Dashboard
from quark.app.metric.total_admin import TotalAdmin
from quark.app.metric.total_file import TotalFile
from quark.app.metric.total_image import TotalImage
from quark.app.metric.total_log import TotalLog

@dataclass
class Index(Dashboard):
    title: str = "仪表盘"

    def cards(self) -> List[Any]:
        return [
            TotalAdmin(),
            TotalFile(),
            TotalImage(),
            TotalLog()
        ]