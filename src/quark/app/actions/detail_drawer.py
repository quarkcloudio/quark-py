from typing import Any

from quark import Request
from quark.template.action import Drawer


class DetailDrawer(Drawer):

    def __init__(self, name: str, detail_component: Any):
        self.name = name
        self.detail_component = detail_component
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.width = 750
        self.set_only_on_index_table_row(True)

    def init(self, request: Request) -> Any:
        # 这里通常 init 方法设置按钮样式等，已在构造函数完成
        return self

    async def get_body(self, request: Request) -> Any:
        return self.detail_component
