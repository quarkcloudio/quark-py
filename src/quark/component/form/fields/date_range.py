from typing import Any, Dict, List
from .base import Base


class DateRange(Base):

    component: str = "dateRangeField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    是否支持清除操作
    """

    auto_focus: bool = False
    """
    是否自动获取焦点
    """

    bordered: bool = True
    """
    是否显示边框
    """

    class_name: str = None
    """
    自定义类名
    """

    default_value: Any = [None, None]
    """
    默认选中项
    """

    disabled: Any = None
    """
    是否禁用
    """

    format: str = "YYYY-MM-DD"
    """
    日期格式
    """

    popup_class_name: str = None
    """
    弹出日历的额外类名
    """

    input_read_only: bool = False
    """
    输入框是否只读
    """

    locale: Any = None
    """
    国际化配置
    """

    mode: str = None
    """
    日期面板的状态
    """

    next_icon: Any = None
    """
    自定义下一个图标
    """

    open: bool = None
    """
    控制浮层显隐
    """

    picker: str = "date"
    """
    选择器类型
    """

    placeholder: List[str] = ["开始日期", "结束日期"]
    """
    输入框占位文本
    """

    placement: str = None
    """
    浮层预设位置
    """

    popup_style: Any = None
    """
    弹出日历的额外样式
    """

    prev_icon: Any = None
    """
    自定义上一个图标
    """

    size: str = None
    """
    输入框大小
    """

    status: str = None
    """
    校验状态
    """

    style: Dict[str, Any] = None
    """
    自定义样式
    """

    suffix_icon: Any = None
    """
    自定义选择框后缀图标
    """

    super_next_icon: Any = None
    """
    自定义 << 切换图标
    """

    super_prev_icon: Any = None
    """
    自定义 >> 切换图标
    """

    value: Any = None
    """
    指定选中项
    """

    default_picker_value: str = None
    """
    默认面板日期
    """

    show_now: bool = None
    """
    设定 showTime 时，是否显示“此刻”按钮
    """

    show_time: Any = None
    """
    是否增加时间选择功能
    """

    show_today: bool = None
    """
    是否展示“今天”按钮
    """

    def set_allow_clear(self, allow_clear: bool):
        self.allow_clear = allow_clear
        return self  # 设置是否支持清除并返回自身

    def set_auto_focus(self, auto_focus: bool):
        self.auto_focus = auto_focus
        return self  # 设置是否自动聚焦并返回自身

    def set_bordered(self, bordered: bool):
        self.bordered = bordered
        return self  # 设置是否显示边框并返回自身

    def set_class_name(self, class_name: str):
        self.class_name = class_name
        return self  # 设置自定义类名并返回自身

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_format(self, format: str):
        self.format = format
        return self  # 设置日期格式并返回自身

    def set_popup_class_name(self, popup_class_name: str):
        self.popup_class_name = popup_class_name
        return self  # 设置弹出日历类名并返回自身

    def set_input_read_only(self, input_read_only: bool):
        self.input_read_only = input_read_only
        return self  # 设置输入框只读并返回自身

    def set_locale(self, locale: Any):
        self.locale = locale
        return self  # 设置国际化配置并返回自身

    def set_mode(self, mode: str):
        self.mode = mode
        return self  # 设置日期面板模式并返回自身

    def set_next_icon(self, next_icon: Any):
        self.next_icon = next_icon
        return self  # 设置下一个图标并返回自身

    def set_open(self, open: bool):
        self.open = open
        return self  # 设置浮层显隐并返回自身

    def set_picker(self, picker: str):
        self.picker = picker
        return self  # 设置选择器类型并返回自身

    def set_placeholder(self, placeholder: List[str]):
        self.placeholder = placeholder
        return self  # 设置输入框占位文本并返回自身

    def set_placement(self, placement: str):
        self.placement = placement
        return self  # 设置浮层位置并返回自身

    def set_popup_style(self, popup_style: Any):
        self.popup_style = popup_style
        return self  # 设置弹出日历样式并返回自身

    def set_prev_icon(self, prev_icon: Any):
        self.prev_icon = prev_icon
        return self  # 设置上一个图标并返回自身

    def set_size(self, size: str):
        self.size = size
        return self  # 设置输入框大小并返回自身

    def set_status(self, status: str):
        self.status = status
        return self  # 设置校验状态并返回自身

    def set_suffix_icon(self, suffix_icon: Any):
        self.suffix_icon = suffix_icon
        return self  # 设置后缀图标并返回自身

    def set_super_next_icon(self, super_next_icon: Any):
        self.super_next_icon = super_next_icon
        return self  # 设置 << 切换图标并返回自身

    def set_super_prev_icon(self, super_prev_icon: Any):
        self.super_prev_icon = super_prev_icon
        return self  # 设置 >> 切换图标并返回自身

    def set_default_picker_value(self, default_picker_value: str):
        self.default_picker_value = default_picker_value
        return self  # 设置默认面板日期并返回自身

    def set_show_now(self, show_now: bool):
        self.show_now = show_now
        return self  # 设置是否显示“此刻”按钮并返回自身

    def set_show_time(self, show_time: Any):
        self.show_time = show_time
        return self  # 设置是否增加时间选择功能并返回自身

    def set_show_today(self, show_today: bool):
        self.show_today = show_today
        return self  # 设置是否展示“今天”按钮并返回自身
