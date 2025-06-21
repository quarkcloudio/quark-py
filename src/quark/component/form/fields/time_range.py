from typing import Dict, List, Optional, Any
from .base import Base


class TimeRange(Base):

    component: str = "timeRangeField"
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

    class_name: Optional[str] = None
    """
    自定义类名，默认值为 None
    """

    clear_icon: Optional[Any] = None
    """
    自定义的清除图标，默认值为 None
    """

    clear_text: Optional[str] = None
    """
    清除按钮的提示文案，默认值为 None
    """

    default_value: Optional[Any] = None
    """
    默认的选中项，默认值为 None
    """

    disabled: Optional[Any] = None
    """
    禁用，默认值为 None
    """

    disabled_time: Optional[Any] = None
    """
    不可选择的时间，默认值为 None
    """

    format: Optional[str] = "HH:mm"
    """
    设置日期格式，为数组时支持多格式匹配，展示以第一个为准，默认值为 "HH:mm"
    """

    hide_disabled_options: bool = False
    """
    隐藏禁止选择的选项，默认值为 False
    """

    hour_step: int = 0
    """
    小时选项间隔，默认值为 0
    """

    input_read_only: bool = False
    """
    设置输入框为只读（避免在移动设备上打开虚拟键盘），默认值为 False
    """

    minute_step: int = 0
    """
    分钟选项间隔，默认值为 0
    """

    open: bool = False
    """
    控制浮层显隐，默认值为 False
    """

    placeholder: List[str] = ["开始时间", "结束时间"]
    """
    输入框占位文本，默认值为 ["开始时间", "结束时间"]
    """

    placement: Optional[str] = None
    """
    浮层预设位置，bottomLeft bottomRight topLeft topRight，默认值为 None
    """

    popup_class_name: Optional[str] = None
    """
    额外的弹出日历 className，默认值为 None
    """

    popup_style: Optional[Any] = None
    """
    额外的弹出日历样式，默认值为 None
    """

    second_step: int = 0
    """
    秒选项间隔，默认值为 0
    """

    show_now: bool = False
    """
    面板是否显示“此刻”按钮，默认值为 False
    """

    size: Optional[str] = None
    """
    输入框大小，large | middle | small，默认值为 None
    """

    status: Optional[str] = None
    """
    设置校验状态，'error' | 'warning'，默认值为 None
    """

    suffix_icon: Optional[Any] = None
    """
    自定义的选择框后缀图标，默认值为 None
    """

    use_12_hours: bool = False
    """
    使用 12 小时制，为 True 时 format 默认为 h:mm:ss a，默认值为 False
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式，默认值为 None
    """

    value: Optional[Any] = None
    """
    指定选中项
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
        设置自动获取焦点。

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
            class_name (str): 自定义类名。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.class_name = class_name
        return self

    def set_clear_icon(self, clear_icon: Any):
        """
        设置自定义的清除图标。

        Args:
            clear_icon (Any): 清除图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.clear_icon = clear_icon
        return self

    def set_clear_text(self, clear_text: str):
        """
        设置清除按钮的提示文案。

        Args:
            clear_text (str): 提示文案。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.clear_text = clear_text
        return self

    def set_disabled_time(self, disabled_time: Any):
        """
        设置不可选择的时间。

        Args:
            disabled_time (Any): 不可选择的时间。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.disabled_time = disabled_time
        return self

    def set_hide_disabled_options(self, hide_disabled_options: bool):
        """
        设置隐藏禁止选择的选项。

        Args:
            hide_disabled_options (bool): 是否隐藏禁止选择的选项。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.hide_disabled_options = hide_disabled_options
        return self

    def set_hour_step(self, hour_step: int):
        """
        设置小时选项间隔。

        Args:
            hour_step (int): 小时选项间隔。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.hour_step = hour_step
        return self

    def set_minute_step(self, minute_step: int):
        """
        设置分钟选项间隔。

        Args:
            minute_step (int): 分钟选项间隔。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.minute_step = minute_step
        return self

    def set_second_step(self, second_step: int):
        """
        设置秒选项间隔。

        Args:
            second_step (int): 秒选项间隔。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.second_step = second_step
        return self

    def set_use_12_hours(self, use_12_hours: bool):
        """
        设置使用 12 小时制。

        Args:
            use_12_hours (bool): 是否使用 12 小时制。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.use_12_hours = use_12_hours
        if use_12_hours and self.format == "HH:mm":
            self.format = "h:mm:ss a"
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_format(self, format_str: str):
        """
        设置日期格式。

        Args:
            format_str (str): 日期格式字符串。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.format = format_str
        return self

    def set_popup_class_name(self, popup_class_name: str):
        """
        设置额外的弹出日历 className。

        Args:
            popup_class_name (str): className 字符串。

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

    def set_open(self, open: bool):
        """
        控制浮层显隐。

        Args:
            open (bool): 是否显示浮层。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.open = open
        return self

    def set_placeholder(self, placeholder: List[str]):
        """
        设置输入框占位文本。

        Args:
            placeholder (List[str]): 占位文本。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str):
        """
        设置浮层预设位置。

        Args:
            placement (str): 预设位置，如 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placement = placement
        return self

    def set_popup_style(self, popup_style: Any):
        """
        设置额外的弹出日历样式。

        Args:
            popup_style (Any): 弹出日历样式。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.popup_style = popup_style
        return self

    def set_size(self, size: str):
        """
        设置控件大小。

        Args:
            size (str): 控件大小，如 'large', 'middle', 'small'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_status(self, status: str):
        """
        设置校验状态。

        Args:
            status (str): 校验状态，如 'error', 'warning'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any):
        """
        设置自定义的选择框后缀图标。

        Args:
            suffix_icon (Any): 后缀图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.suffix_icon = suffix_icon
        return self

    def set_show_now(self, show_now: bool):
        """
        设置面板是否显示“此刻”按钮。

        Args:
            show_now (bool): 是否显示“此刻”按钮。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_now = show_now
        return self
