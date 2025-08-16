from typing import Any, List, Optional
from ...component import Component
from .base import Base
import re


class Option(Component):
    label: str  # 选项显示文本
    value: Any  # 选项值
    disabled: bool = False  # 是否禁用


class Checkbox(Base):

    component: str = "checkboxField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认值
    """

    disabled: bool = False
    """
    是否禁用
    """

    value: Optional[Any] = None
    """
    当前值
    """

    options: List[Option] = []
    """
    选项列表
    """

    def get_options(self) -> List[Option]:
        """
        获取当前可选项。

        Returns:
            List[Option]: 可选项列表。
        """
        return self.options

    def build_options(
        self, items: List[Any], label_name: str, value_name: str
    ) -> List[Option]:
        """通过反射构建选项列表"""
        options = []
        for item in items:
            try:
                value = getattr(item, value_name)
                label = getattr(item, label_name)
            except AttributeError:
                continue
            options.append(Option(label=label, value=value))
        return options

    def list_to_options(
        self, items: List[Any], label_name: str, value_name: str
    ) -> List[Option]:
        """从列表中构建选项"""
        return self.build_options(items, label_name, value_name)

    def set_options(self, *args):
        """设置选项"""
        if len(args) == 1 and isinstance(args[0], list):
            self.options = args[0]
        elif len(args) == 3:
            self.options = self.list_to_options(*args)
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def get_option_label(self, value: Any) -> str:
        """根据值获取标签"""
        labels = [opt.label for opt in self.options if opt.value == value]
        return ", ".join(labels)

    def get_option_value(self, label: str) -> Any:
        """根据标签获取值"""
        labels = re.split(r"[,，]", label)
        values = [opt.value for opt in self.options if opt.label in labels]
        return values if len(values) > 1 else values[0] if values else None

    def get_option_labels(self) -> str:
        """获取所有标签"""
        return ", ".join(opt.label for opt in self.options)
