from fastapi import Request
from typing import Any
from tortoise.models import QuerySet
from ...component.message.message import Message


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

    def handle(self):
        data = self.request.query_params

        id_val = data.get("id")
        if not id_val:
            return Message.error("id不能为空")

        model_instance = self.query.get(id_val)
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

        # 表格行内编辑执行前回调（模板方法）
        before_result = self.resource.before_editable(id_val, field, value)
        if before_result is not None:
            return before_result

        # 构建查询并更新数据
        self.query.filter(id=id_val).update({field: value})

        # 行内编辑执行后回调
        after_result = self.resource.after_editable(id_val, field, value)
        if after_result is not None:
            return after_result

        return Message.success("操作成功")
