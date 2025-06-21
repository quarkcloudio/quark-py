from pydantic import model_validator
from typing import Any, Optional
from .base import Base


class Compact(Base):

    component: str = "compactField"
    """
    组件名称
    """

    block: bool = False
    """
    将宽度调整为父元素宽度的选项,默认值false"
    """

    direction: str = None
    """
    间距方向
    """

    size: str = None
    """
    间距大小
    """

    body: Optional[Any] = None
    """
    组件内容
    """

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        self.only_on_forms()
        return self

    def set_block(self, block: bool):
        """
        设置是否将宽度调整为父元素宽度。
        :param block: 是否调整的布尔值
        :return: 当前组件实例
        """
        self.block = block
        return self

    def set_direction(self, direction: str):
        """
        设置间距方向。
        :param direction: 间距方向字符串
        :return: 当前组件实例
        """
        self.direction = direction
        return self

    def set_size(self, size: str):
        """
        设置间距大小。
        :param size: 间距大小字符串
        :return: 当前组件实例
        """
        self.size = size
        return self

    def set_body(self, body: Any):
        """
        设置容器控件里面的内容。
        :param body: 组件内容
        :return: 当前组件实例
        """
        self.body = body
        return self
