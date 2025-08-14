import json
from typing import Any, Dict

from tortoise.models import Model

from quark import Message, Request

from ..performs_validation import PerformsValidation


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
        try:
            await PerformsValidation(
                request=self.request, fields=self.fields
            ).validator_for_creation(data)
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

        # 保存数据
        try:
            instance = await self.model.create(**new_data)

        except Exception as e:
            return Message.error(str(e))

        id = getattr(instance, "id", None)
        if not id:
            return Message.error("参数错误")

        # 保存后回调
        try:
            await self.resource.after_saved(self.request, id, data, self.model)
        except Exception as e:
            return Message.error(str(e))

        return await self.resource.after_saved_redirect_to(self.request, id, data)
