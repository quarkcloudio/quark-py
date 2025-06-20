from typing import List, Dict, Any


class MenuEditDrawerAction:
    def __init__(self, name: str = None):
        self.Name = name if name else "编辑"
        self.Type = "link"
        self.Size = "small"
        self.DestroyOnClose = True
        self.Reload = "table"
        self.Width = 750
        self.ShowOnlyOnIndexTableRow = True

    def init(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        # 初始化配置
        return {
            "Name": self.Name,
            "Type": self.Type,
            "Size": self.Size,
            "DestroyOnClose": self.DestroyOnClose,
            "Reload": self.Reload,
            "Width": self.Width,
            "ShowOnlyOnIndexTableRow": self.ShowOnlyOnIndexTableRow,
        }

    def get_body(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        template = ctx.get("template")

        api = template.update_api(ctx)
        init_api = template.edit_value_api(ctx)
        fields = template.update_fields_within_components(ctx)

        form_component = {
            "type": "form",
            "key": "editDrawerForm",
            "layout": "vertical",
            "api": api,
            "initApi": init_api,
            "body": fields,
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
                "submitForm": "editDrawerForm",
            },
        ]


# 示例用法
class TemplateExample:
    def update_api(self, ctx):
        return "/api/admin/menu/update"

    def edit_value_api(self, ctx):
        return "/api/admin/menu/edit_value"

    def update_fields_within_components(self, ctx):
        return [
            {"type": "input", "name": "name", "label": "菜单名称"},
            {"type": "input", "name": "path", "label": "路径"},
        ]


ctx_example = {"template": TemplateExample()}

action = MenuEditDrawerAction()
print("Init:", action.init(ctx_example))
print("Body:", action.get_body(ctx_example))
print("Actions:", action.get_actions(ctx_example))
