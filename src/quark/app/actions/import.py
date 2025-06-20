from typing import List, Dict, Any, Optional


class ImportAction:
    def __init__(self, name: Optional[str] = None):
        # 文字
        self.Name = name or "导入数据"
        self.DestroyOnClose = True  # 关闭时销毁 Modal 里的子元素
        self.ShowOnlyOnIndex = True  # 设置展示位置（只在列表页显示）

    def init(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        # 模拟初始化，返回配置参数
        return {
            "DestroyOnClose": self.DestroyOnClose,
            "ShowOnlyOnIndex": self.ShowOnlyOnIndex,
        }

    def get_body(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        resource = ctx.get("resource", "")
        token = ctx.get("token", "")

        api = f"/api/admin/{resource}/import"
        template_link = f"/api/admin/{resource}/import/template?token={token}"
        get_tpl = {
            "type": "tpl",
            "body": f"模板文件: <a href='{template_link}' target='_blank'>下载模板</a>",
            "style": {"marginLeft": "50px"},
        }

        fields = [
            {
                "type": "space",
                "body": [get_tpl],
                "direction": "vertical",
                "size": "middle",
                "style": {"marginBottom": "20px"},
            },
            {
                "type": "file",
                "name": "fileId",
                "label": "导入文件",
                "limitNum": 1,
                "limitType": [
                    "application/vnd.ms-excel",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ],
                "help": "请上传xls格式的文件",
            },
        ]

        form_component = {
            "type": "form",
            "key": "importModalForm",
            "api": api,
            "body": fields,
            "labelCol": {"span": 6},
            "wrapperCol": {"span": 18},
            "style": {"paddingTop": "24px"},
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
                "submitForm": "importModalForm",
            },
        ]


# 模拟使用示例：
ctx_example = {
    "resource": "user",
    "token": "fake-token-12345",
}

action = ImportAction()
print("Init:", action.init(ctx_example))
print("Body:", action.get_body(ctx_example))
print("Actions:", action.get_actions(ctx_example))
