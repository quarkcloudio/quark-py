from typing import Any

from tortoise.queryset import QuerySet

from quark import Message, Request

from ..performs_queries import PerformsQueries


class EditableRequest:

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 查询对象
    query: QuerySet = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        query: QuerySet,
    ):
        self.request = request
        self.resource = resource
        self.query = query

    async def handle(self):
        data = self.request.query_params

        id = data.get("id")
        if not id:
            return Message.error("id不能为空")

        model_instance = await self.query.get(id=id)
        if not model_instance:
            return Message.error("记录不存在")

        field = None
        value = None
        for k, v in data.items():
            if v == "true":
                v = 1
            elif v == "false":
                v = 0

            if k not in ["id", "_t"]:
                field = k
                value = v

        if not field or value is None:
            return Message.error("参数错误")

        try:
            await self.resource.before_editable(self.request, id, field, value)
        except Exception as e:
            return Message.error(str(e))

        # 构建查询并更新数据
        try:
            await PerformsQueries(self.request).build_editable_query(self.query).update(
                **{field: value}
            )
        except Exception as e:
            return Message.error(str(e))

        # 行内编辑执行后回调
        try:
            await self.resource.after_editable(self.request, id, field, value)
        except Exception as e:
            return Message.error(str(e))

        return Message.success("操作成功")
