from typing import Any, Dict
from .base import Base


class Date(Base):

    component: str = "dateField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    是否支持清除
    """

    auto_focus: bool = False
    """
    自动获取焦点
    """

    bordered: bool = True
    """
    是否有边框
    """

    class_name: str = True
    """
    自定义类名
    """

    default_value: Any = None
    """
    默认的选中项
    """

    disabled: Any = None
    """
    禁用状态
    """

    format: str = "YYYY-MM-DD"
    """
    设置日期格式
    """

    popup_class_name: str = None
    """
    额外的弹出日历 className
    """

    input_read_only: bool = False
    """
    设置输入框为只读
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

    picker: str = None
    """
    设置选择器类型
    """

    placeholder: str = "请选择"
    """
    输入框占位文本
    """

    placement: str = None
    """
    浮层预设位置
    """

    popup_style: Any = None
    """
    额外的弹出日历样式
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
    设置校验状态
    """

    style: Dict[str, Any] = None
    """
    自定义样式
    """

    suffix_icon: Any = None
    """
    自定义的选择框后缀图标
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
    当设定了 showTime 的时候，面板是否显示“此刻”按钮
    """

    show_time: Any = None
    """
    增加时间选择功能
    """

    show_today: bool = None
    """
    是否展示“今天”按钮
    """

    def set_allow_clear(self, allow_clear: bool):
        """
        设置是否支持清除功能。
        :param allow_clear: 是否支持清除的布尔值
        :return: 当前 Component 实例
        """
        self.allow_clear = allow_clear
        return self

    def set_auto_focus(self, auto_focus: bool):
        """
        设置是否自动获取焦点。
        :param auto_focus: 是否自动获取焦点的布尔值
        :return: 当前 Component 实例
        """
        self.auto_focus = auto_focus
        return self

    def set_bordered(self, bordered: bool):
        """
        设置是否有边框。
        :param bordered: 是否有边框的布尔值
        :return: 当前 Component 实例
        """
        self.bordered = bordered
        return self

    def set_class_name(self, class_name: str):
        """
        设置组件的自定义类名。
        :param class_name: 类名字符串
        :return: 当前 Component 实例
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
        :param format: 日期格式字符串
        :return: 当前 Component 实例
        """
        self.format = format
        return self

    def set_popup_class_name(self, popup_class_name: str):
        """
        设置额外的弹出日历 className。
        :param popup_class_name: 类名字符串
        :return: 当前 Component 实例
        """
        self.popup_class_name = popup_class_name
        return self

    def set_input_read_only(self, input_read_only: bool):
        """
        设置输入框是否为只读。
        :param input_read_only: 是否只读的布尔值
        :return: 当前 Component 实例
        """
        self.input_read_only = input_read_only
        return self

    def set_locale(self, locale: Any):
        """
        设置国际化配置。
        :param locale: 国际化配置数据，可以是字典或其他合适的数据结构
        :return: 当前 Component 实例
        """
        self.locale = locale
        return self

    def set_mode(self, mode: str):
        """
        设置日期面板的状态。
        :param mode: 状态字符串，如 'time'、'date' 等
        :return: 当前 Component 实例
        """
        self.mode = mode
        return self

    def set_next_icon(self, next_icon: Any):
        """
        设置自定义下一个图标。
        :param next_icon: 图标数据，可以是字符串、图片路径等
        :return: 当前 Component 实例
        """
        self.next_icon = next_icon
        return self

    def set_open(self, open: bool):
        """
        控制浮层的显隐。
        :param open: 是否显示浮层的布尔值
        :return: 当前 Component 实例
        """
        self.open = open
        return self

    def set_picker(self, picker: str):
        """
        设置选择器类型。
        :param picker: 选择器类型字符串，如 'date'、'week' 等
        :return: 当前 Component 实例
        """
        self.picker = picker
        return self

    def set_placeholder(self, placeholder: str):
        """
        设置输入框的占位文本。
        :param placeholder: 占位文本字符串
        :return: 当前 Component 实例
        """
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str):
        """
        设置浮层的预设位置。
        :param placement: 位置字符串，如 'bottomLeft'、'topRight' 等
        :return: 当前 Component 实例
        """
        self.placement = placement
        return self

    def set_popup_style(self, popup_style: Any):
        """
        设置额外的弹出日历样式。
        :param popup_style: 样式数据，可以是字典或其他合适的数据结构
        :return: 当前 Component 实例
        """
        self.popup_style = popup_style
        return self

    def set_prev_icon(self, prev_icon: Any):
        """
        设置自定义上一个图标。
        :param prev_icon: 图标数据，可以是字符串、图片路径等
        :return: 当前 Component 实例
        """
        self.prev_icon = prev_icon
        return self

    def set_size(self, size: str):
        """
        设置输入框的大小。
        :param size: 大小字符串，如 'large'、'middle'、'small'
        :return: 当前 Component 实例
        """
        self.size = size
        return self

    def set_status(self, status: str):
        """
        设置校验状态。
        :param status: 状态字符串，如 'error'、'warning'
        :return: 当前 Component 实例
        """
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any):
        """
        设置自定义的选择框后缀图标。
        :param suffix_icon: 图标数据，可以是字符串、图片路径等
        :return: 当前 Component 实例
        """
        self.suffix_icon = suffix_icon
        return self

    def set_super_next_icon(self, super_next_icon: Any):
        """
        设置自定义 << 切换图标。
        :param super_next_icon: 图标数据，可以是字符串、图片路径等
        :return: 当前 Component 实例
        """
        self.super_next_icon = super_next_icon
        return self

    def set_super_prev_icon(self, super_prev_icon: Any):
        """
        设置自定义 >> 切换图标。
        :param super_prev_icon: 图标数据，可以是字符串、图片路径等
        :return: 当前 Component 实例
        """
        self.super_prev_icon = super_prev_icon
        return self

    def set_default_picker_value(self, default_picker_value: str):
        """
        设置默认面板日期。
        :param default_picker_value: 日期字符串
        :return: 当前 Component 实例
        """
        self.default_picker_value = default_picker_value
        return self

    def set_show_now(self, show_now: bool):
        """
        当设定了 showTime 的时候，设置面板是否显示“此刻”按钮。
        :param show_now: 是否显示“此刻”按钮的布尔值
        :return: 当前 Component 实例
        """
        self.show_now = show_now
        return self

    def set_show_time(self, show_time: Any):
        """
        增加时间选择功能。
        :param show_time: 时间选择功能相关配置数据，可以是字典或其他合适的数据结构
        :return: 当前 Component 实例
        """
        self.show_time = show_time
        return self

    def set_show_today(self, show_today: bool):
        """
        设置是否展示“今天”按钮。
        :param show_today: 是否展示“今天”按钮的布尔值
        :return: 当前 Component 实例
        """
        self.show_today = show_today
        return self
