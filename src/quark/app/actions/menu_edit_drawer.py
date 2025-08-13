from typing import Any, Dict, List

from quark import Request
from quark.component.action.action import Action
from quark.component.form.form import Form
from quark.template.action import Drawer


class MenuEditDrawer(Drawer):
    def __init__(self, name: str, api: str, init_api: str, fields: Any):
        self.name = name
        self.api = api
        self.init_api = init_api
        self.fields = fields
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.Width = 750
        self.set_only_on_index_table_row(True)

    def get_body(self, request: Request) -> Dict[str, Any]:
        return (
            Form()
            .set_api(self.api)
            .set_init_api(self.init_api)
            .set_body(self.fields)
            .set_layout("vertical")
            .set_key("editDrawerForm", False)
        )

    def get_actions(self, ctx: Dict[str, Any]) -> List[Dict[str, Any]]:
        return [
            Action().set_label("取消").set_action_type("cancel"),
            Action()
            .set_submit_form("editDrawerForm")
            .set_label("提交")
            .set_with_loading(True)
            .set_reload("table")
            .set_action_type("submit")
            .set_type("primary", ghost=False),
        ]
