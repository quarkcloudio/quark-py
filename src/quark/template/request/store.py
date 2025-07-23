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
    model: Model = None

    # 字段列表
    fields: list = None

    def __init__(self, request: Request, resource: Any, model: Model, fields: list):
        self.request = request
        self.resource = resource
        self.model = model
        self.fields = fields

    async def handle(self, data: Dict[str, Any]) -> Any:
        # 验证数据合法性
        errMsg = await PerformsValidation(
            request=self.request, fields=self.fields
        ).validator_for_creation(data)
        if errMsg:
            return Message.error(errMsg)

        # 保存前回调
        try:
            data = await self.resource.before_saving(self.request, data)
        except Exception as e:
            return Message.error(str(e))

        # 重组数据
        new_data = {}
        model_fields = self.model.__class__.__annotations__.keys()
        for k, v in data.items():
            nv = v
            if isinstance(v, (list, dict)):
                nv = json.dumps(v, ensure_ascii=False)

            camel_case_name = self.to_pascal_case(k)
            if camel_case_name in model_fields:
                new_data[k] = nv

        # 数据赋值
        for field, value in new_data.items():
            setattr(self.model, field, value)

        # 保存数据
        await self.model.save()

        if not hasattr(self.model, "id"):
            return Message.error("参数错误")

        id = self.model.id
        # 保存后回调
        try:
            await self.resource.after_saved(self.request, id, data, self.model)
        except Exception as e:
            return Message.error(str(e))

        return await self.resource.after_saved_redirect_to(self.request, id, data, None)

    def to_pascal_case(self, s: str) -> str:
        return "".join(word.capitalize() for word in s.split("_"))
