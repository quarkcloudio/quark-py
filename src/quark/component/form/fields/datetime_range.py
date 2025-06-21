from typing import Dict, Any, List, Optional
from .base import Base


class DatetimeRange(Base):

    component: str = "datetimeRangeField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    是否支持清除，默为 True
    """

    auto_focus: bool = False
    """
    是否自动获取焦点，默为 False
    """

    bordered: bool = True
    """
    是否有边框，默为 True
    """

    class_name: Optional[str] = None
    """
    自定义类名
    """

    default_value: Optional[Any] = [None, None]
    """
    默认的选中项
    """

    disabled: Optional[Any] = None
    """
    是否禁用
    """

    format: str = "YYYY-MM-DD HH:mm:ss"
    """
    日期格式，默为 "YYYY-MM-DD HH:mm:ss"
    """

    popup_class_name: Optional[str] = None
    """
    额外的弹出日历 className
    """

    input_read_only: bool = False
    """
    输入框是否只读，默为 False
    """

    locale: Optional[Any] = None
    """
    国际化配置
    """

    mode: Optional[str] = None
    """
    日期面板的状态
    """

    next_icon: Optional[Any] = None
    """
    自定义下一个图标
    """

    open: bool = None
    """
    浮层是否显隐，默为 False
    """

    picker: Optional[str] = None
    """
    选择器类型
    """

    placeholder: List[str] = ["开始时间", "结束时间"]
    """
    输入框占位文本，默为 ["开始时间", "结束时间"]
    """

    placement: Optional[str] = None
    """
    浮层预设位置
    """

    popup_style: Optional[Any] = None
    """
    额外的弹出日历样式
    """

    prev_icon: Optional[Any] = None
    """
    自定义上一个图标
    """

    size: Optional[str] = None
    """
    输入框大小
    """

    status: Optional[str] = None
    """
    校验状态
    """

    style: Optional[Dict[str, Any]] = None
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

    default_picker_value: Optional[str] = None
    """
    默认面板日期
    """

    show_now: bool = False
    """
    面板是否显示“此刻”按钮，默为 False
    """

    show_time: Optional[Any] = None
    """
    是否增加时间选择功能
    """

    show_today: bool = False
    """
    是否展示“今天”按钮，默为 False
    """

    def set_allow_clear(self, allow_clear: bool):
        """
        设置是否支持清除

        Args:
            allow_clear (bool): 是否支持清除

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.allow_clear = allow_clear
        return self

    def set_auto_focus(self, auto_focus: bool):
        """
        设置是否自动获取焦点

        Args:
            auto_focus (bool): 是否自动获取焦点

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.auto_focus = auto_focus
        return self

    def set_bordered(self, bordered: bool):
        """
        设置是否有边框

        Args:
            bordered (bool): 是否有边框

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.bordered = bordered
        return self

    def set_class_name(self, class_name: str):
        """
        设置自定义类名

        Args:
            class_name (str): 自定义类名

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.class_name = class_name
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_format(self, format_str: str):
        """
        设置日期格式

        Args:
            format_str (str): 日期格式字符串

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.format = format_str
        return self

    def set_popup_class_name(self, popup_class_name: str):
        """
        设置额外的弹出日历 className

        Args:
            popup_class_name (str): className 字符串

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.popup_class_name = popup_class_name
        return self

    def set_input_read_only(self, input_read_only: bool):
        """
        设置输入框为只读

        Args:
            input_read_only (bool): 是否只读

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.input_read_only = input_read_only
        return self

    def set_locale(self, locale: Any):
        """
        设置国际化配置

        Args:
            locale (Any): 国际化配置信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.locale = locale
        return self

    def set_mode(self, mode: str):
        """
        设置日期面板的状态

        Args:
            mode (str): 状态字符串，如 'time', 'date' 等

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.mode = mode
        return self

    def set_next_icon(self, next_icon: Any):
        """
        设置自定义下一个图标

        Args:
            next_icon (Any): 图标信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.next_icon = next_icon
        return self

    def set_open(self, open_flag: bool):
        """
        控制浮层显隐

        Args:
            open_flag (bool): 是否显示浮层

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.open = open_flag
        return self

    def set_picker(self, picker: str):
        """
        设置选择器类型

        Args:
            picker (str): 选择器类型字符串，如 'date', 'week' 等

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.picker = picker
        return self

    def set_placeholder(self, placeholder: List[str]):
        """
        设置输入框占位文本

        Args:
            placeholder (List[str]): 占位文本列表

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str):
        """
        设置浮层预设位置

        Args:
            placement (str): 预设位置字符串，如 'bottomLeft', 'bottomRight' 等

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.placement = placement
        return self

    def set_popup_style(self, popup_style: Any):
        """
        设置额外的弹出日历样式

        Args:
            popup_style (Any): 样式信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.popup_style = popup_style
        return self

    def set_prev_icon(self, prev_icon: Any):
        """
        设置自定义上一个图标

        Args:
            prev_icon (Any): 图标信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.prev_icon = prev_icon
        return self

    def set_size(self, size: str):
        """
        设置输入框大小

        Args:
            size (str): 大小字符串，如 'large', 'middle', 'small'

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.size = size
        return self

    def set_status(self, status: str):
        """
        设置校验状态

        Args:
            status (str): 校验状态字符串，如 'error', 'warning'

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any):
        """
        设置自定义的选择框后缀图标

        Args:
            suffix_icon (Any): 图标信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.suffix_icon = suffix_icon
        return self

    def set_super_next_icon(self, super_next_icon: Any):
        """
        设置自定义 << 切换图标

        Args:
            super_next_icon (Any): 图标信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.super_next_icon = super_next_icon
        return self

    def set_super_prev_icon(self, super_prev_icon: Any):
        """
        设置自定义 >> 切换图标

        Args:
            super_prev_icon (Any): 图标信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.super_prev_icon = super_prev_icon
        return self

    def set_default_picker_value(self, default_picker_value: str):
        """
        设置默认面板日期

        Args:
            default_picker_value (str): 默认面板日期字符串

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.default_picker_value = default_picker_value
        return self

    def set_show_now(self, show_now: bool):
        """
        设置当设定了 show_time 时，面板是否显示“此刻”按钮

        Args:
            show_now (bool): 是否显示“此刻”按钮

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.show_now = show_now
        return self

    def set_show_time(self, show_time: Any):
        """
        设置增加时间选择功能

        Args:
            show_time (Any): 时间选择功能信息

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.show_time = show_time
        return self

    def set_show_today(self, show_today: bool):
        """
        设置是否展示“今天”按钮

        Args:
            show_today (bool): 是否展示“今天”按钮

        Returns:
            Component: 当前组件实例，支持链式调用
        """
        self.show_today = show_today
        return self
