from typing import Any, List, Optional

# 假设这些是你自定义的组件基类
from app.template.admin.resource.actions import Modal
from app.template.admin.component import action as action_comp
from app.template.admin.component import form as form_comp
from app.template.admin.resource import types
from app.core.context import Context


class EditModalAction(Modal):
    def __init__(self, name: Optional[str] = None):
        super().__init__()
        self.name = name or "编辑"
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.reload = "table"
        self.set_only_on_index_table_row(True)

    def init(self, ctx: Context) -> Any:
        # 可初始化时逻辑
        return self

    def get_body(self, ctx: Context) -> Any:
        template = ctx.template  # 假设ctx.template已实现Resourcer接口

        api = template.update_api(ctx)
        init_api = template.edit_value_api(ctx)
        fields = template.update_fields_within_components(ctx)

        form = (
            form_comp.Component()
            .init()
            .set_style({"paddingTop": "24px"})
            .set_key("editModalForm", False)
            .set_api(api)
            .set_init_api(init_api)
            .set_body(fields)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
        )
        return form

    def get_actions(self, ctx: Context) -> List[Any]:
        cancel = (
            action_comp.Component().init().set_label("取消").set_action_type("cancel")
        )

        submit = (
            action_comp.Component()
            .init()
            .set_label("提交")
            .set_with_loading(True)
            .set_reload("table")
            .set_action_type("submit")
            .set_type("primary", False)
            .set_submit_form("editModalForm")
        )

        return [cancel, submit]
