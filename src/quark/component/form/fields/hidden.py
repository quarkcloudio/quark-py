from typing import Any, Optional
from .base import Base

class Hidden(Base):

    component: str = "hiddenField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认的选中项。
    """

    value: Optional[Any] = None
    """
    指定选中项
    """