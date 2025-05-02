from dataclasses import dataclass
from typing import Any, Optional
from quark_go_v3 import Context, Action


@dataclass
class Switch(Action):
    """
    表示一个开关组件，用于切换状态。
    """
    checked_children: Optional[Any] = None  # 选中时的内容
    unchecked_children: Optional[Any] = None  # 未选中时的内容
    field_name: Optional[Any] = None  # 字段名称
    field_value: Optional[Any] = None  # 字段值

    def new(self, ctx: Context) -> "Switch":
        """
        初始化方法。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            Switch: 返回当前实例。
        """
        self.action_type = "switch"
        return self

    @property
    def get_checked_children(self) -> Optional[Any]:
        """获取选中时的内容"""
        return self.checked_children

    @property
    def get_unchecked_children(self) -> Optional[Any]:
        """获取未选中时的内容"""
        return self.unchecked_children

    @property
    def get_field_name(self) -> Optional[Any]:
        """获取字段名称"""
        return self.field_name

    @property
    def get_field_value(self) -> Optional[Any]:
        """获取字段值"""
        return self.field_value