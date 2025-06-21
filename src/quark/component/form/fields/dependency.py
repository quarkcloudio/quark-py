from typing import List
from .base import Base


class Dependency(Base):

    component: str = "dependencyField"
    """
    组件名称
    """

    ignore_form_list_field: bool = False
    """
    是否忽略 FormList 上的字段，默为 False
    """

    names: List[str] = []
    """
    组件内容
    """

    def set_ignore_form_list_field(self, ignore_form_list_field: bool):
        """
        忽略 FormList 上的字段。

        Args:
            ignore_form_list_field (bool): 是否忽略。

        Returns:
            Component: 当前组件实例，支持链式调用。
        """
        self.ignore_form_list_field = ignore_form_list_field
        return self
