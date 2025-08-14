from typing import Any

from quark import Request
from quark.template.action import Modal


class DetailModal(Modal):

    def __init__(self, name: str, detail_component: Any):
        self.name = name
        self.detail_component = detail_component
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.width = 750
        self.set_only_on_index_table_row(True)

    async def get_body(self, request: Request) -> Any:
        return self.detail_component
