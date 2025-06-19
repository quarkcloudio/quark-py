from typing import List, Any
from pydantic import model_validator
from fastapi import Request
from quark.template.dashboard import Dashboard
from quark.app.metrics.total_admin import TotalAdmin
from quark.app.metrics.total_file import TotalFile
from quark.app.metrics.total_image import TotalImage
from quark.app.metrics.total_log import TotalLog
from quark.app.metrics.team_info import TeamInfo
from quark.app.metrics.system_info import SystemInfo


class Index(Dashboard):
    """仪表盘"""

    @model_validator(mode="after")
    def init(self):
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
