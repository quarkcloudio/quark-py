from typing import Dict, Any, Optional
from pydantic import model_validator
from .base import Base


class Editor(Base):

    component: str = "editorField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认选中的选项
    """

    disabled: bool = False
    """
    整组失效
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    @model_validator(mode="after")
    def init(self):
        self.style = {"height": 500, "width": "100%"}
        self.set_key()
        return self

    def set_width(self, width: Any):
        """
        设置组件宽度。

        Args:
            width (Any): 宽度值。

        Returns:
            Component: 当前组件实例，支持链式调用。
        """
        style = self.style.copy() if self.style else {}
        style["width"] = width
        self.style = style
        return self

    def set_height(self, height: Any):
        """
        设置组件高度。

        Args:
            height (Any): 高度值。

        Returns:
            Component: 当前组件实例，支持链式调用。
        """
        style = self.style.copy() if self.style else {}
        style["height"] = height
        self.style = style
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
