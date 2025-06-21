from typing import Any, Optional
from .base import Base


class List(Base):

    component: str = "listField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认的选中项
    """

    disabled: bool = False
    """
    整组失效，默认 False
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    items: Optional[Any] = None
    """
    列表项
    """

    button_text: str = "添加一行数据"
    """
    按钮文字，默认 "添加一行数据"
    """

    button_position: str = "top"
    """
    按钮位置，默认 "top"
    """

    always_show_item_label: bool = True
    """
    Item 中总是展示 label，默认 True
    """

    def set_button(self, text: str, position: str):
        """
        设置按钮文字和位置。

        Args:
            text (str): 按钮文字。
            position (str): 按钮位置。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.button_text = text
        self.button_position = position
        return self

    def set_item(self, callback: Any):
        """
        设置表单项。

        Args:
            callback (Any): 回调函数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if callable(callback):
            self.items = callback()
        return self

    def set_always_show_item_label(self, always_show_item_label: bool):
        """
        设置 Item 中是否总是展示 label。

        Args:
            always_show_item_label (bool): 是否总是展示 label。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.always_show_item_label = always_show_item_label
        return self

    def set_api(self, api: str):
        """
        设置上传的 api 接口。

        Args:
            api (str): api 接口地址。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.api = api
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
