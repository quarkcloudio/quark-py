from typing import Any
from app.core.context import Context
from app.template.admin.resource.actions import Drawer
from app.template.admin.resource.types import Resourcer


class DetailDrawerAction(Drawer):
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
        # 这里通常 init 方法设置按钮样式等，已在构造函数完成
        return self

    def get_body(self, ctx: Context) -> Any:
        # 获取模板资源接口实例
        template: Resourcer = ctx.template

        # 详情页面数据接口地址
        init_api = template.detail_value_api(ctx)

        # 获取详情页面内嵌组件字段
        component = template.detail_fields_within_components(ctx, init_api, None)

        return component
