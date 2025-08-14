from typing import Any, Optional

from .action import Action


class Switch(Action):
    """
    表示一个开关组件，用于切换状态。
    """

    # 选中时的内容
    checked_children: Optional[Any] = None

    # 未选中时的内容
    unchecked_children: Optional[Any] = None

    # 字段名称
    field_name: Optional[Any] = None

    # 字段值
    field_value: Optional[Any] = None

    def __init__(self):
        self.action_type = "switch"

    def get_checked_children(self) -> Optional[Any]:
        """获取选中时的内容"""
        return self.checked_children

    def get_unchecked_children(self) -> Optional[Any]:
        """获取未选中时的内容"""
        return self.unchecked_children

    def get_field_name(self) -> Optional[Any]:
        """获取字段名称"""
        return self.field_name

    def get_field_value(self) -> Optional[Any]:
        """获取字段值"""
        return self.field_value
