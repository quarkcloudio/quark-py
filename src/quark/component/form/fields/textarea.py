from typing import Dict, Optional, Any
from .base import Base


class Textarea(Base):

    component: str = "textAreaField"
    """
    组件名称
    """

    addon_after: Optional[Any] = None
    """
    带标签的 input，设置后置标签
    """

    addon_before: Optional[Any] = None
    """
    带标签的 input，设置前置标签
    """

    allow_clear: bool = False
    """
    可以点击清除图标删除内容，默认值为 False
    """

    auto_size: Optional[Any] = None
    """
    自适应内容高度，可设置为 true | false 或对象：{ minRows: 2, maxRows: 6 }，默认值为 None
    """

    bordered: bool = True
    """
    是否有边框，默认值为 True
    """

    default_value: Optional[Any] = None
    """
    默认的选中项，默认值为 None
    """

    disabled: bool = False
    """
    禁用，默认值为 False
    """

    id: Optional[str] = None
    """
    输入框的 id，默认值为 None
    """

    max_length: int = 200
    """
    最大长度，默认值为 200
    """

    show_count: bool = False
    """
    是否展示字数，默认值为 False
    """

    status: Optional[str] = None
    """
    设置校验状态,'error' | 'warning'，默认值为 None
    """

    prefix: Optional[Any] = None
    """
    带有前缀图标的 input，默认值为 None
    """

    size: Optional[str] = None
    """
    控件大小。注：标准表单内的输入框大小限制为 middle，large | middle | small，默认值为 None
    """

    suffix: Optional[Any] = None
    """
    带有后缀图标的 input，默认值为 None
    """

    type: Optional[str] = None
    """
    声明 input 类型，同原生 input 标签的 type 属性，默认值为 None
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    placeholder: str = "请输入"
    """
    占位符，默认值为 "请输入"
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式
    """

    rows: int = None
    """
    用于多行输入
    """

    def set_addon_after(self, addon_after: Any):
        """
        设置带标签 input 的后置标签。

        Args:
            addon_after (Any): 后置标签。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.addon_after = addon_after
        return self

    def set_addon_before(self, addon_before: Any):
        """
        设置带标签 input 的前置标签。

        Args:
            addon_before (Any): 前置标签。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.addon_before = addon_before
        return self

    def set_allow_clear(self, allow_clear: bool):
        """
        设置是否可以点击清除图标删除内容。

        Args:
            allow_clear (bool): 是否允许清除。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.allow_clear = allow_clear
        return self

    def set_auto_size(self, auto_size: Any):
        """
        设置自适应内容高度。

        Args:
            auto_size (Any): 自适应设置。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.auto_size = auto_size
        return self

    def set_bordered(self, bordered: bool):
        """
        设置是否有边框。

        Args:
            bordered (bool): 是否有边框。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.bordered = bordered
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_id(self, id_str: str):
        """
        设置输入框的 id。

        Args:
            id_str (str): 输入框 id。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.id = id_str
        return self

    def set_max_length(self, max_length: int):
        """
        设置最大长度。

        Args:
            max_length (int): 最大长度值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.max_length = max_length
        return self

    def set_show_count(self, show_count: bool):
        """
        设置是否展示字数。

        Args:
            show_count (bool): 是否展示字数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_count = show_count
        return self

    def set_status(self, status: str):
        """
        设置校验状态。

        Args:
            status (str): 校验状态，'error' | 'warning'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.status = status
        return self

    def set_placeholder(self, placeholder: str):
        """
        设置输入框占位文本。

        Args:
            placeholder (str): 占位文本。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placeholder = placeholder
        return self

    def set_prefix(self, prefix: Any):
        """
        设置带有前缀图标的 input。

        Args:
            prefix (Any): 前缀图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.prefix = prefix
        return self

    def set_size(self, size: str):
        """
        设置控件大小。

        Args:
            size (str): 控件大小，large | middle | small。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_suffix(self, suffix: Any):
        """
        设置带有后缀图标的 input。

        Args:
            suffix (Any): 后缀图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.suffix = suffix
        return self

    def set_type(self, input_type: str):
        """
        设置 input 类型。

        Args:
            input_type (str): input 类型。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.type = input_type
        return self

    def set_rows(self, rows: int):
        """
        设置多行输入的行数。

        Args:
            rows (int): 行数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.rows = rows
        return self
