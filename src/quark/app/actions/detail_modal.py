from typing import Any
from app.core.context import Context
from app.template.admin.resource.actions import Modal
from app.template.admin.resource.types import Resourcer


class DetailModalAction(Modal):
    def __init__(self, name: str = "详情"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.width = 750
        self.set_only_on_index_table_row(True)

    def init(self, ctx: Context) -> Any:
        # 这里通常 init 处理初始化逻辑，构造函数已初始化属性
        return self

    def get_body(self, ctx: Context) -> Any:
        template: Resourcer = ctx.template
        init_api = template.detail_value_api(ctx)
        component = template.detail_fields_within_components(ctx, init_api, None)
        return component
