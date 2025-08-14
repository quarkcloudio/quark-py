from typing import Any, Optional

from quark import Request
from quark.template.action import Link


class DetailLink(Link):

    def __init__(self, name: Optional[str] = None):
        self.name = name or "详情"
        self.type = "link"
        self.size = "small"
        self.set_only_on_index_table_row(True)

    def init(self, request: Request) -> Any:
        # 初始化按钮属性（如果需要额外初始化逻辑，可以写这里）
        return self

    async def get_href(self, request: Request) -> str:
        # 替换路径中的 "/index" 为 "/detail&id=${id}"
        href = request.url.path.replace("/index", "/detail&id=${id}")
        return f"#/layout/index?api={href}"
