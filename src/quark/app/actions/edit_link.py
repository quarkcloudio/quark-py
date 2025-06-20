from typing import Any, Optional
from app.core.context import Context
from app.template.admin.resource.actions import Link


class EditLinkAction(Link):
    def __init__(self, name: Optional[str] = None):
        super().__init__()
        self.name = name or "编辑"
        self.type = "link"
        self.size = "small"
        self.set_only_on_index_table_row(True)

    def init(self, ctx: Context) -> Any:
        # 可添加初始化逻辑，这里直接返回自己
        return self

    def get_href(self, ctx: Context) -> str:
        # 替换路径中的 /index 为 /edit&id=${id}
        path = ctx.path
        href = path.replace("/index", "/edit&id=${id}")
        return f"#/layout/index?api={href}"
