from dataclasses import dataclass
from typing import List, Any
from quark.template.dashboard import Dashboard
from quark.app.metric.total_admin import TotalAdmin
from quark.app.metric.total_file import TotalFile
from quark.app.metric.total_image import TotalImage
from quark.app.metric.total_log import TotalLog
from quark.app.metric.team_info import TeamInfo
from quark.app.metric.system_info import SystemInfo

@dataclass
class Index(Dashboard):
    title: str = "仪表盘"

    def cards(self) -> List[Any]:
        return [
            TotalAdmin(),
            TotalFile(),
            TotalImage(),
            TotalLog(),
            SystemInfo(),
            TeamInfo()
        ]