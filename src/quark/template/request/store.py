import json
from typing import Any, Dict
from fastapi import Request
from tortoise.models import Model
from ..performs_validation import PerformsValidation
from ...component.message.message import Message


class StoreRequest:

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 查询对象
    query: Model = None

    # 列表页字段
    fields: list = None

    def __init__(self, request: Request, resource: Any, query: Model, fields: list):
        self.request = request
        self.resource = resource
        self.query = query
        self.fields = fields

    async def handle(self, data: Dict[str, Any]) -> Any:

        print("1111111111111111")
        # 验证数据合法性
        try:
            await PerformsValidation(
                request=self.request, fields=self.fields
            ).validator_for_creation(self.request, data)
        except Exception as e:
            return Message.error(str(e))

        print("222222222222")
        # 保存前回调
        try:
            data = await self.resource.before_saving(self.request, data)
        except Exception as e:
            return Message.error(str(e))

        print("3333333333333")
        # 重组数据
        new_data = {}
        model_fields = self.query.__class__.__annotations__.keys()
        for k, v in data.items():
            nv = v
            if isinstance(v, (list, dict)):
                nv = json.dumps(v, ensure_ascii=False)

            camel_case_name = self.to_pascal_case(k)
            if camel_case_name in model_fields:
                new_data[k] = nv

        # 数据赋值
        for field, value in new_data.items():
            setattr(self.query, field, value)

        # 保存数据
        await self.query.save()

        # 因为 tortoise 不会更新零值，我们再使用 update 对部分字段重新更新
        if not hasattr(self.query, "id"):
            return Message.error("参数错误")

        id = self.query.id
        await self.query.__class__.filter(id=id).update(**new_data)

        # 保存后回调
        try:
            await self.resource.after_saved(self.request, id, data, self.query)
        except Exception as e:
            return Message.error(str(e))

        return await self.resource.after_saved_redirect_to(self.request, id, data, None)

    def to_pascal_case(self, s: str) -> str:
        return "".join(word.capitalize() for word in s.split("_"))
