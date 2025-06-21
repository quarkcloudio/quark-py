from typing import Any, Optional
from .base import Base


class ImagePicker(Base):

    component: str = "imagePickerField"
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

    mode: str = "single"
    """
    上传模式，单图或多图，single|multiple
    """

    button: str = "上传图片"
    """
    上传按钮标识
    """

    limit_num: int = 3
    """
    上传文件数量限制
    """

    size: str = ""
    """
    按钮大小，default、small
    """

    def set_mode(self, v):
        """
        验证上传模式是否合法。

        Args:
            v (str): 上传模式。

        Returns:
            str: 合法的上传模式。

        Raises:
            ValueError: 当上传模式不合法时抛出异常。
        """
        if v == "s":
            v = "single"
        if v == "m":
            v = "multiple"
        limits = ["single", "multiple"]
        if v not in limits:
            raise ValueError("argument must be in 'single', 'multiple'!")
        self.mode = v
        return v

    def set_limit_num(self, limit_num: int):
        """
        设置上传文件数量限制。

        Args:
            limit_num (int): 上传文件数量限制值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.limit_num = limit_num
        return self

    def set_button(self, text: str):
        """
        设置上传按钮的标题。

        Args:
            text (str): 按钮标题。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.button = text
        return self

    def set_size(self, size: str):
        """
        设置按钮大小。

        Args:
            size (str): 按钮大小，如 'default', 'small'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
