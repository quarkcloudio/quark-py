from typing import List, Dict, Any
from quark import Request
from quark.template.action import Drawer
from quark.component.form.form import Form
from quark.component.action.action import Action


class MenuCreateDrawer(Drawer):
    def __init__(
        self,
        title: str,
        api: str,
        fields: List[Dict[str, Any]],
        initial_values: Dict[str, Any],
    ):

        # 文字
        self.name = "创建" + title

        # api
        self.api = api

        # 字段
        self.fields = fields

        # 初始值
        self.initial_values = initial_values

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

    def get_body(self, request: Request) -> Dict[str, Any]:
        return (
            Form()
            .set_api(self.api)
            .set_body(self.fields)
            .set_initial_values(self.initial_values)
            .set_label_col({"span": 6})
            .set_wrapper_col({"span": 18})
            .set_key("createDrawerForm", destroy=False)
        )

    def get_actions(self, request: Request) -> List[Dict[str, Any]]:
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
