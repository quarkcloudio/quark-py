from app.core.context import Context
from app.template.admin.resource.actions import Drawer
from app.template.admin.component.form import Component as FormComponent
from app.template.admin.component.action import Component as ActionComponent


class CreateDrawerAction(Drawer):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.type = "primary"
        self.icon = "plus-circle"
        self.reload = "table"
        self.destroy_on_close = True
        self.set_only_on_index(True)

    def init(self, ctx: Context):
        template = ctx.template  # 假设实现了 Resourcer 接口
        self.name = "创建" + template.get_title()
        return self

    def get_body(self, ctx: Context):
        template = ctx.template

        api = template.creation_api(ctx)
        fields = template.creation_fields_within_components(ctx)
        initial_data = template.before_creating(ctx)

        return (
            FormComponent()
            .init()
            .set_key("createDrawerForm", destroy=False)
            .set_api(api)
            .set_body(fields)
            .set_initial_values(initial_data)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
        )

    def get_actions(self, ctx: Context):
        return [
            ActionComponent().init().set_label("取消").set_action_type("cancel"),
            ActionComponent()
            .init()
            .set_label("提交")
            .set_with_loading(True)
            .set_reload("table")
            .set_action_type("submit")
            .set_type("primary", ghost=False)
            .set_submit_form("createDrawerForm"),
        ]
