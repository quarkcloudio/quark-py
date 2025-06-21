from typing import Dict, Any, Optional
from .base import Base


class Display(Base):

    component: str = "displayField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认的选中项
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式
    """

    value: Optional[Any] = None
    """
    指定选中项,string[] | number[]
    """

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
