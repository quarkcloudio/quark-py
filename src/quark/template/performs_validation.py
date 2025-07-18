import re
import json
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Union, Type, Callable, Awaitable, cast
from abc import ABC, abstractmethod
from urllib.parse import parse_qs, urlparse

from tortoise.models import Model
from tortoise import fields
from tortoise.query_utils import Q


class PerformsValidation:
    @abstractmethod
    def creation_fields_without_when(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def update_fields_without_when(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def import_fields_without_when(self, ctx: Context) -> List[Any]:
        pass

    async def validator_for_creation(
        self, ctx: Context, data: Dict[str, Any]
    ) -> Optional[str]:
        rules = await self.rules_for_creation(ctx)
        validator = await self.validator(rules, data)
        await self.after_validation(ctx, validator)
        await self.after_creation_validation(ctx, validator)
        return validator

    async def validator_for_update(
        self, ctx: Context, data: Dict[str, Any]
    ) -> Optional[str]:
        rules = await self.rules_for_update(ctx)
        validator = await self.validator(rules, data)
        await self.after_validation(ctx, validator)
        await self.after_update_validation(ctx, validator)
        return validator

    async def validator_for_import(
        self, ctx: Context, data: Dict[str, Any]
    ) -> Optional[str]:
        rules = await self.rules_for_import(ctx)
        validator = await self.validator(rules, data)
        await self.after_validation(ctx, validator)
        await self.after_import_validation(ctx, validator)
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

    async def rules_for_creation(self, ctx: Context) -> List[Rule]:
        fields = self.creation_fields_without_when(ctx)
        rules = []
        for v in fields:
            rules.extend(await self.get_rules_for_creation(v))
            if isinstance(v, WhenComponent):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(ctx, vi):
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

    async def rules_for_update(self, ctx: Context) -> List[Rule]:
        fields = self.update_fields_without_when(ctx)
        rules = []
        for v in fields:
            rules.extend(await self.get_rules_for_update(v))
            if isinstance(v, WhenComponent):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(ctx, vi):
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

    async def rules_for_import(self, ctx: Context) -> List[Rule]:
        fields = self.import_fields_without_when(ctx)
        rules = []
        for v in fields:
            rules.extend(await self.get_rules_for_creation(v))
            if isinstance(v, WhenComponent):
                when_component = v
                if when_component.items:
                    for vi in when_component.items:
                        if await self.need_validate_when_rules(ctx, vi):
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

    async def need_validate_when_rules(self, ctx: Context, when_item: WhenItem) -> bool:
        cond_name = when_item.condition_name
        cond_opt = when_item.option
        cond_op = when_item.condition_operator

        parsed = urlparse(ctx.original_url())
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

    async def after_validation(self, ctx: Context, validator: Optional[str]):
        pass

    async def after_creation_validation(self, ctx: Context, validator: Optional[str]):
        pass

    async def after_update_validation(self, ctx: Context, validator: Optional[str]):
        pass

    async def after_import_validation(self, ctx: Context, validator: Optional[str]):
        pass
