import json
from fastapi import Request
from typing import Dict, Any, Optional
from tortoise.models import Model
from datetime import datetime
from ..performs_queries import PerformsQueries
from ...component.message.message import Message


class EditRequest:
    """
    用于处理资源编辑页数据填充和初始化数据获取。
    """

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 查询对象
    query: Model = None

    # 字段
    fields: Optional[Any] = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        query: Model,
        fields: Optional[Any],
    ):
        self.request = request
        self.resource = resource
        self.query = query
        self.fields = fields

    def fill_data(self) -> Dict[str, Any]:
        """
        获取并解析编辑表单数据。
        """
        result = {}
        id_value = self.request.query_params.get("id", "")
        if not id_value:
            return result

        # 构建查询
        query = PerformsQueries(self.request).build_edit_query(self.query)
        result = query.first() or {}

        fields = {}
        for field in self.fields:
            name = getattr(field, "name", "")

            value = result.get(name)
            if value is None:
                continue

            component = getattr(field, "component", "")
            field_value: Any = value

            # 时间字段处理
            if component == "datetimeField" or component == "dateField":
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

        # 编辑前回调
        before_editing = getattr(self.resource, "before_editing", None)
        if before_editing:
            data = before_editing(self.request, data)

        # 解析嵌套 JSON 字符串
        parsed_data = {}
        for key, value in data.items():
            if isinstance(value, str):
                try:
                    parsed = json.loads(value)
                    if isinstance(parsed, (dict, list)):
                        value = parsed
                except json.JSONDecodeError:
                    pass
            parsed_data[key] = value

        return Message.success("获取成功", parsed_data)
