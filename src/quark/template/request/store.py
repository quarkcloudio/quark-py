import json
from pydantic import ValidationError
from typing import Any, Dict
from quark.context import Context  # 假设你封装了类似 quark.Context 的 Python 类
from quark.template.admin.resource.types import Resourcer  # 自定义接口定义
from tortoise import Tortoise
from tortoise.exceptions import DoesNotExist


class StoreRequest:

    async def handle(self, ctx: Context, data: Dict[str, Any]) -> Any:
        # 模版实例
        template: Resourcer = ctx.template

        # 模型结构体
        model_instance = template.get_model()  # 返回一个模型类
        data_instance = template.get_model()()  # 创建一个新实例

        # 验证数据合法性
        try:
            await template.validator_for_creation(ctx, data)
        except ValidationError as e:
            return ctx.json_error(str(e))

        # 保存前回调
        try:
            data = await template.before_saving(ctx, data)
        except Exception as e:
            return ctx.json_error(str(e))

        # 重组数据
        new_data = {}
        model_fields = data_instance.__class__.__annotations__.keys()

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
            setattr(data_instance, field, value)

        # 保存数据
        await data_instance.save()

        # 因为 tortoise 不会更新零值，我们再使用 update 对部分字段重新更新
        if not hasattr(data_instance, "id"):
            return ctx.json_error("参数错误")

        id = data_instance.id
        await data_instance.__class__.filter(id=id).update(**new_data)

        # 保存后回调
        try:
            await template.after_saved(ctx, id, data, data_instance)
        except Exception as e:
            return ctx.json_error(str(e))

        return await template.after_saved_redirect_to(ctx, id, data, None)

    def to_pascal_case(self, s: str) -> str:
        # 替代 stringy.New(k).PascalCase("?", "").Get()
        return "".join(word.capitalize() for word in s.split("_"))
