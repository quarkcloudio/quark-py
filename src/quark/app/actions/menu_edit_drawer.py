from typing import Any, List

from quark import Request
from quark.component.action.action import Action
from quark.component.form.form import Form
from quark.template.action import Drawer
from quark.template.resolves_fields import ResolvesFields


class MenuEditDrawer(Drawer):

    def __init__(self, resource: Any):
        self.resource = resource
        self.name = "编辑"
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.width = 750
        self.set_only_on_index_table_row(True)

    async def get_body(self, request: Request) -> Any:
        api = await self.resource.update_api(request)
        init_api = await self.resource.edit_value_api(request)
        fields = ResolvesFields(
            request=request,
            fields=await self.resource.fields(request),
        ).update_fields_within_components()

        return (
            Form()
            .set_api(api)
            .set_init_api(init_api)
            .set_body(fields)
            .set_layout("vertical")
            .set_key("editDrawerForm", False)
        )

    async def get_actions(self, request: Request) -> List[Any]:
        return [
            Action().set_label("取消").set_action_type("cancel"),
            Action()
            .set_submit_form("editDrawerForm")
            .set_label("提交")
            .set_with_loading(True)
            .set_reload("table")
            .set_action_type("submit")
            .set_type("primary", False),
        ]
