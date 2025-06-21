from typing import Any, Optional
from .base import Base


class Hidden(Base):

    component: str = "hiddenField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认的选中项。
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
