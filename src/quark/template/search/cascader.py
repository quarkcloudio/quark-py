from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from searches.base import Search  # 假设你已有一个 Search 基类
from component.form.fields.cascader import Option as CascaderOption


@dataclass
class Cascader(Search):
    """级联选择搜索字段配置类"""

    cascader_options: List[CascaderOption] = None

    def __post_init__(self):
        self.component = "cascaderField"
        if self.cascader_options is None:
            self.cascader_options = []

    def new(self, ctx: Any) -> "Cascader":
        """加载初始化数据"""
        self.component = "cascaderField"
        return self

    def init(self, ctx: Any) -> "Cascader":
        """初始化"""
        return self

    def option(self, label: str, value: Any) -> CascaderOption:
        """
        创建一个选项对象

        :param label: 显示名称
        :param value: 值
        :return: CascaderOption 对象
        """
        return CascaderOption(value=value, label=label)

    def set_options(self, *options: Any) -> "Cascader":
        """
        设置可选项数据源

        支持以下几种调用方式：

        - set_options([CascaderOption(...), CascaderOption(...)])
        - set_options(options_list, parent_key, label_name, value_name)
        - set_options(options_list, level, parent_key, label_name, value_name)

        :param options: 可变参数，根据参数数量判断处理逻辑
        :return: Cascader 实例
        """
        if len(options) == 1 and isinstance(options[0], list):
            self.cascader_options = options[0]
        elif len(options) == 4:
            options_list, parent_key, label_name, value_name = options
            self.cascader_options = CascaderOption.list_to_options(
                options_list, 0, parent_key, label_name, value_name
            )
        elif len(options) == 5:
            options_list, level, parent_key, label_name, value_name = options
            self.cascader_options = CascaderOption.list_to_options(
                options_list, level, parent_key, label_name, value_name
            )
        else:
            raise ValueError("Unsupported number of arguments in set_options")

        return self

    def get_cascader_options(self) -> List[CascaderOption]:
        """获取级联选项数据"""
        return self.cascader_options

    def apply(self, ctx: Any, query: Any, value: Any) -> Any:
        """执行查询逻辑，子类可重写此方法"""
        return super().apply(ctx, query, value)

    def options(self, ctx: Any) -> Optional[Any]:
        """扩展属性选项"""
        return super().options(ctx)