import json
from datetime import datetime
from typing import Any, Dict, Optional

from tortoise.queryset import QuerySet

from quark import Message, Request

from ..performs_queries import PerformsQueries
from ..resolves_actions import ResolvesActions


class DetailRequest:
    """
    用于处理资源详情页数据填充和初始化数据获取。
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
        获取并解析详情页数据
        """
        result = {}
        id_value = self.request.query_params.get("id", "")
        if not id_value:
            return result

        # 构建查询
        result = (
            await PerformsQueries(self.request).build_detail_query(self.query).first()
        )
        fields = {}
        for field in self.fields:
            component = getattr(field, "component", None)
            name = getattr(field, "name", "")

            if component == "actionField":
                # 行为字段
                items = getattr(field, "items", [])
                callback = field.callback

                if callback:
                    items = await callback(result)

                parsed_items = []
                for action in items:
                    parsed_items.append(
                        await ResolvesActions(self.request).build_action(action)
                    )

                fields[name] = parsed_items

            else:
                # 普通字段
                callback = field.callback
                if callback:
                    fields[name] = await callback(result)
                else:
                    value = getattr(result, name, None)
                    if value is None:
                        continue

                    if isinstance(value, str):
                        # JSON 解析
                        try:
                            value = json.loads(value)
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
                            value = value.strftime(format_str)

                    fields[name] = value

        return fields

    async def values(self) -> Any:
        """
        获取表单初始化数据，并调用显示前回调。
        """
        data = await self.fill_data()

        # 显示前回调
        data = await self.resource.before_detail_showing(self.request, data)

        return Message.success("获取成功", data)
