import json
from typing import Any, Dict
from fastapi import Request
from tortoise.models import Model
from ..performs_queries import PerformsQueries
from ...component.message.message import Message


class UpdateRequest:

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

    async def handle(self, request: Request) -> Any:
        try:
            data: Dict[str, Any] = json.loads(await request.json())
        except Exception as e:
            return Message.error(str(e))

        # 验证参数合法性
        if not data.get("id"):
            return Message.error("参数错误")

        # 模型结构体类
        model_cls = self.model

        # 验证数据合法性
        try:
            await self.resource.validator_for_update(request, data)
        except Exception as e:
            return Message.error(str(e))

        # 保存前回调
        try:
            data = await self.resource.before_saving(request, data)
        except Exception as e:
            return Message.error(str(e))

        # 重组数据
        new_data = {}
        model_fields = model_cls.__annotations__.keys()

        for k, v in data.items():
            nv = v
            if isinstance(v, (list, dict)):
                nv = json.dumps(v, ensure_ascii=False)

            camel_case_name = self.to_pascal_case(k)

            if camel_case_name in model_fields:
                new_data[k] = nv

        # 创建更新查询（Tortoise ORM不支持链式 Updates，所以你可能得手动实现 BuildUpdateQuery）
        query = PerformsQueries(self.request).build_update_query(self.query)

        # 执行更新
        await query.filter(id=data["id"]).update(**new_data)

        # 保存后回调
        try:
            await self.resource.after_saved(request, int(data["id"]), data, query)
        except Exception as e:
            return Message.error(str(e))

        return await self.resource.after_saved_redirect_to(
            request, int(data["id"]), data, None
        )

    def to_pascal_case(self, s: str) -> str:
        return "".join(word.capitalize() for word in s.split("_"))
