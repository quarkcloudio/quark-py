import json
from pydantic import ValidationError
from typing import Any, Dict
from fastapi import Request
from tortoise.models import Model
from ...component.message.message import Message


class StoreRequest:

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 模型对象
    model: Model = None

    # 查询对象
    query: Model = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        model: Model,
        query: Model,
    ):
        self.request = request
        self.resource = resource
        self.model = model
        self.query = query

    async def handle(self, request: Request, data: Dict[str, Any]) -> Any:
        # 验证数据合法性
        try:
            await self.resource.validator_for_creation(request, data)
        except ValidationError as e:
            return Message.error(str(e))

        # 保存前回调
        try:
            data = await self.resource.before_saving(request, data)
        except Exception as e:
            return Message.error(str(e))

        # 重组数据
        new_data = {}
        model_fields = self.model.__class__.__annotations__.keys()

        for k, v in data.items():
            nv = v

            if isinstance(v, (list, dict)):
                nv = json.dumps(v, ensure_ascii=False)

            # 将字段名转换为PascalCase，假设你有一个 stringy 工具或自己实现
            camel_case_name = self.to_pascal_case(k)

            if camel_case_name in model_fields:
                new_data[k] = nv

        # 数据赋值
        for field, value in new_data.items():
            setattr(self.model, field, value)

        # 保存数据
        await self.model.save()

        # 因为 tortoise 不会更新零值，我们再使用 update 对部分字段重新更新
        if not hasattr(self.model, "id"):
            return Message.error("参数错误")

        id = self.model.id
        await self.model.__class__.filter(id=id).update(**new_data)

        # 保存后回调
        try:
            await self.resource.after_saved(request, id, data, self.model)
        except Exception as e:
            return Message.error(str(e))

        return await self.resource.after_saved_redirect_to(request, id, data, None)

    def to_pascal_case(self, s: str) -> str:
        return "".join(word.capitalize() for word in s.split("_"))
