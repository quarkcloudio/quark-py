import re
from typing import Any, Dict, List, Optional, Type
from urllib.parse import parse_qs, urlparse

from fastapi import Request
from tortoise import Tortoise
from tortoise.expressions import Q
from tortoise.models import Model

from ..component.form import Rule
from ..component.form.fields.when import Item, When


class PerformsValidation:

    # 请求对象
    request: Request = None

    # 字段
    fields: Optional[Any] = None

    def __init__(
        self,
        request: Optional[Request] = None,
        fields: Optional[Any] = None,
    ):
        self.request = request
        self.fields = fields

    async def validator_for_creation(self, data: Dict[str, Any]):
        rules = await self.rules_for_creation()
        validator = await self.validator(rules, data)
        if validator:
            raise ValueError(validator)

    async def validator_for_update(self, data: Dict[str, Any]):
        rules = await self.rules_for_update()
        validator = await self.validator(rules, data)
        if validator:
            raise ValueError(validator)

    async def validator_for_import(self, data: Dict[str, Any]):
        rules = await self.rules_for_import()
        validator = await self.validator(rules, data)
        if validator:
            raise ValueError(validator)

    async def validator(self, rules: List[Rule], data: Dict[str, Any]) -> Optional[str]:
        for rule in rules:
            field_value = data.get(rule.name)
            if rule.rule_type == "required":
                if field_value is None or field_value == "":
                    return rule.message
            elif rule.rule_type == "min":
                if isinstance(field_value, str):
                    if len(field_value) < rule.min_value:
                        return rule.message
            elif rule.rule_type == "max":
                if isinstance(field_value, str):
                    if len(field_value) > rule.max_value:
                        return rule.message
            elif rule.rule_type == "regexp":
                if isinstance(field_value, str):
                    # 标准化正则表达式模式
                    pattern = rule.pattern
                    if pattern.startswith("/") and pattern.endswith("/"):
                        pattern = pattern[1:-1]
                    if not re.fullmatch(pattern, field_value):
                        return rule.message
            elif rule.rule_type == "unique":
                try:
                    # 通过 Tortoise ORM 获取模型
                    table: Type[Model] = Tortoise.apps.get("models").get(
                        rule.unique_table
                    )
                    if not table:
                        # 如果通过表名找不到，尝试通过类名查找
                        table = Tortoise.apps.get("models").get(
                            rule.unique_table.rstrip("s").capitalize()
                        )

                    if not table or not issubclass(table, Model):
                        return f"验证规则错误: 找不到模型 {rule.unique_table}"

                    # 其余代码保持不变
                    field = rule.unique_table_field
                    ignore_value = rule.unique_ignore_value

                    # 构建查询条件
                    filter_kwargs = {f"{field}": field_value}
                    query = table.filter(**filter_kwargs)

                    # 处理忽略值（用于更新时排除自身）
                    if (
                        ignore_value
                        and ignore_value.startswith("{")
                        and ignore_value.endswith("}")
                    ):
                        ignore_key = ignore_value.strip("{}")
                        ignore_val = data.get(ignore_key)
                        if ignore_val is not None:
                            query = query.filter(~Q(**{f"{ignore_key}": ignore_val}))

                    count = await query.count()
                    if count > 0:
                        return rule.message

                except KeyError:
                    return f"验证规则错误: 找不到模型 {rule.unique_table}"
                except Exception as e:
                    return f"验证规则错误: {str(e)}"
        return None

    async def rules_for_creation(self) -> List[Rule]:
        rules = []
        for v in self.fields:
            rules.extend(await self.get_rules_for_creation(v))
            if isinstance(v, When):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(vi):
                            body = vi.body
                            if body:
                                if isinstance(body, list):
                                    for bv in body:
                                        rules.extend(
                                            await self.get_rules_for_creation(bv)
                                        )
                                else:
                                    rules.extend(
                                        await self.get_rules_for_creation(body)
                                    )
        return rules

    async def rules_for_update(self) -> List[Rule]:
        rules = []
        for v in self.fields:
            rules.extend(await self.get_rules_for_update(v))
            if isinstance(v, When):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(vi):
                            body = vi.body
                            if body:
                                if isinstance(body, list):
                                    for bv in body:
                                        rules.extend(
                                            await self.get_rules_for_update(bv)
                                        )
                                else:
                                    rules.extend(await self.get_rules_for_update(body))
        return rules

    async def rules_for_import(self) -> List[Rule]:
        rules = []
        for v in self.fields:
            rules.extend(await self.get_rules_for_creation(v))
            if isinstance(v, When):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(vi):
                            body = vi.body
                            if body:
                                if isinstance(body, list):
                                    for bv in body:
                                        rules.extend(
                                            await self.get_rules_for_creation(bv)
                                        )
                                else:
                                    rules.extend(
                                        await self.get_rules_for_creation(body)
                                    )
        return rules

    async def need_validate_when_rules(self, when_item: Item) -> bool:
        cond_name = when_item.condition_name
        cond_opt = when_item.option
        cond_op = when_item.condition_operator
        parsed = urlparse(self.request.url.path)
        query_params = parse_qs(parsed.query)
        value = query_params.get(cond_name, [""])[0]

        if not value:
            return False

        if cond_op == "=":
            return value == cond_opt
        elif cond_op == ">":
            return value > cond_opt
        elif cond_op == "<":
            return value < cond_opt
        elif cond_op == "<=":
            return value <= cond_opt
        elif cond_op == ">=":
            return value >= cond_opt
        elif cond_op == "has":
            if isinstance(cond_opt, list):
                return value in cond_opt
            else:
                return cond_opt in value
        elif cond_op == "in":
            if isinstance(cond_opt, list):
                return value in cond_opt
            else:
                return value == cond_opt
        else:
            return value == cond_opt

    async def get_rules_for_creation(self, field: Any) -> List[Rule]:
        rules = []
        if hasattr(field, "get_rules"):
            rules.extend(field.get_rules())
        if hasattr(field, "get_creation_rules"):
            rules.extend(field.get_creation_rules())
        return rules

    async def get_rules_for_update(self, field: Any) -> List[Rule]:
        rules = []
        if hasattr(field, "get_rules"):
            rules.extend(field.get_rules())
        if hasattr(field, "get_update_rules"):
            rules.extend(field.get_update_rules())
        return rules
