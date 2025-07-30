from typing import Dict, Any, Optional, List
from .base import Base


class Image(Base):

    component: str = "imageField"
    """
    组件名称
    """

    api: Optional[str] = "/api/admin/upload/image/handle"
    """
    上传接口地址
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

    limit_size: int = 2
    """
    上传文件大小限制
    """

    limit_type: List[str] = ["image/jpeg", "image/png"]
    """
    上传文件类型限制
    """

    limit_num: int = 3
    """
    上传文件数量限制
    """

    limit_w_h: Dict[str, int] = {"width": 0, "height": 0}
    """
    上传图片宽高限制
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

    def set_limit_size(self, limit_size: int):
        """
        设置上传文件大小限制。

        Args:
            limit_size (int): 上传文件大小限制值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.limit_size = limit_size
        return self

    def set_limit_type(self, limit_type: List[str]):
        """
        设置上传文件类型限制。

        Args:
            limit_type (List[str]): 上传文件类型列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.limit_type = limit_type
        return self

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

    def set_limit_wh(self, width: int, height: int):
        """
        设置上传图片宽高限制。

        Args:
            width (int): 图片宽度限制。
            height (int): 图片高度限制。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.limit_w_h = {"width": width, "height": height}
        return self

    def set_api(self, api: str):
        """
        设置上传的 api 接口。

        Args:
            api (str): 接口地址。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.api = api
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

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
