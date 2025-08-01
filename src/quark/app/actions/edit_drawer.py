from typing import Any, List
from quark import Request
from quark.template.action import Drawer
from quark.component.form.form import Form
from quark.component.action.action import Action


class EditDrawer(Drawer):
    def __init__(self, name: str, api: str, init_api: str, fields: Any):
        self.name = name
        self.api = api
        self.init_api = init_api
        self.fields = fields
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.set_only_on_index_table_row(True)

    def get_body(self, request: Request) -> Any:
        return (
            Form()
            .set_api(self.api)
            .set_init_api(self.init_api)
            .set_body(self.fields)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
            .set_key("editDrawerForm", False)
        )

    def get_actions(self, request: Request) -> List[Any]:
        return [
            (Action().set_label("取消").set_action_type("cancel")),
            (
                Action()
                .set_label("提交")
                .set_with_loading(True)
                .set_reload("table")
                .set_action_type("submit")
                .set_type("primary", False)
                .set_submit_form("editDrawerForm")
            ),
        ]
