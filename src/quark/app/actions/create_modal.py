from typing import Any

from quark import Request
from quark.component.action.action import Action
from quark.component.form.form import Form
from quark.template.action import Modal
from quark.template.resolves_fields import ResolvesFields


class CreateModal(Modal):

    def __init__(self, resource: Any):
        self.resource = resource
        self.name = "创建" + resource.title
        self.type = "primary"
        self.icon = "plus-circle"
        self.reload = "table"
        self.destroy_on_close = True
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
            .set_style(
                {
                    "paddingTop": "24px",
                }
            )
            .set_api(api)
            .set_body(fields)
            .set_initial_values(data)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
            .set_key("createModalForm", False)
        )

    async def get_actions(self, request: Request):
        return [
            Action().set_label("取消").set_action_type("cancel"),
            Action()
            .set_submit_form("createModalForm")
            .set_label("提交")
            .set_with_loading(True)
            .set_reload("table")
            .set_action_type("submit")
            .set_type("primary", False),
        ]
