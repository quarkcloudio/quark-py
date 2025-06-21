from typing import Any
from quark import Request
from quark.template.action import Drawer
from quark.component.form.form import Form
from quark.component.action.action import Action


class CreateDrawer(Drawer):
    def __init__(self, title: str, api: str, fields: Any, initial_data: dict):
        self.name = "创建" + title
        self.api = api
        self.fields = fields
        self.initial_data = initial_data
        self.type = "primary"
        self.icon = "plus-circle"
        self.reload = "table"
        self.destroy_on_close = True
        self.set_only_on_index(True)

    def get_body(self, request: Request):
        return (
            Form()
            .set_api(self.api)
            .set_body(self.fields)
            .set_initial_values(self.initial_data)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
            .set_key("createDrawerForm", destroy=False)
        )

    def get_actions(self, request: Request):
        return [
            Action().set_label("取消").set_action_type("cancel"),
            Action()
            .set_submit_form("createDrawerForm")
            .set_label("提交")
            .set_with_loading(True)
            .set_reload("table")
            .set_action_type("submit")
            .set_type("primary", ghost=False),
        ]
