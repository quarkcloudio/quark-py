from typing import Any
from .base import Base


class Selects(Base):

    component: str = "selects"
    """
    组件名称
    """

    body: Any
    """
    组件内容
    """

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
