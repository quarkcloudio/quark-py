from typing import List
from quark import Request
from quark.template.action import Action
from quark.component.message.message import Message


class BatchEnable(Action):
    def __init__(self, name: str = "批量启用"):
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.set_only_on_index_table_alert(True)
        self.with_confirm("确定要启用吗？", "启用后数据将正常使用！", "modal")

    def get_api_params(self) -> List[str]:
        return ["id"]

    async def handle(self, request: Request, db_model):
        id_param = request.query_params.get("id")
        if not id_param:
            return Message.error("参数错误")

        try:
            ids = [int(i) for i in id_param.split(",")]
            await db_model.filter(id__in=ids).update(status=1)
            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
