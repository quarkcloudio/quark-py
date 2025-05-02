import json
from typing import Dict, Any, Optional, List, Union
from datetime import datetime
from quark_go_v3 import Context, Resourcer


class EditRequest:
    """
    用于处理资源编辑页数据填充和初始化数据获取。
    """

    def fill_data(self, ctx: Context) -> Dict[str, Any]:
        """
        获取并解析编辑表单数据。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            dict: 返回解析后的数据字典。
        """
        result = {}
        id_value = ctx.query("id", "")
        if not id_value:
            return result

        # 模版实例
        template: Resourcer = ctx.template

        # 模型结构体 & 查询
        model_instance = template.get_model()
        query = template.build_edit_query(ctx, model_instance)
        record = query.first() or {}

        # 获取更新字段
        update_fields = template.update_fields(ctx)

        fields = {}

        for field in update_fields:
            name = getattr(field, "name", "")

            value = record.get(name)
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

        # 编辑前回调
        before_editing = getattr(template, "before_editing", None)
        if before_editing:
            data = before_editing(ctx, data)

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

        return ctx.cjson_ok("获取成功", parsed_data)