from typing import Any, List, Optional

from quark import Request

from ...component.form.fields.cascader import Option
from .search import Search


class Cascader(Search):
    """级联选择搜索字段配置类"""

    cascader_options: List[Option] = None

    def __init__(self, column: str = "", name: str = ""):
        self.component = "cascaderField"
        return self

    def option(self, label: str, value: Any) -> Option:
        """
        创建一个选项对象

        :param label: 显示名称
        :param value: 值
        :return: Option 对象
        """
        return Option(value=value, label=label)

    def set_options(self, *options: Any) -> "Cascader":
        """
        设置可选项数据源

        支持以下几种调用方式：

        - set_options([Option(...), Option(...)])
        - set_options(options_list, parent_key, label_name, value_name)
        - set_options(options_list, level, parent_key, label_name, value_name)

        :param options: 可变参数，根据参数数量判断处理逻辑
        :return: Cascader 实例
        """
        if len(options) == 1 and isinstance(options[0], list):
            self.cascader_options = options[0]
        elif len(options) == 4:
            options_list, parent_key, label_name, value_name = options
            self.cascader_options = Option.list_to_options(
                options_list, 0, parent_key, label_name, value_name
            )
        elif len(options) == 5:
            options_list, level, parent_key, label_name, value_name = options
            self.cascader_options = Option.list_to_options(
                options_list, level, parent_key, label_name, value_name
            )
        else:
            raise ValueError("Unsupported number of arguments in set_options")

        return self

    def get_cascader_options(self) -> List[Option]:
        """获取级联选项数据"""
        return self.cascader_options

    def apply(self, request: Request, query: Any, value: Any) -> Any:
        """执行查询逻辑，子类可重写此方法"""
        return super().apply(request, query, value)

    def options(self, request: Request) -> Optional[Any]:
        """扩展属性选项"""
        return super().options(request)
