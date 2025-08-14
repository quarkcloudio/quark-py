from typing import Any, Dict, List

from quark import Request
from quark.services.auth import AuthService
from quark.template.action import Action


class Import(Action):

    def __init__(self, name: str = "导入数据"):
        self.name = name
        self.destroy_on_close = True
        self.set_only_on_index(True)

    async def get_body(self, request: Request) -> Dict[str, Any]:
        resource = request.url.path.get("resource", "")
        token = AuthService(request).get_token()

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

    async def get_actions(self, request: Request) -> List[Dict[str, Any]]:
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
