from typing import Any, Dict, List

from quark import Request
from quark.component.action.action import Action
from quark.component.form.form import Form
from quark.template.action import Drawer
from quark.template.resolves_fields import ResolvesFields


class MenuCreateDrawer(Drawer):

    def __init__(self, resource: Any):

        # 资源
        self.resource = resource

        # 名称
        self.name = "创建" + resource.title

        # 类型
        self.type = "primary"

        # 图标
        self.icon = "plus-circle"

        # 执行成功后刷新的组件
        self.reload = "table"

        # 关闭时销毁 Drawer 里的子元素
        self.destroy_on_close = True

        # 抽屉弹出层宽度
        self.width = 750

        # 设置展示位置（只在列表页显示）
        self.set_only_on_index(True)

    async def get_body(self, request: Request):
        api = await self.resource.creation_api(request)
        fields = ResolvesFields(
            request=request,
            fields=await self.resource.fields(request),
        ).creation_fields_within_components()
        data = await self.resource.before_creating(request)
        return (
            Form()
            .set_api(api)
            .set_body(fields)
            .set_initial_values(data)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
            .set_key("createDrawerForm", False)
        )

    async def get_actions(self, request: Request):
        return [
            Action().set_label("取消").set_action_type("cancel"),
            Action()
            .set_submit_form("createDrawerForm")
            .set_label("提交")
            .set_with_loading(True)
            .set_reload("table")
            .set_action_type("submit")
            .set_type("primary", False),
        ]
