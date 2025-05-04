import json
from typing import Dict, List, Any, Callable, Optional
from pydantic import BaseModel

# 模拟 rule 模块
class Rule(BaseModel):
    name: str = ""  # 校验规则所属的字段名

# 模拟 table 模块
class TableColumn(BaseModel):
    def init(self):
        return self  # 初始化表格列实例并返回

# 模拟 when 模块
class WhenItem(BaseModel):
    body: Any = None  # 当条件满足时要执行的内容
    condition: str = ""  # 条件表达式
    condition_name: str = ""  # 条件所依赖的字段名
    condition_operator: str = ""  # 条件判断的操作符
    option: Any = None  # 条件判断的选项值

class WhenComponent(BaseModel):
    items: List[WhenItem] = []  # 存储多个 WhenItem 实例的列表

    def set_items(self, items: List[WhenItem]):
        self.items = items
        return self  # 设置 When 组件的条件项列表并返回自身

def new_when():
    return WhenComponent()  # 创建一个新的 WhenComponent 实例

def new_when_item():
    return WhenItem()  # 创建一个新的 WhenItem 实例

class Component(BaseModel):
    # 组件基本信息
    component_key: str = ""  # 组件唯一标识
    component: str = ""  # 组件名称

    # 表单布局相关属性
    row_props: Optional[Dict[str, Any]] = None  # 开启 grid 模式时传递给 Row 的属性
    col_props: Optional[Dict[str, Any]] = None  # 开启 grid 模式时传递给 Col 的属性
    secondary: bool = False  # 是否为次要控件，仅在 LightFilter 下有效
    colon: bool = True  # 是否显示 label 后面的冒号
    extra: str = ""  # 额外的提示信息
    has_feedback: bool = False  # 是否展示校验状态图标
    help: str = ""  # 提示信息
    hidden: bool = False  # 是否隐藏字段，但仍参与收集和校验
    initial_value: Optional[Any] = None  # 子元素默认值
    label: str = ""  # label 标签文本
    label_align: str = "right"  # 标签文本对齐方式
    label_col: Optional[Any] = None  # label 标签布局设置
    name: str = ""  # 字段名，支持数组形式
    no_style: bool = False  # 是否不带样式，作为纯字段控件使用
    required: bool = False  # 是否为必填字段
    tooltip: str = ""  # label 旁的提示信息
    value_prop_name: str = ""  # 子节点值的属性名
    wrapper_col: Optional[Any] = None  # 输入控件的布局设置

    # 表格列相关属性
    column: TableColumn = TableColumn().init()  # 列表页、详情页中列属性
    align: str = ""  # 列的对齐方式
    fixed: Optional[Any] = None  # 列是否固定
    editable: bool = False  # 表格列是否可编辑
    ellipsis: bool = False  # 是否自动缩略
    copyable: bool = False  # 是否支持复制
    filters: Optional[Any] = None  # 表头筛选菜单项
    order: int = 0  # 查询表单中的权重
    sorter: Optional[Any] = None  # 可排序列设置
    span: int = 0  # 详情页中包含列的数量
    column_width: int = 0  # 列表页中列的宽度

    # 通用属性
    api: str = ""  # 获取数据的接口地址
    ignore: bool = False  # 是否忽略保存到数据库
    rules: List[Rule] = []  # 全局校验规则
    creation_rules: List[Rule] = []  # 创建页校验规则
    update_rules: List[Rule] = []  # 编辑页校验规则
    frontend_rules: List[Rule] = []  # 前端校验规则
    when: Optional[WhenComponent] = None  # When 组件实例
    when_item: List[WhenItem] = []  # When 组件的条件项列表
    show_on_index: bool = True  # 是否在列表页展示
    show_on_detail: bool = True  # 是否在详情页展示
    show_on_creation: bool = True  # 是否在创建页展示
    show_on_update: bool = True  # 是否在编辑页展示
    show_on_export: bool = True  # 是否在导出 Excel 时展示
    show_on_import: bool = True  # 是否在导入 Excel 时展示
    callback: Optional[Callable[[Dict[str, Any]], Any]] = None  # 回调函数

    # 日期范围选择器特有属性
    allow_clear: bool = True  # 是否支持清除操作
    auto_focus: bool = False  # 是否自动获取焦点
    bordered: bool = True  # 是否显示边框
    class_name: str = ""  # 自定义类名
    default_value: Optional[Any] = [None, None]  # 默认选中项
    disabled: Optional[Any] = None  # 是否禁用
    format: str = "YYYY-MM-DD"  # 日期格式
    popup_class_name: str = ""  # 弹出日历的额外类名
    input_read_only: bool = False  # 输入框是否只读
    locale: Optional[Any] = None  # 国际化配置
    mode: str = ""  # 日期面板的状态
    next_icon: Optional[Any] = None  # 自定义下一个图标
    open: bool = False  # 控制浮层显隐
    picker: str = "date"  # 选择器类型
    placeholder: List[str] = ["开始日期", "结束日期"]  # 输入框占位文本
    placement: str = ""  # 浮层预设位置
    popup_style: Optional[Any] = None  # 弹出日历的额外样式
    prev_icon: Optional[Any] = None  # 自定义上一个图标
    size: str = ""  # 输入框大小
    status: str = ""  # 校验状态
    style: Dict[str, Any] = {}  # 自定义样式
    suffix_icon: Optional[Any] = None  # 自定义选择框后缀图标
    super_next_icon: Optional[Any] = None  # 自定义 << 切换图标
    super_prev_icon: Optional[Any] = None  # 自定义 >> 切换图标
    value: Optional[Any] = None  # 指定选中项
    default_picker_value: str = ""  # 默认面板日期
    show_now: bool = False  # 设定 showTime 时，是否显示“此刻”按钮
    show_time: Optional[Any] = None  # 是否增加时间选择功能
    show_today: bool = False  # 是否展示“今天”按钮

    @classmethod
    def new(cls):
        return cls().init()  # 创建一个新的组件实例并初始化

    def init(self):
        self.component = "dateRangeField"
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.column = TableColumn().init()
        self.picker = "date"
        self.format = "YYYY-MM-DD"
        self.placeholder = ["开始日期", "结束日期"]
        self.default_value = [None, None]
        # 需实现类似 SetKey 的功能
        # self.set_key(component.DEFAULT_KEY, component.DEFAULT_CRYPT)
        return self  # 初始化组件属性并返回自身

    def set_key(self, key: str, crypt: bool):
        # 需实现类似 hex.Make 的功能
        self.component_key = key
        return self  # 设置组件标识并返回自身

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self  # 设置组件样式并返回自身

    def set_tooltip(self, tooltip: str):
        self.tooltip = tooltip
        return self  # 设置 label 提示信息并返回自身

    def set_width(self, width: Any):
        style = self.style.copy()
        style["width"] = width
        self.style = style
        return self  # 设置组件宽度并返回自身

    def set_row_props(self, row_props: Dict[str, Any]):
        self.row_props = row_props
        return self  # 设置 Row 属性并返回自身

    def set_col_props(self, col_props: Dict[str, Any]):
        self.col_props = col_props
        return self  # 设置 Col 属性并返回自身

    def set_secondary(self, secondary: bool):
        self.secondary = secondary
        return self  # 设置是否为次要控件并返回自身

    def set_colon(self, colon: bool):
        self.colon = colon
        return self  # 设置是否显示冒号并返回自身

    def set_extra(self, extra: str):
        self.extra = extra
        return self  # 设置额外提示信息并返回自身

    def set_has_feedback(self, has_feedback: bool):
        self.has_feedback = has_feedback
        return self  # 设置是否展示校验图标并返回自身

    def set_help(self, help: str):
        self.help = help
        return self  # 设置提示信息并返回自身

    def set_no_style(self):
        self.no_style = True
        return self  # 设置为无样式纯字段控件并返回自身

    def set_label(self, label: str):
        self.label = label
        return self  # 设置 label 文本并返回自身

    def set_label_align(self, align: str):
        self.label_align = align
        return self  # 设置标签对齐方式并返回自身

    def set_label_col(self, col: Any):
        self.label_col = col
        return self  # 设置 label 布局并返回自身

    def set_name(self, name: str):
        self.name = name
        return self  # 设置字段名并返回自身

    def set_name_as_label(self):
        self.label = self.name.title()
        return self  # 将字段名转换为 label 文本并返回自身

    def set_required(self):
        self.required = True
        return self  # 设置字段为必填并返回自身

    def build_frontend_rules(self, path: str):
        frontend_rules = []
        rules = []
        creation_rules = []
        update_rules = []

        uri = path.split("/")
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        if self.rules:
            # 需实现 rule.ConvertToFrontendRules 功能
            rules = self.rules
        if is_creating and self.creation_rules:
            # 需实现 rule.ConvertToFrontendRules 功能
            creation_rules = self.creation_rules
        if is_editing and self.update_rules:
            # 需实现 rule.ConvertToFrontendRules 功能
            update_rules = self.update_rules

        frontend_rules.extend(rules)
        frontend_rules.extend(creation_rules)
        frontend_rules.extend(update_rules)

        self.frontend_rules = frontend_rules
        return self  # 根据路径生成前端校验规则并返回自身

    def set_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self  # 设置全局校验规则并返回自身

    def set_creation_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self  # 设置创建页校验规则并返回自身

    def set_update_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self  # 设置编辑页校验规则并返回自身

    def get_rules(self):
        return self.rules  # 获取全局校验规则

    def get_creation_rules(self):
        return self.creation_rules  # 获取创建页校验规则

    def get_update_rules(self):
        return self.update_rules  # 获取编辑页校验规则

    def set_value_prop_name(self, value_prop_name: str):
        self.value_prop_name = value_prop_name
        return self  # 设置子节点值属性名并返回自身

    def set_wrapper_col(self, col: Any):
        self.wrapper_col = col
        return self  # 设置输入控件布局并返回自身

    def set_column(self, f: Callable[[TableColumn], TableColumn]):
        self.column = f(self.column)
        return self  # 通过函数设置列属性并返回自身

    def set_align(self, align: str):
        self.align = align
        return self  # 设置列对齐方式并返回自身

    def set_fixed(self, fixed: Any):
        self.fixed = fixed
        return self  # 设置列固定状态并返回自身

    def set_editable(self, editable: bool):
        self.editable = editable
        return self  # 设置表格列是否可编辑并返回自身

    def set_ellipsis(self, ellipsis: bool):
        self.ellipsis = ellipsis
        return self  # 设置是否自动缩略并返回自身

    def set_copyable(self, copyable: bool):
        self.copyable = copyable
        return self  # 设置是否支持复制并返回自身

    def set_filters(self, filters: Any):
        if isinstance(filters, dict):
            tmp_filters = []
            for k, v in filters.items():
                tmp_filters.append({"text": v, "value": k})
            self.filters = tmp_filters
        else:
            self.filters = filters
        return self  # 设置表头筛选菜单项并返回自身

    def set_order(self, order: int):
        self.order = order
        return self  # 设置查询表单权重并返回自身

    def set_sorter(self, sorter: bool):
        self.sorter = sorter
        return self  # 设置是否可排序并返回自身

    def set_span(self, span: int):
        self.span = span
        return self  # 设置详情页列数量并返回自身

    def set_column_width(self, width: int):
        self.column_width = width
        return self  # 设置列表页列宽度并返回自身

    def set_value(self, value: Any):
        self.value = value
        return self  # 设置组件值并返回自身

    def set_default(self, value: Any):
        self.default_value = value
        return self  # 设置组件默认值并返回自身

    def set_disabled(self, disabled: bool):
        self.disabled = disabled
        return self  # 设置组件是否禁用并返回自身

    def set_ignore(self, ignore: bool):
        self.ignore = ignore
        return self  # 设置是否忽略保存到数据库并返回自身

    def set_when(self, *value):
        w = new_when()
        i = new_when_item()
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

        if option is not None:
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
                i.condition = f"<%=(String({self.name}).indexOf('{get_option}') != -1) %>"
            elif operator == "in":
                json_str = json.dumps(option)
                i.condition = f"<%=({json_str}.indexOf({self.name}) != -1) %>"
            else:
                i.condition = f"<%=String({self.name}) === '{get_option}' %>"

        i.condition_name = self.name
        i.condition_operator = operator
        i.option = option
        self.when_item.append(i)
        self.when = w.set_items(self.when_item)
        return self  # 设置 When 组件条件并返回自身

    def get_when(self):
        return self.when  # 获取 When 组件实例

    def hide_from_index(self, callback: bool):
        self.show_on_index = not callback
        return self  # 设置是否在列表页隐藏并返回自身

    def hide_from_detail(self, callback: bool):
        self.show_on_detail = not callback
        return self  # 设置是否在详情页隐藏并返回自身

    def hide_when_creating(self, callback: bool):
        self.show_on_creation = not callback
        return self  # 设置是否在创建页隐藏并返回自身

    def hide_when_updating(self, callback: bool):
        self.show_on_update = not callback
        return self  # 设置是否在编辑页隐藏并返回自身

    def hide_when_exporting(self, callback: bool):
        self.show_on_export = not callback
        return self  # 设置是否在导出时隐藏并返回自身

    def hide_when_importing(self, callback: bool):
        self.show_on_import = not callback
        return self  # 设置是否在导入时隐藏并返回自身

    def on_index_showing(self, callback: bool):
        self.show_on_index = callback
        return self  # 设置是否在列表页显示并返回自身

    def on_detail_showing(self, callback: bool):
        self.show_on_detail = callback
        return self  # 设置是否在详情页显示并返回自身

    def show_on_creating(self, callback: bool):
        self.show_on_creation = callback
        return self  # 设置是否在创建页显示并返回自身

    def show_on_updating(self, callback: bool):
        self.show_on_update = callback
        return self  # 设置是否在编辑页显示并返回自身

    def show_on_exporting(self, callback: bool):
        self.show_on_export = callback
        return self  # 设置是否在导出时显示并返回自身

    def show_on_importing(self, callback: bool):
        self.show_on_import = callback
        return self  # 设置是否在导入时显示并返回自身

    def only_on_index(self):
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self  # 设置只在列表页显示并返回自身

    def only_on_detail(self):
        self.show_on_index = False
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self  # 设置只在详情页显示并返回自身

    def only_on_forms(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self  # 设置只在表单页显示并返回自身

    def only_on_creating(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self  # 设置只在创建页显示并返回自身

    def only_on_updating(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self  # 设置只在编辑页显示并返回自身

    def only_on_export(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = False
        return self  # 设置只在导出时显示并返回自身

    def only_on_import(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = True
        return self  # 设置只在导入时显示并返回自身

    def except_on_forms(self):
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = True
        return self  # 设置在表单页隐藏并返回自身

    def is_shown_on_update(self):
        return self.show_on_update  # 检查是否在编辑页显示

    def is_shown_on_index(self):
        return self.show_on_index  # 检查是否在列表页显示

    def is_shown_on_detail(self):
        return self.show_on_detail  # 检查是否在详情页显示

    def is_shown_on_creation(self):
        return self.show_on_creation  # 检查是否在创建页显示

    def is_shown_on_export(self):
        return self.show_on_export  # 检查是否在导出时显示

    def is_shown_on_import(self):
        return self.show_on_import  # 检查是否在导入时显示

    def get_value_enum(self):
        return {}  # 获取列值枚举，目前返回空字典

    def set_callback(self, closure: Callable[[Dict[str, Any]], Any]):
        if closure is not None:
            self.callback = closure
        return self  # 设置回调函数并返回自身

    def get_callback(self):
        return self.callback  # 获取回调函数

    def set_api(self, api: str):
        self.api = api
        return self  # 设置数据接口地址并返回自身

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
        return self  # 设置默认值并返回自身

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

