from typing import Any, Optional
from .base import Base


class ID(Base):

    component: str = "idField"
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

    on_index_displayed: bool = True
    """
    在列表页显示字段，默认 True
    """

    on_detail_displayed: bool = True
    """
    在详情页显示字段，默认 True
    """

    on_form_displayed: bool = True
    """
    在表单页显示控件，默认 True
    """

    on_export_displayed: bool = True
    """
    在导出页显示字段，默认 True
    """

    def init(self):
        """
        初始化组件属性。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.component = "idField"
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.on_index_displayed = True
        self.show_on_import = False

        return self

    def set_on_index_displayed(self, displayed: bool):
        """
        在列表页是否显示字段。

        Args:
            displayed (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.on_index_displayed = displayed
        return self

    def set_on_detail_displayed(self, displayed: bool):
        """
        在详情页是否显示字段。

        Args:
            displayed (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.on_detail_displayed = displayed
        return self

    def set_on_form_displayed(self, displayed: bool):
        """
        在表单页是否显示控件。

        Args:
            displayed (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.on_form_displayed = displayed
        return self

    def set_on_export_displayed(self, displayed: bool):
        """
        在导出页是否显示字段。

        Args:
            displayed (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.on_export_displayed = displayed
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
