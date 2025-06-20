from typing import Any, List
from app.core.context import Context
from app.template.admin.resource.actions import Drawer
from app.template.admin.resource.types import Resourcer
from app.template.admin.component import form, action


class EditDrawerAction(Drawer):
    def __init__(self, name: str = "编辑"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.set_only_on_index_table_row(True)

    def init(self, ctx: Context) -> Any:
        # 这里通常可写额外初始化逻辑
        return self

    def get_body(self, ctx: Context) -> Any:
        template: Resourcer = ctx.template

        api = template.update_api(ctx)
        init_api = template.edit_value_api(ctx)
        fields = template.update_fields_within_components(ctx)

        return (
            form.Component()
            .init()
            .set_key("editDrawerForm", False)
            .set_api(api)
            .set_init_api(init_api)
            .set_body(fields)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
        )

    def get_actions(self, ctx: Context) -> List[Any]:
        return [
            (action.Component().init().set_label("取消").set_action_type("cancel")),
            (
                action.Component()
                .init()
                .set_label("提交")
                .set_with_loading(True)
                .set_reload("table")
                .set_action_type("submit")
                .set_type("primary", False)
                .set_submit_form("editDrawerForm")
            ),
        ]
