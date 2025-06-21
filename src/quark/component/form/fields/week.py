from typing import Any, Dict, Optional
from .base import Base


class Week(Base):

    component: str = "weekField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    是否支持清除，默认true
    """

    auto_focus: bool = False
    """
    自动获取焦点，默认false
    """

    bordered: bool = True
    """
    是否有边框，默认true
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
    输入框占位文本
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
    指定选中项,string[] | number[]
    """

    default_picker_value: str = ""
    """
    默认面板日期
    """

    show_now: bool = False
    """
    当设定了 showTime 的时候，面板是否显示“此刻”按钮
    """

    show_time: Optional[Any] = None
    """
    增加时间选择功能
    """

    show_today: bool = False
    """
    是否展示“今天”按钮
    """

    # 可以点击清除图标删除内容
    def set_allow_clear(self, allow_clear: bool):
        self.allow_clear = allow_clear
        return self

    # 自动获取焦点，默认false
    def set_auto_focus(self, auto_focus: bool):
        self.auto_focus = auto_focus
        return self

    # 是否有边框，默认true
    def set_bordered(self, bordered: bool):
        self.bordered = bordered
        return self

    # 自定义类名
    def set_class_name(self, class_name: str):
        self.class_name = class_name
        return self

    # 默认的选中项
    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    # 设置日期格式，为数组时支持多格式匹配，展示以第一个为准。
    def set_format(self, format: str):
        self.format = format
        return self

    # 自定义类名
    def set_popup_class_name(self, popup_class_name: str):
        self.popup_class_name = popup_class_name
        return self

    # 设置输入框为只读（避免在移动设备上打开虚拟键盘）
    def set_input_read_only(self, input_read_only: bool):
        self.input_read_only = input_read_only
        return self

    # 国际化配置
    def set_locale(self, locale: Any):
        self.locale = locale
        return self

    # 日期面板的状态 time | date | month | year | decade
    def set_mode(self, mode: str):
        self.mode = mode
        return self

    # 自定义下一个图标
    def set_next_icon(self, next_icon: Any):
        self.next_icon = next_icon
        return self

    # 控制浮层显隐
    def set_open(self, open: bool):
        self.open = open
        return self

    # 设置选择器类型 date | week | month | quarter | year
    def set_picker(self, picker: str):
        self.picker = picker
        return self

    # 输入框占位文本
    def set_placeholder(self, placeholder: str):
        self.placeholder = placeholder
        return self

    # 浮层预设位置，bottomLeft bottomRight topLeft topRight
    def set_placement(self, placement: str):
        self.placement = placement
        return self

    # 额外的弹出日历样式
    def set_popup_style(self, popup_style: Any):
        self.popup_style = popup_style
        return self

    # 自定义上一个图标
    def set_prev_icon(self, prev_icon: Any):
        self.prev_icon = prev_icon
        return self

    # 控件大小。注：标准表单内的输入框大小限制为 large。可选 large default small
    def set_size(self, size: str):
        self.size = size
        return self

    # 设置校验状态，'error' | 'warning'
    def set_status(self, status: str):
        self.status = status
        return self

    # 自定义的选择框后缀图标
    def set_suffix_icon(self, suffix_icon: Any):
        self.suffix_icon = suffix_icon
        return self

    # 自定义 << 切换图标
    def set_super_next_icon(self, super_next_icon: Any):
        self.super_next_icon = super_next_icon
        return self

    # 自定义 >> 切换图标
    def set_super_prev_icon(self, super_prev_icon: Any):
        self.super_prev_icon = super_prev_icon
        return self

    # 默认面板日期
    def set_default_picker_value(self, default_picker_value: str):
        self.default_picker_value = default_picker_value
        return self

    # 当设定了 showTime 的时候，面板是否显示“此刻”按钮
    def set_show_now(self, show_now: bool):
        self.show_now = show_now
        return self

    # 增加时间选择功能
    def set_show_time(self, show_time: Any):
        self.show_time = show_time
        return self

    # 是否展示“今天”按钮
    def set_show_today(self, show_today: bool):
        self.show_today = show_today
        return self
