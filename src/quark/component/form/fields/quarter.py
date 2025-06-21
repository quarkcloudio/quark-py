from typing import Dict, Optional, Any
from .base import Base


class Quarter(Base):

    component: str = "quarterField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    是否支持清除，默认值为 True
    """

    auto_focus: bool = False
    """
    自动获取焦点，默认值为 False
    """

    bordered: bool = True
    """
    是否有边框，默认值为 True
    """

    class_name: str = ""
    """
    自定义类名
    """

    default_value: Optional[Any] = None
    """
    默认的选中项
    """

    disabled: Optional[Any] = None
    """
    禁用
    """

    format: str = ""
    """
    设置日期格式，为数组时支持多格式匹配，展示以第一个为准
    """

    popup_class_name: str = ""
    """
    额外的弹出日历 className
    """

    input_read_only: bool = False
    """
    设置输入框为只读（避免在移动设备上打开虚拟键盘）
    """

    locale: Optional[Any] = None
    """
    国际化配置
    """

    mode: str = ""
    """
    日期面板的状态 time | date | month | year | decade
    """

    next_icon: Optional[Any] = None
    """
    自定义下一个图标
    """

    open: bool = False
    """
    控制浮层显隐
    """

    picker: str = ""
    """
    设置选择器类型 date | week | month | quarter | year
    """

    placeholder: str = "请选择"
    """
    输入框占位文本，默认为 "请选择"
    """

    placement: str = ""
    """
    浮层预设位置，bottomLeft bottomRight topLeft topRight
    """

    popup_style: Optional[Any] = None
    """
    额外的弹出日历样式
    """

    prev_icon: Optional[Any] = None
    """
    自定义上一个图标
    """

    size: str = ""
    """
    输入框大小，large | middle | small
    """

    status: str = ""
    """
    设置校验状态，'error' | 'warning'
    """

    style: Dict[str, Any] = {}
    """
    自定义样式
    """

    suffix_icon: Optional[Any] = None
    """
    自定义的选择框后缀图标
    """

    super_next_icon: Optional[Any] = None
    """
    自定义 << 切换图标
    """

    super_prev_icon: Optional[Any] = None
    """
    自定义 >> 切换图标
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    default_picker_value: str = ""
    """
    默认面板日期
    """

    show_now: bool = False
    """
    当设定了 show_time 的时候，面板是否显示“此刻”按钮
    """

    show_time: Optional[Any] = None
    """
    增加时间选择功能
    """

    show_today: bool = False
    """
    是否展示“今天”按钮
    """

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

    def set_auto_focus(self, auto_focus: bool):
        """
        设置是否自动获取焦点。

        Args:
            auto_focus (bool): 是否自动获取焦点。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.auto_focus = auto_focus
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

    def set_class_name(self, class_name: str):
        """
        设置自定义类名。

        Args:
            class_name (str): 类名。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.class_name = class_name
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_format(self, format: str):
        """
        设置日期格式。

        Args:
            format (str): 日期格式。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.format = format
        return self

    def set_popup_class_name(self, popup_class_name: str):
        """
        设置额外的弹出日历 className。

        Args:
            popup_class_name (str): className。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.popup_class_name = popup_class_name
        return self

    def set_input_read_only(self, input_read_only: bool):
        """
        设置输入框为只读。

        Args:
            input_read_only (bool): 是否只读。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.input_read_only = input_read_only
        return self

    def set_locale(self, locale: Any):
        """
        设置国际化配置。

        Args:
            locale (Any): 国际化配置信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.locale = locale
        return self

    def set_mode(self, mode: str):
        """
        设置日期面板的状态。

        Args:
            mode (str): 状态，如 'time', 'date', 'month', 'year', 'decade'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.mode = mode
        return self

    def set_next_icon(self, next_icon: Any):
        """
        设置自定义下一个图标。

        Args:
            next_icon (Any): 图标信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.next_icon = next_icon
        return self

    def set_open(self, open: bool):
        """
        控制浮层显隐。

        Args:
            open (bool): 是否打开。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.open = open
        return self

    def set_picker(self, picker: str):
        """
        设置选择器类型。

        Args:
            picker (str): 选择器类型，如 'date', 'week', 'month', 'quarter', 'year'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.picker = picker
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

    def set_placement(self, placement: str):
        """
        设置浮层预设位置。

        Args:
            placement (str): 位置，如 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placement = placement
        return self

    def set_popup_style(self, popup_style: Any):
        """
        设置额外的弹出日历样式。

        Args:
            popup_style (Any): 样式信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.popup_style = popup_style
        return self

    def set_prev_icon(self, prev_icon: Any):
        """
        设置自定义上一个图标。

        Args:
            prev_icon (Any): 图标信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.prev_icon = prev_icon
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

    def set_suffix_icon(self, suffix_icon: Any):
        """
        设置自定义的选择框后缀图标。

        Args:
            suffix_icon (Any): 图标信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.suffix_icon = suffix_icon
        return self

    def set_super_next_icon(self, super_next_icon: Any):
        """
        设置自定义 << 切换图标。

        Args:
            super_next_icon (Any): 图标信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.super_next_icon = super_next_icon
        return self

    def set_super_prev_icon(self, super_prev_icon: Any):
        """
        设置自定义 >> 切换图标。

        Args:
            super_prev_icon (Any): 图标信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.super_prev_icon = super_prev_icon
        return self

    def set_default_picker_value(self, default_picker_value: str):
        """
        设置默认面板日期。

        Args:
            default_picker_value (str): 默认面板日期。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_picker_value = default_picker_value
        return self

    def set_show_now(self, show_now: bool):
        """
        设置当设定了 show_time 的时候，面板是否显示“此刻”按钮。

        Args:
            show_now (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_now = show_now
        return self

    def set_show_time(self, show_time: Any):
        """
        设置增加时间选择功能。

        Args:
            show_time (Any): 时间选择功能信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_time = show_time
        return self

    def set_show_today(self, show_today: bool):
        """
        设置是否展示“今天”按钮。

        Args:
            show_today (bool): 是否展示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_today = show_today
        return self
