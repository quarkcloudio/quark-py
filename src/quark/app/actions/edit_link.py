from typing import Optional

from quark import Request
from quark.template.action import Link


class EditLink(Link):

    def __init__(self, name: Optional[str] = None):
        self.name = name or "编辑"
        self.type = "link"
        self.size = "small"
        self.set_only_on_index_table_row(True)

    async def get_href(self, request: Request) -> str:
        # 替换路径中的 /index 为 /edit&id=${id}
        href = request.url.path.replace("/index", "/edit&id=${id}")
        return f"#/layout/index?api={href}"
