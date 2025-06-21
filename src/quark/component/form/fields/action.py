from typing import Any
from .base import Base


class Action(Base):

    component: str = "actionField"
    """
    组件名称
    """

    def set_items(self, items: Any):
        """设置行为项。"""
        self.items = items
        return self
