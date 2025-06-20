from typing import List, Dict, Any


class MenuCreateDrawerAction:
    def __init__(self):
        self.Name = ""
        self.Type = ""
        self.Icon = ""
        self.Reload = ""
        self.DestroyOnClose = True
        self.Width = 750
        self.ShowOnlyOnIndex = True

    def init(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        template = ctx.get("template")

        # 文字
        self.Name = "创建" + template.get_title()

        # 类型
        self.Type = "primary"

        # 图标
        self.Icon = "plus-circle"

        # 执行成功后刷新的组件
        self.Reload = "table"

        # 关闭时销毁 Drawer 里的子元素
        self.DestroyOnClose = True

        # 抽屉弹出层宽度
        self.Width = 750

        # 设置展示位置（只在列表页显示）
        self.ShowOnlyOnIndex = True

        return {
            "Name": self.Name,
            "Type": self.Type,
            "Icon": self.Icon,
            "Reload": self.Reload,
            "DestroyOnClose": self.DestroyOnClose,
            "Width": self.Width,
            "ShowOnlyOnIndex": self.ShowOnlyOnIndex,
        }

    def get_body(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        template = ctx.get("template")

        api = template.creation_api(ctx)
        fields = template.creation_fields_within_components(ctx)
        initial_values = template.before_creating(ctx)

        form_component = {
            "type": "form",
            "key": "createDrawerForm",
            "layout": "vertical",
            "api": api,
            "body": fields,
            "initialValues": initial_values,
        }

        return form_component

    def get_actions(self, ctx: Dict[str, Any]) -> List[Dict[str, Any]]:
        return [
            {
                "type": "action",
                "label": "取消",
                "actionType": "cancel",
            },
            {
                "type": "action",
                "label": "提交",
                "withLoading": True,
                "reload": "table",
                "actionType": "submit",
                "btnType": "primary",
                "submitForm": "createDrawerForm",
            },
        ]


# 示例使用：假设有一个模板类实现了必要的方法
class TemplateExample:
    def get_title(self):
        return "菜单"

    def creation_api(self, ctx):
        return "/api/admin/menu/create"

    def creation_fields_within_components(self, ctx):
        # 返回字段列表，示例
        return [
            {"type": "input", "name": "name", "label": "菜单名称"},
            {"type": "input", "name": "path", "label": "路径"},
        ]

    def before_creating(self, ctx):
        # 创建前的默认数据
        return {
            "name": "",
            "path": "/",
        }


ctx_example = {"template": TemplateExample()}

action = MenuCreateDrawerAction()
print("Init:", action.init(ctx_example))
print("Body:", action.get_body(ctx_example))
print("Actions:", action.get_actions(ctx_example))
