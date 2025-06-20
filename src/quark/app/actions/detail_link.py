from typing import Any, Optional
from app.core.context import Context
from app.template.admin.resource.actions import Link


class DetailLinkAction(Link):
    def __init__(self, name: Optional[str] = None):
        super().__init__()
        self.name = name or "详情"
        self.type = "link"
        self.size = "small"
        self.set_only_on_index_table_row(True)

    def init(self, ctx: Context) -> Any:
        # 初始化按钮属性（如果需要额外初始化逻辑，可以写这里）
        return self

    def get_href(self, ctx: Context) -> str:
        # 替换路径中的 "/index" 为 "/detail&id=${id}"
        path = ctx.path
        href = path.replace("/index", "/detail&id=${id}")
        return f"#/layout/index?api={href}"
