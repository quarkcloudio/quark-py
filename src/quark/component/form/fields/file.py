from typing import Dict, Any, Optional, List
from .base import Base


class File(Base):

    component: str = "fileField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认选中的选项
    """

    disabled: bool = False
    """
    整组是否失效，默认为 False
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    button: str = "上传文件"
    """
    上传按钮标识，默认为 "上传文件"
    """

    limit_size: int = 2
    """
    上传文件大小限制，默认为 2
    """

    limit_type: List[str] = ["jpeg", "png", "doc", "docx"]
    """
    上传文件类型限制，默认为 ["jpeg", "png", "doc", "docx"]
    """

    limit_num: int = 3
    """
    上传文件数量限制，默认为 3
    """

    limit_wh: Dict[str, int] = {}
    """
    上传图片宽高限制
    """

    def set_limit_size(self, limit_size: int):
        """
        设置上传文件大小限制。

        Args:
            limit_size (int): 大小限制值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.limit_size = limit_size
        return self

    def set_limit_type(self, limit_type: List[str]):
        """
        设置上传文件类型限制。

        Args:
            limit_type (List[str]): 类型限制列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.limit_type = limit_type
        return self

    def set_limit_num(self, limit_num: int):
        """
        设置上传文件数量限制。

        Args:
            limit_num (int): 数量限制值。

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

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
