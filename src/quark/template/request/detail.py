import json
from typing import Dict, Any, List, Optional, Union, Callable
from datetime import datetime
from quark_go_v3 import Context, Resourcer


class DetailRequest:
    """
    用于处理资源详情页数据填充和初始化数据获取。
    """

    def fill_data(self, ctx: Context) -> Dict[str, Any]:
        """
        获取并解析详情页数据。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            dict: 返回解析后的数据字典。
        """
        result = {}
        id_value = ctx.query("id", "")
        if not id_value:
            return result

        # 获取模板实例
        template: Resourcer = ctx.template

        # 获取模型并查询数据
        model_instance = template.get_model()
        query = template.build_detail_query(ctx, model_instance)
        result = query.first() or {}

        # 获取详情字段
        detail_fields = template.detail_fields(ctx)

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
                    action.new(ctx)
                    action.init(ctx)
                    parsed_items.append(template.build_action(ctx, action))

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

    def values(self, ctx: Context) -> Any:
        """
        获取表单初始化数据，并调用显示前回调。

        Args:
            ctx (Context): Quark 上下文对象.

        Returns:
            JSON 响应：返回处理后的数据。
        """
        template: Resourcer = ctx.template
        data = self.fill_data(ctx)

        # 显示前回调
        before_showing = getattr(template, "before_detail_showing", None)
        if before_showing:
            data = before_showing(ctx, data)

        return ctx.cjson_ok("获取成功", data)