from typing import List

from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.template.action import Action


class Delete(Action):

    def __init__(self, name: str = "删除"):
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.with_confirm(
            "确定要删除吗？", "删除后数据将无法恢复，请谨慎操作！", "modal"
        )
        self.set_only_on_index_table_row(True)
        self.set_api_params(["id"])

    def get_api_params(self) -> List[str]:
        return ["id"]

    async def handle(self, request: Request, query: QuerySet):
        try:
            # ORM 需要根据你的实际框架调整，这里示例使用异步删除
            await query.delete()
            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
