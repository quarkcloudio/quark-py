from typing import Optional, Any
from .base import Base


class Space(Base):

    component: str = "spaceField"
    """
    组件名称
    """

    align: str = ""
    """
    对齐方式，start | end | center | baseline，默认值为 ""
    """

    direction: str = ""
    """
    间距方向，默认值为 ""
    """

    size: str = ""
    """
    间距大小，默认值为 ""
    """

    split: str = ""
    """
    设置拆分，默认值为 ""
    """

    wrap: bool = False
    """
    是否自动换行，仅在 horizontal 时有效，默认值为 False
    """

    body: Optional[Any] = None
    """
    组件内容，默认值为 None
    """

    def set_align(self, align: str):
        """
        设置对齐方式。

        Args:
            align (str): 对齐方式，如 'start', 'end', 'center', 'baseline'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.align = align
        return self

    def set_direction(self, direction: str):
        """
        设置间距方向。

        Args:
            direction (str): 间距方向。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.direction = direction
        return self

    def set_size(self, size: str):
        """
        设置间距大小。

        Args:
            size (str): 间距大小，如 'small', 'middle', 'large' 或数字。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_split(self, split: str):
        """
        设置拆分卡片的方向。

        Args:
            split (str): 拆分方向，如 'vertical', 'horizontal'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.split = split
        return self

    def set_wrap(self, wrap: bool):
        """
        设置是否自动换行。

        Args:
            wrap (bool): 是否自动换行。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.wrap = wrap
        return self

    def set_body(self, body: Any):
        """
        设置容器控件里面的内容。

        Args:
            body (Any): 组件内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.body = body
        return self
