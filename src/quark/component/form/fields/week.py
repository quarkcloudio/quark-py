from typing import Any, Dict, List, Optional, Callable
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

    mode: str = ""  # 日期面板的状态 time | date | month | year | decade
    """
    组件名称
    """

    next_icon: Optional[Any] = None  # 自定义下一个图标
    """
    组件名称
    """

    open: bool = False  # 控制浮层显隐
    """
    组件名称
    """

    picker: str = ""  # 设置选择器类型 date | week | month | quarter | year
    """
    组件名称
    """

    placeholder: str = "请选择"  # 输入框占位文本
    """
    组件名称
    """

    placement: str = ""  # 浮层预设位置，bottomLeft bottomRight topLeft topRight
    """
    组件名称
    """

    popup_style: Optional[Any] = None  # 额外的弹出日历样式
    """
    组件名称
    """

    prev_icon: Optional[Any] = None  # 自定义上一个图标
    """
    组件名称
    """

    size: str = ""  # 输入框大小，large | middle | small
    """
    组件名称
    """

    status: str = ""  # 设置校验状态，'error' | 'warning'
    """
    组件名称
    """

    style: Optional[Dict[str, Any]] = None  # 自定义样式
    """
    组件名称
    """

    suffix_icon: Optional[Any] = None  # 自定义的选择框后缀图标
    """
    组件名称
    """

    super_next_icon: Optional[Any] = None  # 自定义 << 切换图标
    """
    组件名称
    """

    super_prev_icon: Optional[Any] = None  # 自定义 >> 切换图标
    """
    组件名称
    """

    value: Optional[Any] = None  # 指定选中项,string[] | number[]
    """
    组件名称
    """

    default_picker_value: str = ""  # 默认面板日期
    """
    组件名称
    """

    show_now: bool = False  # 当设定了 showTime 的时候，面板是否显示“此刻”按钮
    """
    组件名称
    """

    show_time: Optional[Any] = None  # 增加时间选择功能
    """
    组件名称
    """

    show_today: bool = False  # 是否展示“今天”按钮
    """
    组件名称
    """

    class Config:
        allow_population_by_field_name = True

    # 初始化组件
    @classmethod
    def new(cls):
        return cls().init()

    # 初始化
    def init(self):
        self.component = "weekField"
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.column = TableColumn().init()
        self.placeholder = "请选择"
        self.set_key("DEFAULT_KEY", False)
        return self

    # 设置Key
    def set_key(self, key: str, crypt: bool):
        # 模拟 hex.Make 函数，这里简单返回 key
        self.component_key = key
        return self

    # Set style.
    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    # 会在 label 旁增加一个 icon，悬浮后展示配置的信息
    def set_tooltip(self, tooltip: str):
        self.tooltip = tooltip
        return self

    # Field 的长度，我们归纳了常用的 Field 长度以及适合的场景，支持了一些枚举 "xs" , "s" , "m" , "l" , "x"
    def set_width(self, width: Any):
        style = self.style.copy() if self.style else {}
        style["width"] = width
        self.style = style
        return self

    # 开启 grid 模式时传递给 Row, 仅在ProFormGroup, ProFormList, ProFormFieldSet 中有效，默认：{ gutter: 8 }
    def set_row_props(self, row_props: Dict[str, Any]):
        self.row_props = row_props
        return self

    # 开启 grid 模式时传递给 Col，默认：{ xs: 24 }
    def set_col_props(self, col_props: Dict[str, Any]):
        self.col_props = col_props
        return self

    # 是否是次要控件，只针对 LightFilter 下有效
    def set_secondary(self, secondary: bool):
        self.secondary = secondary
        return self

    # 配合 label 属性使用，表示是否显示 label 后面的冒号
    def set_colon(self, colon: bool):
        self.colon = colon
        return self

    # 额外的提示信息，和 help 类似，当需要错误信息和提示文案同时出现时，可以使用这个。
    def set_extra(self, extra: str):
        self.extra = extra
        return self

    # 配合 validateStatus 属性使用，展示校验状态图标，建议只配合 Input 组件使用
    def set_has_feedback(self, has_feedback: bool):
        self.has_feedback = has_feedback
        return self

    # 配合 help 属性使用，展示校验状态图标，建议只配合 Input 组件使用
    def set_help(self, help: str):
        self.help = help
        return self

    # 为 true 时不带样式，作为纯字段控件使用
    def set_no_style(self):
        self.no_style = True
        return self

    # label 标签的文本
    def set_label(self, label: str):
        self.label = label
        return self

    # 标签文本对齐方式
    def set_label_align(self, align: str):
        self.label_align = align
        return self

    # label 标签布局，同 <Col> 组件，设置 span offset 值，如 {span: 3, offset: 12} 或 sm: {span: 3, offset: 12}。
    # 你可以通过 Form 的 labelCol 进行统一设置。当和 Form 同时设置时，以 Item 为准
    def set_label_col(self, col: Any):
        self.label_col = col
        return self

    # 字段名，支持数组
    def set_name(self, name: str):
        self.name = name
        return self

    # 字段名转标签，只支持英文
    def set_name_as_label(self):
        # 使用 str.title() 替代 strings.Title
        self.label = self.name.title()
        return self

    # 是否必填，如不设置，则会根据校验规则自动生成
    def set_required(self):
        self.required = True
        return self

    # 生成前端验证规则
    def build_frontend_rules(self, path: str):
        uri = path.split("/")
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        rules = [Rule(**rule.dict()) for rule in self.rules]
        creation_rules = [Rule(**rule.dict()) for rule in self.creation_rules] if is_creating else []
        update_rules = [Rule(**rule.dict()) for rule in self.update_rules] if is_editing else []

        frontend_rules = []
        frontend_rules.extend(rules)
        frontend_rules.extend(creation_rules)
        frontend_rules.extend(update_rules)

        self.frontend_rules = frontend_rules
        return self

    # 校验规则，设置字段的校验逻辑
    def set_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    # 校验规则，只在创建表单提交时生效
    def set_creation_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    # 校验规则，只在更新表单提交时生效
    def set_update_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self

    # 获取全局验证规则
    def get_rules(self):
        return self.rules

    # 获取创建表单验证规则
    def get_creation_rules(self):
        return self.creation_rules

    # 获取更新表单验证规则
    def get_update_rules(self):
        return self.update_rules

    # 子节点的值的属性，如 Switch 的是 "checked"
    def set_value_prop_name(self, value_prop_name: str):
        self.value_prop_name = value_prop_name
        return self

    # 需要为输入控件设置布局样式时，使用该属性，用法同 labelCol。
    # 你可以通过 Form 的 wrapperCol 进行统一设置。当和 Form 同时设置时，以 Item 为准。
    def set_wrapper_col(self, col: Any):
        self.wrapper_col = col
        return self

    # 列表页、详情页中列属性
    def set_column(self, f: Callable[[TableColumn], TableColumn]):
        self.column = f(self.column)
        return self

    # 设置列的对齐方式,left | right | center，只在列表页、详情页中有效
    def set_align(self, align: str):
        self.align = align
        return self

    # （IE 下无效）列是否固定，可选 true (等效于 left) left rightr，只在列表页中有效
    def set_fixed(self, fixed: Any):
        self.fixed = fixed
        return self

    # 表格列是否可编辑，只在列表页中有效
    def set_editable(self, editable: bool):
        self.editable = editable
        return self

    # 是否自动缩略，只在列表页、详情页中有效
    def set_ellipsis(self, ellipsis: bool):
        self.ellipsis = ellipsis
        return self

    # 是否支持复制，只在列表页、详情页中有效
    def set_copyable(self, copyable: bool):
        self.copyable = copyable
        return self

    # 表头的筛选菜单项，当值为 true 时，自动使用 valueEnum 生成，只在列表页中有效
    def set_filters(self, filters: Any):
        if isinstance(filters, dict):
            tmp_filters = []
            for k, v in filters.items():
                tmp_filters.append({"text": v, "value": k})
            self.filters = tmp_filters
        else:
            self.filters = filters
        return self

    # 查询表单中的权重，权重大排序靠前，只在列表页中有效
    def set_order(self, order: int):
        self.order = order
        return self

    # 可排序列，只在列表页中有效
    def set_sorter(self, sorter: bool):
        self.sorter = sorter
        return self

    # 包含列的数量，只在详情页中有效
    def set_span(self, span: int):
        self.span = span
        return self

    # 设置列宽，只在列表页中有效
    def set_column_width(self, width: int):
        self.column_width = width
        return self

    # 设置保存值。
    def set_value(self, value: Any):
        self.value = value
        return self

    # 设置默认值。
    def set_default(self, value: Any):
        self.default_value = value
        return self

    # 是否禁用状态，默认为 false
    def set_disabled(self, disabled: bool):
        self.disabled = disabled
        return self

    # 是否忽略保存到数据库，默认为 false
    def set_ignore(self, ignore: bool):
        self.ignore = ignore
        return self

    # 设置When组件数据
    def set_when(self, *value):
        w = WhenComponent()
        i = WhenItem()
        operator = "="
        option = None

        if len(value) == 2:
            option = value[0]
            callback = value[1]
            i.body = callback()
        elif len(value) == 3:
            operator = value[0]
            option = value[1]
            callback = value[2]
            i.body = callback()

        get_option = str(option)
        if operator == "!=":
            i.condition = f"<%=String({self.name}) !== '{get_option}' %>"
        elif operator == "=":
            i.condition = f"<%=String({self.name}) === '{get_option}' %>"
        elif operator == ">":
            i.condition = f"<%=String({self.name}) > '{get_option}' %>"
        elif operator == "<":
            i.condition = f"<%=String({self.name}) < '{get_option}' %>"
        elif operator == "<=":
            i.condition = f"<%=String({self.name}) <= '{get_option}' %>"
        elif operator == ">=":
            i.condition = f"<%=String({self.name}) >= '{get_option}' %>"
        elif operator == "has":
            i.condition = f"<%=(String({self.name}).indexOf('{get_option}') !=-1) %>"
        elif operator == "in":
            import json
            json_str = json.dumps(option)
            i.condition = f"<%=({json_str}.indexOf({self.name}) !=-1) %>"
        else:
            i.condition = f"<%=String({self.name}) === '{get_option}' %>"

        i.condition_name = self.name
        i.condition_operator = operator
        i.option = option
        self.when_item.append(i)
        self.when = w.set_items(self.when_item)
        return self

    # 获取When组件数据
    def get_when(self):
        return self.when

    # Specify that the element should be hidden from the index view.
    def hide_from_index(self, callback: bool):
        self.show_on_index = not callback
        return self

    # Specify that the element should be hidden from the detail view.
    def hide_from_detail(self, callback: bool):
        self.show_on_detail = not callback
        return self

    # Specify that the element should be hidden from the creation view.
    def hide_when_creating(self, callback: bool):
        self.show_on_creation = not callback
        return self

    # Specify that the element should be hidden from the update view.
    def hide_when_updating(self, callback: bool):
        self.show_on_update = not callback
        return self

    # Specify that the element should be hidden from the export file.
    def hide_when_exporting(self, callback: bool):
        self.show_on_export = not callback
        return self

    # Specify that the element should be hidden from the import file.
    def hide_when_importing(self, callback: bool):
        self.show_on_import = not callback
        return self

    # Specify that the element should be hidden from the index view.
    def on_index_showing(self, callback: bool):
        self.show_on_index = callback
        return self

    # Specify that the element should be hidden from the detail view.
    def on_detail_showing(self, callback: bool):
        self.show_on_detail = callback
        return self

    # Specify that the element should be hidden from the creation view.
    def show_on_creating(self, callback: bool):
        self.show_on_creation = callback
        return self

    # Specify that the element should be hidden from the update view.
    def show_on_updating(self, callback: bool):
        self.show_on_update = callback
        return self

    # Specify that the element should be hidden from the export file.
    def show_on_exporting(self, callback: bool):
        self.show_on_export = callback
        return self

    # Specify that the element should be hidden from the import file.
    def show_on_importing(self, callback: bool):
        self.show_on_import = callback
        return self

    # Specify that the element should only be shown on the index view.
    def only_on_index(self):
        self.show_on_index = true
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    # Specify that the element should only be shown on the detail view.
    def only_on_detail(self):
        self.show_on_index = False
        self.show_on_detail = true
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    # Specify that the element should only be shown on forms.
    def only_on_forms(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = true
        self.show_on_update = true
        self.show_on_export = False
        self.show_on_import = False
        return self

    # Specify that the element should only be shown on the creation view.
    def only_on_creating(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = true
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    # Specify that the element should only be shown on the update view.
    def only_on_updating(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = true
        self.show_on_export = False
        self.show_on_import = False
        return self

    # Specify that the element should only be shown on export file.
    def only_on_export(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = true
        self.show_on_import = False
        return self

    # Specify that the element should only be shown on import file.
    def only_on_import(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = true
        return self

    # Specify that the element should be hidden from forms.
    def except_on_forms(self):
        self.show_on_index = true
        self.show_on_detail = true
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = true
        self.show_on_import = true
        return self

    # Check for showing when updating.
    def is_shown_on_update(self):
        return self.show_on_update

    # Check showing on index.
    def is_shown_on_index(self):
        return self.show_on_index

    # Check showing on detail.
    def is_shown_on_detail(self):
        return self.show_on_detail

    # Check for showing when creating.
    def is_shown_on_creation(self):
        return self.show_on_creation

    # Check for showing when exporting.
    def is_shown_on_export(self):
        return self.show_on_export

    # Check for showing when importing.
    def is_shown_on_import(self):
        return self.show_on_import

    # 当前列值的枚举 valueEnum
    def get_value_enum(self):
        data = {}
        return data

    # 设置回调函数
    def set_callback(self, closure: Optional[Callable[[Dict[str, Any]], Any]]):
        if closure is not None:
            self.callback = closure
        return self

    # 获取回调函数
    def get_callback(self):
        return self.callback

    # 获取数据接口
    def set_api(self, api: str):
        self.api = api
        return self

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