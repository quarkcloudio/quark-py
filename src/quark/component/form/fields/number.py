from typing import Any, Dict, Optional

from pydantic import model_validator

from .base import Base


class Number(Base):

    component: str = "inputNumberField"
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

    bordered: bool = True
    """
    是否有边框，默认值为 True
    """

    controls: bool = False
    """
    是否显示增减按钮，也可设置自定义箭头图标，默认值为 False
    """

    decimal_separator: Optional[str] = None
    """
    小数点，默认值为 None
    """

    default_value: Optional[Any] = None
    """
    默认的选中项
    """

    disabled: Optional[Any] = None
    """
    禁用
    """

    keyboard: bool = False
    """
    是否启用键盘快捷行为，默认值为 False
    """

    max: Optional[int] = None
    """
    最大值
    """

    min: Optional[int] = None
    """
    最小值
    """

    precision: Optional[int] = None
    """
    数值精度，配置 formatter 时会以 formatter 为准
    """

    read_only: bool = False
    """
    只读，默认值为 False
    """

    status: Optional[str] = None
    """
    设置校验状态,'error' | 'warning'
    """

    prefix: Optional[Any] = None
    """
    带有前缀图标的 input
    """

    size: Optional[str] = None
    """
    控件大小。注：标准表单内的输入框大小限制为 middle，large | middle | small
    """

    step: Optional[Any] = None
    """
    每次改变步数，可以为小数
    """

    string_mode: bool = False
    """
    字符值模式，开启后支持高精度小数。同时 onChange 将返回 string 类型，默认值为 False
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    placeholder: str = "请输入"
    """
    占位符，默认为 "请输入"
    """

    style: Dict[str, Any] = {}
    """
    自定义样式
    """

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        self.set_width(200)
        return self

    def set_addon_after(self, addon_after: Any):
        """
        设置带标签的 input 后置标签。

        Args:
            addon_after (Any): 后置标签信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.addon_after = addon_after
        return self

    def set_addon_before(self, addon_before: Any):
        """
        设置带标签的 input 前置标签。

        Args:
            addon_before (Any): 前置标签信息。

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

    def set_controls(self, controls: bool):
        """
        设置是否显示增减按钮。

        Args:
            controls (bool): 是否显示按钮。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.controls = controls
        return self

    def set_decimal_separator(self, decimal_separator: str):
        """
        设置小数点。

        Args:
            decimal_separator (str): 小数点字符。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.decimal_separator = decimal_separator
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_keyboard(self, keyboard: bool):
        """
        设置是否启用键盘快捷行为。

        Args:
            keyboard (bool): 是否启用。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.keyboard = keyboard
        return self

    def set_max(self, max: int):
        """
        设置最大值。

        Args:
            max (int): 最大值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.max = max
        return self

    def set_min(self, min: int):
        """
        设置最小值。

        Args:
            min (int): 最小值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.min = min
        return self

    def set_precision(self, precision: int):
        """
        设置数值精度。

        Args:
            precision (int): 精度值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.precision = precision
        return self

    def set_read_only(self, read_only: bool):
        """
        设置只读状态。

        Args:
            read_only (bool): 是否只读。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.read_only = read_only
        return self

    def set_status(self, status: str):
        """
        设置校验状态。

        Args:
            status (str): 状态，如 'error', 'warning'。

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
            prefix (Any): 前缀图标信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.prefix = prefix
        return self

    def set_size(self, size: str):
        """
        设置控件大小。

        Args:
            size (str): 大小，如 'large', 'middle', 'small'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_step(self, step: Any):
        """
        设置每次改变步数。

        Args:
            step (Any): 步数，可以为小数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.step = step
        return self

    def set_string_mode(self, string_mode: bool):
        """
        设置字符值模式。

        Args:
            string_mode (bool): 是否开启字符值模式。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.string_mode = string_mode
        return self
