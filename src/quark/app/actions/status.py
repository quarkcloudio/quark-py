from tortoise.queryset import QuerySet
from tortoise.transactions import in_transaction

from quark import Message, Request
from quark.template.action import Action


class Status(Action):
    def __init__(self):
        self.reload = "table"
        self.checked_children = "正常"
        self.unchecked_children = "禁用"
        self.field_name = "status"
        self.field_value = "1"
        self.set_only_on_index_table_row(True)

    def get_api_params(self):
        return ["id"]

    async def handle(self, request: Request, query: QuerySet):
        # 获取参数
        status = request.query_params.get("status")
        if status is None:
            return Message.error("参数错误")

        id_ = request.query_params.get("id")
        if id_ is None:
            return Message.error("缺少id参数")

        # 解析状态
        if status in ("0", "false"):
            field_status = 0
        else:
            field_status = 1

        try:
            async with in_transaction() as conn:
                obj = await query.filter(id=int(id_)).using_db(conn).first()
                if not obj:
                    return Message.error("记录不存在")

                obj.status = field_status
                await obj.save(using_db=conn)
        except Exception as e:
            return Message.error(str(e))

        return Message.success("操作成功")
