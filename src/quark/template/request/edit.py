import json
from datetime import datetime
from typing import Any, Dict, Optional

from tortoise.queryset import QuerySet

from quark import Message, Request

from ..performs_queries import PerformsQueries


class EditRequest:
    """
    用于处理资源编辑页数据填充和初始化数据获取。
    """

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 查询对象
    query: QuerySet = None

    # 字段
    fields: Optional[Any] = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        query: QuerySet,
        fields: Optional[Any],
    ):
        self.request = request
        self.resource = resource
        self.query = query
        self.fields = fields

    async def fill_data(self) -> Dict[str, Any]:
        """
        获取并解析编辑表单数据。
        """
        id_value = self.request.query_params.get("id", "")
        if not id_value:
            return {}

        # 构建查询
        result = (
            await PerformsQueries(self.request).build_edit_query(self.query).first()
        )
        if not result:
            return {}

        # 将查询结果转为 dict
        if hasattr(result, "to_dict"):
            result_dict = result.to_dict()
        elif hasattr(result, "__dict__"):
            result_dict = dict(result.__dict__)
        else:
            result_dict = dict(result)

        # 填充字段数据
        fields_data = {}
        for field in self.fields:
            name = getattr(field, "name", None)
            if not name or name not in result_dict:
                continue

            value = result_dict[name]
            component = getattr(field, "component", "")
            field_value: Any = value

            # 时间字段格式化
            if component in ["datetimeField", "dateField"]:
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

            fields_data[name] = field_value

        return fields_data

    async def values(self) -> Any:
        """
        获取表单初始化数据，并调用显示前回调。
        """
        data = await self.fill_data()

        # 编辑前回调
        data = await self.resource.before_editing(self.request, data)

        # 解析嵌套 JSON 字符串为对象
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
