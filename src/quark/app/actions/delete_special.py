from typing import List

from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.template.action import Action


class DeleteSpecial(Action):

    def __init__(self, name=None):
        # 名称支持动态表达式，Python中可用字符串或模板渲染实现
        self.name = name or "<%= (id==1 ? '' : '删除') %>"
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
            await query.delete()
            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
