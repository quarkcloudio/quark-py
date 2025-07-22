import re
from typing import List, Dict, Any, Optional, Type
from urllib.parse import parse_qs, urlparse
from fastapi import Request
from tortoise.models import Model
from tortoise.query_utils import Q
from ..component.form import Rule
from ..component.form.fields.when import When, Item


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

    async def validator_for_creation(
        self, request: Request, data: Dict[str, Any]
    ) -> Optional[str]:
        rules = await self.rules_for_creation(request)
        validator = await self.validator(rules, data)
        return validator

    async def validator_for_update(
        self, request: Request, data: Dict[str, Any]
    ) -> Optional[str]:
        rules = await self.rules_for_update(request)
        validator = await self.validator(rules, data)
        return validator

    async def validator_for_import(
        self, request: Request, data: Dict[str, Any]
    ) -> Optional[str]:
        rules = await self.rules_for_import(request)
        validator = await self.validator(rules, data)
        return validator

    async def validator(self, rules: List[Rule], data: Dict[str, Any]) -> Optional[str]:
        for rule in rules:
            field_value = data.get(rule.name)
            if rule.rule_type == "required":
                if field_value is None or field_value == "":
                    return rule.message
            elif rule.rule_type == "min":
                if isinstance(field_value, str):
                    if len(field_value) < rule.min:
                        return rule.message
            elif rule.rule_type == "max":
                if isinstance(field_value, str):
                    if len(field_value) > rule.max:
                        return rule.message
            elif rule.rule_type == "regexp":
                if isinstance(field_value, str):
                    if not re.fullmatch(rule.pattern, field_value):
                        return rule.message
            elif rule.rule_type == "unique":
                table: Type[Model] = globals()[rule.unique_table]
                field = rule.unique_table_field
                ignore_value = rule.unique_ignore_value
                if ignore_value:
                    ignore_key = ignore_value.strip("{}")
                    ignore_val = data.get(ignore_key)
                    count = (
                        await table.filter(**{f"{field}": field_value})
                        .filter(~Q(**{f"{ignore_key}": ignore_val}))
                        .count()
                    )
                else:
                    count = await table.filter(**{f"{field}": field_value}).count()
                if count > 0:
                    return rule.message
        return None

    async def rules_for_creation(self, request: Request) -> List[Rule]:
        rules = []
        for v in self.fields:
            rules.extend(await self.get_rules_for_creation(v))
            if isinstance(v, When):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(request, vi):
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

    async def rules_for_update(self, request: Request) -> List[Rule]:
        rules = []
        for v in self.fields:
            rules.extend(await self.get_rules_for_update(v))
            if isinstance(v, When):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(request, vi):
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

    async def rules_for_import(self, request: Request) -> List[Rule]:
        rules = []
        for v in self.fields:
            rules.extend(await self.get_rules_for_creation(v))
            if isinstance(v, When):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(request, vi):
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

    async def need_validate_when_rules(self, request: Request, when_item: Item) -> bool:
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
