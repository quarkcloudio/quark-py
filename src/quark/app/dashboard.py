from typing import Any, List

from quark import Dashboard, Request
from quark.app.metrics.system_info import SystemInfo
from quark.app.metrics.team_info import TeamInfo
from quark.app.metrics.total_admin import TotalAdmin
from quark.app.metrics.total_file import TotalFile
from quark.app.metrics.total_image import TotalImage
from quark.app.metrics.total_log import TotalLog


class Index(Dashboard):
    """仪表盘"""

    async def init(self, request: Request):
        self.title = "仪表盘"
        return self

    async def cards(self, request: Request) -> List[Any]:
        return [
            TotalAdmin(),
            TotalFile(),
            TotalImage(),
            TotalLog(),
            SystemInfo(),
            TeamInfo(),
        ]
