from typing import Any, Optional
from .base import Base


class Group(Base):

    component: str = "groupField"
    """
    组件名称
    """

    title: Optional[str] = None
    """
    分组标题
    """

    body: Optional[Any] = None
    """
    组件内容
    """

    size: int = 32
    """
    子元素个数，默认 32
    """

    def set_title(self, title: str):
        """
        设置分组标题。

        Args:
            title (str): 分组标题内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.title = title
        return self

    def set_body(self, body: Any):
        """
        设置组件内容。

        Args:
            body (Any): 组件内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.body = body
        return self

    def set_size(self, size: int):
        """
        设置子元素个数。

        Args:
            size (int): 子元素个数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self
