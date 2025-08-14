from typing import Optional

from quark import Request
from quark.services.auth import AuthService


class Export:
    def __init__(self, name: Optional[str] = None):
        self.name = name or "导出"
        self.type = "link"
        self.size = "small"
        self.target = "_blank"
        self.only_on_index_table_row = True

    async def get_href(self, request: Request) -> str:
        token = AuthService(request).get_token()
        return request.url.path.replace("/index", f"/export?id=${{id}}&token={token}")
