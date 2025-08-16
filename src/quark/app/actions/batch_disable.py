from typing import List

from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.template.action import Action


class BatchDisable(Action):

    def __init__(self, name: str = "批量禁用"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.set_only_on_index_table_alert(True)
        self.with_confirm(
            "确定要禁用吗？", "禁用后数据将无法使用，请谨慎操作！", "modal"
        )

    def get_api_params(self) -> List[str]:
        return ["id"]

    async def handle(self, request: Request, query: QuerySet):
        id_param = request.query_params.get("id")
        if not id_param:
            return Message.error("参数错误")

        try:
            ids = [int(i) for i in id_param.split(",")]

            # 更新 status 字段为 0
            await query.filter(id__in=ids).update(status=0)
            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
