import json
from typing import Any

from tortoise.models import Model, QuerySet

from quark import Message, Request

from ..performs_queries import PerformsQueries
from ..performs_validation import PerformsValidation


class UpdateRequest:

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 模型
    model: Model = None

    # 查询对象
    query: QuerySet = None

    # 字段列表
    fields: list = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        model: Model,
        query: QuerySet,
        fields: list,
    ):
        self.request = request
        self.resource = resource
        self.model = model
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
        model_fields = set(self.model._meta.fields_map.keys())

        for k, v in data.items():
            # 只处理模型中存在的字段
            if k in model_fields:
                # 处理特殊数据类型
                if isinstance(v, (list, dict)):
                    new_data[k] = json.dumps(v, ensure_ascii=False)
                else:
                    new_data[k] = v

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
