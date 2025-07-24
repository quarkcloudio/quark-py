import json
from typing import Any
from fastapi import Request
from tortoise.models import QuerySet
from ..performs_queries import PerformsQueries
from ..performs_validation import PerformsValidation
from ...component.message.message import Message


class UpdateRequest:

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 查询对象
    query: QuerySet = None

    # 字段列表
    fields: list = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        query: QuerySet,
        fields: list,
    ):
        self.request = request
        self.resource = resource
        self.query = query
        self.fields = fields

    async def handle(self) -> Any:
        data = await self.request.json()

        # 验证参数合法性
        if not data.get("id"):
            return Message.error("参数错误")

        # 验证数据合法性
        try:
            await PerformsValidation(
                request=self.request, fields=self.fields
            ).validator_for_update(data)
        except Exception as e:
            return Message.error(str(e))

        # 保存前回调
        try:
            data = await self.resource.before_saving(self.request, data)
        except Exception as e:
            return Message.error(str(e))

        # 重组数据
        new_data = {}
        for k, v in data.items():
            nv = v
            if isinstance(v, (list, dict)):
                nv = json.dumps(v, ensure_ascii=False)

            new_data[k] = nv

        query = await PerformsQueries(self.request).build_update_query(self.query)

        # 删除id，否则无法更新
        del new_data["id"]

        # 执行更新
        try:
            await query.filter(id=data["id"]).update(**new_data)
        except Exception as e:
            return Message.error(str(e))

        # 保存后回调
        try:
            await self.resource.after_saved(self.request, data["id"], data, query)
        except Exception as e:
            return Message.error(str(e))

        return await self.resource.after_saved_redirect_to(
            self.request, data["id"], data
        )
