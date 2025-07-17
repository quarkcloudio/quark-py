import json
from fastapi import Request
from typing import Dict, Any, Optional, Callable
from tortoise.models import Model
from datetime import datetime
from ..performs_queries import PerformsQueries
from ..resolves_actions import ResolvesActions
from ...component.message.message import Message


class DetailRequest:
    """
    用于处理资源详情页数据填充和初始化数据获取。
    """

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 查询对象
    model: Model = None

    # 字段
    fields: Optional[Any] = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        model: Model,
        fields: Optional[Any],
    ):
        self.request = request
        self.resource = resource
        self.model = model
        self.fields = fields

    def fill_data(self) -> Dict[str, Any]:
        """
        获取并解析详情页数据
        """
        result = {}
        id_value = self.request.query_params.get("id", "")
        if not id_value:
            return result

        # 构建查询
        query = PerformsQueries(self.request).build_detail_query(self.model)
        result = query.first() or {}

        # 获取详情字段
        detail_fields = self.fields

        fields = {}
        for field in detail_fields:
            component = getattr(field, "component", None)
            name = getattr(field, "name", "")

            if component == "actionField":
                # 行为字段
                items = getattr(field, "items", [])
                callback: Optional[Callable] = getattr(field, "get_callback", None)

                if callback:
                    items = callback(result)

                parsed_items = []

                for action in items:
                    parsed_items.append(
                        ResolvesActions().set_request(self.request).build_action(action)
                    )

                fields[name] = parsed_items

            else:
                # 普通字段
                callback: Optional[Callable] = getattr(field, "get_callback", None)

                if callback:
                    fields[name] = callback(result)
                else:
                    value = result.get(name)
                    if value is not None:
                        field_value: Any = value

                        if isinstance(value, str):
                            # JSON 解析
                            try:
                                field_value = json.loads(value)
                            except json.JSONDecodeError:
                                pass

                        # 时间字段处理
                        if component in ("datetimeField", "dateField"):
                            format_str = getattr(field, "format", "%Y-%m-%d %H:%M:%S")
                            format_str = (
                                format_str.replace("YYYY", "%Y")
                                .replace("MM", "%m")
                                .replace("DD", "%d")
                                .replace("HH", "%H")
                                .replace("mm", "%M")
                                .replace("ss", "%S")
                            )
                            if isinstance(value, datetime):
                                field_value = value.strftime(format_str)

                        fields[name] = field_value

        return fields

    def values(self) -> Any:
        """
        获取表单初始化数据，并调用显示前回调。
        """
        data = self.fill_data()

        # 显示前回调
        before_showing = getattr(self.resource, "before_detail_showing", None)
        if before_showing:
            data = before_showing(self.request, data)

        return Message.success("获取成功", data)
