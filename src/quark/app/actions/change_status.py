from typing import List

from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.template.action import Action


class ChangeStatus(Action):

    def __init__(self, name: str = "<%= (status==1 ? '禁用' : '启用') %>"):
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.set_only_on_index_table_row(True)
        self.with_confirm(
            "确定要<%= (status==1 ? '禁用' : '启用') %>数据吗？", "", "pop"
        )

    def get_api_params(self) -> List[str]:
        return ["id", "status"]

    async def handle(self, request: Request, query: QuerySet):
        status = request.query_params.get("status")
        if status is None:
            return Message.error("参数错误")

        try:
            # 切换状态逻辑
            field_status = 0 if status == "1" else 1

            id_param = request.query_params.get("id")
            if not id_param:
                return Message.error("缺少 ID 参数")

            ids = [int(i) for i in id_param.split(",")]
            await query.filter(id__in=ids).update(status=field_status)
            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
