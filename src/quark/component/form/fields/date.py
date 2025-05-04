import json
from typing import Dict, List, Any, Callable, Optional
from pydantic import BaseModel

# 模拟 rule 模块，定义校验规则类
class Rule(BaseModel):
    """
    表示表单字段的校验规则类。
    目前仅包含字段名，可根据实际需求扩展更多校验规则相关属性。
    """
    name: str = ""


class TableColumn:
    """
    表示表格列的类，用于定义列表页、详情页中列的属性。
    """
    def init(self):
        """
        初始化表格列实例。
        :return: 当前表格列实例
        """
        return self


# 模拟 when 模块
class WhenItem(BaseModel):
    """
    表示 When 组件中的单个条件项。
    包含条件触发时的内容、条件表达式、条件字段名、操作符和选项值。
    """
    body: Any = None  # 条件触发时执行的内容
    condition: str = ""  # 条件表达式
    condition_name: str = ""  # 条件所依赖的字段名
    condition_operator: str = ""  # 条件操作符，如 =、!= 等
    option: Any = None  # 条件判断的选项值


class WhenComponent(BaseModel):
    """
    表示 When 组件，用于管理多个 WhenItem 条件项。
    """
    items: List[WhenItem] = []  # 存储多个 WhenItem 实例的列表

    def set_items(self, items: List[WhenItem]):
        """
        设置 When 组件中的条件项列表。
        :param items: 包含多个 WhenItem 实例的列表
        :return: 当前 WhenComponent 实例
        """
        self.items = items
        return self


def new_when():
    """
    创建一个新的 WhenComponent 实例。
    :return: 新的 WhenComponent 实例
    """
    return WhenComponent()


def new_when_item():
    """
    创建一个新的 WhenItem 实例。
    :return: 新的 WhenItem 实例
    """
    return WhenItem()


class Component(BaseModel):
    """
    表示日期表单字段组件的类，包含该组件的各种属性和操作方法。
    """
    # 组件基本信息
    component_key: str = ""  # 组件标识
    component: str = ""  # 组件名称

    # 表单布局相关属性
    row_props: Optional[Dict[str, Any]] = None  # 开启 grid 模式时传递给 Row 的属性，仅在特定组件中有效
    col_props: Optional[Dict[str, Any]] = None  # 开启 grid 模式时传递给 Col 的属性
    secondary: bool = False  # 是否是次要控件，仅在 LightFilter 下有效
    colon: bool = True  # 配合 label 属性使用，表示是否显示 label 后面的冒号
    extra: str = ""  # 额外的提示信息，和 help 类似
    has_feedback: bool = False  # 配合 validateStatus 属性使用，展示校验状态图标
    help: str = ""  # 提示信息，如不设置，则会根据校验规则自动生成
    hidden: bool = False  # 是否隐藏字段（依然会收集和校验字段）
    initial_value: Any = None  # 设置子元素默认值，如果与 Form 的 initialValues 冲突则以 Form 为准
    label: str = ""  # label 标签的文本
    label_align: str = "right"  # 标签文本对齐方式
    label_col: Any = None  # label 标签布局，同 <Col> 组件
    name: str = ""  # 字段名，支持数组
    no_style: bool = False  # 为 true 时不带样式，作为纯字段控件使用
    required: bool = False  # 必填样式设置
    tooltip: str = ""  # 会在 label 旁增加一个 icon，悬浮后展示配置的信息
    value_prop_name: str = ""  # 子节点的值的属性
    wrapper_col: Any = None  # 需要为输入控件设置布局样式时使用

    # 表格列相关属性
    column: TableColumn = TableColumn().init()  # 列表页、详情页中列属性
    align: str = ""  # 设置列的对齐方式，left | right | center
    fixed: Any = None  # 列是否固定，可选 true (等效于 left)、left、right
    editable: bool = False  # 表格列是否可编辑
    ellipsis: bool = False  # 是否自动缩略
    copyable: bool = False  # 是否支持复制
    filters: Any = None  # 表头的筛选菜单项
    order: int = 0  # 查询表单中的权重，权重大排序靠前
    sorter: Any = None  # 可排序列
    span: int = 0  # 包含列的数量，只在详情页中有效
    column_width: int = 0  # 设置列宽

    # 其他通用属性
    api: str = ""  # 获取数据接口
    ignore: bool = False  # 是否忽略保存到数据库
    rules: List[Rule] = []  # 全局校验规则
    creation_rules: List[Rule] = []  # 创建页校验规则
    update_rules: List[Rule] = []  # 编辑页校验规则
    frontend_rules: List[Rule] = []  # 前端校验规则
    when: Optional[WhenComponent] = None  # When 组件实例
    when_item: List[WhenItem] = []  # When 组件的条件项列表
    show_on_index: bool = True  # 在列表页展示
    show_on_detail: bool = True  # 在详情页展示
    show_on_creation: bool = True  # 在创建页面展示
    show_on_update: bool = True  # 在编辑页面展示
    show_on_export: bool = True  # 在导出的 Excel 上展示
    show_on_import: bool = True  # 在导入 Excel 上展示
    callback: Optional[Callable[[Dict[str, Any]], Any]] = None  # 回调函数

    # 日期组件特有的属性
    allow_clear: bool = True  # 是否支持清除
    auto_focus: bool = False  # 自动获取焦点
    bordered: bool = True  # 是否有边框
    class_name: str = ""  # 自定义类名
    default_value: Any = None  # 默认的选中项
    disabled: Any = None  # 禁用状态
    format: str = "YYYY-MM-DD"  # 设置日期格式
    popup_class_name: str = ""  # 额外的弹出日历 className
    input_read_only: bool = False  # 设置输入框为只读
    locale: Any = None  # 国际化配置
    mode: str = ""  # 日期面板的状态
    next_icon: Any = None  # 自定义下一个图标
    open: bool = False  # 控制浮层显隐
    picker: str = ""  # 设置选择器类型
    placeholder: str = "请选择"  # 输入框占位文本
    placement: str = ""  # 浮层预设位置
    popup_style: Any = None  # 额外的弹出日历样式
    prev_icon: Any = None  # 自定义上一个图标
    size: str = ""  # 输入框大小
    status: str = ""  # 设置校验状态
    style: Dict[str, Any] = {}  # 自定义样式
    suffix_icon: Any = None  # 自定义的选择框后缀图标
    super_next_icon: Any = None  # 自定义 << 切换图标
    super_prev_icon: Any = None  # 自定义 >> 切换图标
    value: Any = None  # 指定选中项
    default_picker_value: str = ""  # 默认面板日期
    show_now: bool = False  # 当设定了 showTime 的时候，面板是否显示“此刻”按钮
    show_time: Any = None  # 增加时间选择功能
    show_today: bool = False  # 是否展示“今天”按钮

    @classmethod
    def new(cls):
        """
        类方法，用于创建一个新的 Component 实例并进行初始化。
        :return: 初始化后的 Component 实例
        """
        return cls().init()

    def init(self):
        """
        初始化组件的属性，设置一些默认值。
        :return: 当前 Component 实例
        """
        self.component = "dateField"
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
        self.format = "YYYY-MM-DD"
        # 这里需要实现 hex.Make 功能
        # self.set_key(component.DEFAULT_KEY, component.DEFAULT_CRYPT)
        return self

    def set_key(self, key: str, crypt: bool):
        """
        设置组件的标识。
        :param key: 要设置的组件标识
        :param crypt: 是否加密，在当前实现中未使用，需实现 hex.Make 功能
        :return: 当前 Component 实例
        """
        # 需实现 hex.Make 功能
        self.component_key = key
        return self

    def set_style(self, style: Dict[str, Any]):
        """
        设置组件的自定义样式。
        :param style: 包含样式属性的字典
        :return: 当前 Component 实例
        """
        self.style = style
        return self

    def set_tooltip(self, tooltip: str):
        """
        设置 label 旁的提示信息。
        :param tooltip: 提示信息内容
        :return: 当前 Component 实例
        """
        self.tooltip = tooltip
        return self

    def set_width(self, width: Any):
        """
        设置组件的宽度，通过更新样式属性实现。
        :param width: 宽度值，可以是字符串或数字
        :return: 当前 Component 实例
        """
        style = self.style.copy()
        style["width"] = width
        self.style = style
        return self

    def set_row_props(self, row_props: Dict[str, Any]):
        """
        设置开启 grid 模式时传递给 Row 的属性。
        :param row_props: 包含 Row 属性的字典
        :return: 当前 Component 实例
        """
        self.row_props = row_props
        return self

    def set_col_props(self, col_props: Dict[str, Any]):
        """
        设置开启 grid 模式时传递给 Col 的属性。
        :param col_props: 包含 Col 属性的字典
        :return: 当前 Component 实例
        """
        self.col_props = col_props
        return self

    def set_secondary(self, secondary: bool):
        """
        设置是否为次要控件。
        :param secondary: 是否为次要控件的布尔值
        :return: 当前 Component 实例
        """
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool):
        """
        设置是否显示 label 后面的冒号。
        :param colon: 是否显示冒号的布尔值
        :return: 当前 Component 实例
        """
        self.colon = colon
        return self

    def set_extra(self, extra: str):
        """
        设置额外的提示信息。
        :param extra: 额外提示信息内容
        :return: 当前 Component 实例
        """
        self.extra = extra
        return self

    def set_has_feedback(self, has_feedback: bool):
        """
        设置是否展示校验状态图标。
        :param has_feedback: 是否展示图标的布尔值
        :return: 当前 Component 实例
        """
        self.has_feedback = has_feedback
        return self

    def set_help(self, help: str):
        """
        设置提示信息。
        :param help: 提示信息内容
        :return: 当前 Component 实例
        """
        self.help = help
        return self

    def set_no_style(self):
        """
        设置为不带样式的纯字段控件。
        :return: 当前 Component 实例
        """
        self.no_style = True
        return self

    def set_label(self, label: str):
        """
        设置 label 标签的文本。
        :param label: label 文本内容
        :return: 当前 Component 实例
        """
        self.label = label
        return self

    def set_label_align(self, align: str):
        """
        设置标签文本的对齐方式。
        :param align: 对齐方式字符串，如 'left'、'right'、'center'
        :return: 当前 Component 实例
        """
        self.label_align = align
        return self

    def set_label_col(self, col: Any):
        """
        设置 label 标签的布局。
        :param col: 布局设置，可以是字典或其他合适的数据结构
        :return: 当前 Component 实例
        """
        self.label_col = col
        return self

    def set_name(self, name: str):
        """
        设置字段名。
        :param name: 字段名
        :return: 当前 Component 实例
        """
        self.name = name
        return self

    def set_name_as_label(self):
        """
        将字段名转换为 label 文本，将字段名的首字母大写。
        :return: 当前 Component 实例
        """
        self.label = self.name.title()
        return self

    def set_required(self):
        """
        设置字段为必填项。
        :return: 当前 Component 实例
        """
        self.required = True
        return self

    def build_frontend_rules(self, path: str):
        """
        根据当前路径生成前端验证规则。
        :param path: 当前请求的路径
        :return: 当前 Component 实例
        """
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
        return self

    def set_rules(self, rules: List[Rule]):
        """
        设置全局校验规则，并为每个规则设置字段名。
        :param rules: 包含多个 Rule 实例的列表
        :return: 当前 Component 实例
        """
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Rule]):
        """
        设置创建页校验规则，并为每个规则设置字段名。
        :param rules: 包含多个 Rule 实例的列表
        :return: 当前 Component 实例
        """
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    def set_update_rules(self, rules: List[Rule]):
        """
        设置编辑页校验规则，并为每个规则设置字段名。
        :param rules: 包含多个 Rule 实例的列表
        :return: 当前 Component 实例
        """
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self

    def get_rules(self):
        """
        获取全局校验规则列表。
        :return: 包含多个 Rule 实例的列表
        """
        return self.rules

    def get_creation_rules(self):
        """
        获取创建页校验规则列表。
        :return: 包含多个 Rule 实例的列表
        """
        return self.creation_rules

    def get_update_rules(self):
        """
        获取编辑页校验规则列表。
        :return: 包含多个 Rule 实例的列表
        """
        return self.update_rules

    def set_value_prop_name(self, value_prop_name: str):
        """
        设置子节点的值的属性名。
        :param value_prop_name: 属性名
        :return: 当前 Component 实例
        """
        self.value_prop_name = value_prop_name
        return self

    def set_wrapper_col(self, col: Any):
        """
        设置输入控件的布局样式。
        :param col: 布局设置，可以是字典或其他合适的数据结构
        :return: 当前 Component 实例
        """
        self.wrapper_col = col
        return self

    def set_column(self, f: Callable[[TableColumn], TableColumn]):
        """
        通过传入的函数设置列表页、详情页中列属性。
        :param f: 处理 TableColumn 实例的函数
        :return: 当前 Component 实例
        """
        self.column = f(self.column)
        return self

    def set_align(self, align: str):
        """
        设置列的对齐方式。
        :param align: 对齐方式字符串，如 'left'、'right'、'center'
        :return: 当前 Component 实例
        """
        self.align = align
        return self

    def set_fixed(self, fixed: Any):
        """
        设置列是否固定。
        :param fixed: 固定设置，可以是布尔值、字符串等
        :return: 当前 Component 实例
        """
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool):
        """
        设置表格列是否可编辑。
        :param editable: 是否可编辑的布尔值
        :return: 当前 Component 实例
        """
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool):
        """
        设置是否自动缩略。
        :param ellipsis: 是否自动缩略的布尔值
        :return: 当前 Component 实例
        """
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        """
        设置是否支持复制。
        :param copyable: 是否支持复制的布尔值
        :return: 当前 Component 实例
        """
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any):
        """
        设置表头的筛选菜单项。如果传入的是字典，将其转换为特定格式的列表。
        :param filters: 筛选菜单项设置，可以是字典或其他合适的数据结构
        :return: 当前 Component 实例
        """
        if isinstance(filters, dict):
            tmp_filters = []
            for k, v in filters.items():
                tmp_filters.append({"text": v, "value": k})
            self.filters = tmp_filters
        else:
            self.filters = filters
        return self

    def set_order(self, order: int):
        """
        设置查询表单中的权重。
        :param order: 权重值，整数类型
        :return: 当前 Component 实例
        """
        self.order = order
        return self

    def set_sorter(self, sorter: bool):
        """
        设置是否为可排序列。
        :param sorter: 是否可排序的布尔值
        :return: 当前 Component 实例
        """
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        """
        设置包含列的数量，只在详情页中有效。
        :param span: 列数量，整数类型
        :return: 当前 Component 实例
        """
        self.span = span
        return self

    def set_column_width(self, width: int):
        """
        设置列宽，只在列表页中有效。
        :param width: 列宽值，整数类型
        :return: 当前 Component 实例
        """
        self.column_width = width
        return self

    def set_value(self, value: Any):
        """
        设置组件的值。
        :param value: 组件的值，可以是任意类型
        :return: 当前 Component 实例
        """
        self.value = value
        return self

    def set_default(self, value: Any):
        """
        设置组件的默认值。
        :param value: 默认值，可以是任意类型
        :return: 当前 Component 实例
        """
        self.default_value = value
        return self

    def set_disabled(self, disabled: bool):
        """
        设置组件是否禁用。
        :param disabled: 是否禁用的布尔值
        :return: 当前 Component 实例
        """
        self.disabled = disabled
        return self

    def set_ignore(self, ignore: bool):
        """
        设置是否忽略保存到数据库。
        :param ignore: 是否忽略的布尔值
        :return: 当前 Component 实例
        """
        self.ignore = ignore
        return self

    def set_when(self, *value):
        """
        设置 When 组件的数据，根据传入的参数生成条件项并添加到 When 组件中。
        :param value: 可变参数，根据不同情况设置条件和回调
        :return: 当前 Component 实例
        """
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
        return self

    def get_when(self):
        """
        获取 When 组件实例。
        :return: WhenComponent 实例或 None
        """
        return self.when

    def hide_from_index(self, callback: bool):
        """
        指定元素是否在列表页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool):
        """
        指定元素是否在详情页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool):
        """
        指定元素是否在创建页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool):
        """
        指定元素是否在编辑页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_update = not callback
        return self

    def hide_when_exporting(self, callback: bool):
        """
        指定元素是否在导出文件时隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_export = not callback
        return self

    def hide_when_importing(self, callback: bool):
        """
        指定元素是否在导入文件时隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_import = not callback
        return self

    def on_index_showing(self, callback: bool):
        """
        指定元素是否在列表页显示。
        :param callback: 是否显示的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_index = callback
        return self

    def on_detail_showing(self, callback: bool):
        """
        指定元素是否在详情页显示。
        :param callback: 是否显示的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_detail = callback
        return self

    def show_on_creating(self, callback: bool):
        """
        指定元素是否在创建页显示。
        :param callback: 是否显示的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_creation = callback
        return self

    def show_on_updating(self, callback: bool):
        """
        指定元素是否在编辑页显示。
        :param callback: 是否显示的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_update = callback
        return self

    def show_on_exporting(self, callback: bool):
        """
        指定元素是否在导出文件时显示。
        :param callback: 是否显示的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_export = callback
        return self

    def show_on_importing(self, callback: bool):
        """
        指定元素是否在导入文件时显示。
        :param callback: 是否显示的布尔值
        :return: 当前 Component 实例
        """
        self.show_on_import = callback
        return self

    def only_on_index(self):
        """
        指定元素只在列表页显示，其他页面隐藏。
        :return: 当前 Component 实例
        """
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_detail(self):
        """
        指定元素只在详情页显示，其他页面隐藏。
        :return: 当前 Component 实例
        """
        self.show_on_index = False
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_forms(self):
        """
        指定元素只在表单页（创建页和编辑页）显示，其他页面隐藏。
        :return: 当前 Component 实例
        """
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_creating(self):
        """
        指定元素只在创建页显示，其他页面隐藏。
        :return: 当前 Component 实例
        """
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_updating(self):
        """
        指定元素只在编辑页显示，其他页面隐藏。
        :return: 当前 Component 实例
        """
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_export(self):
        """
        指定元素只在导出文件时显示，其他页面隐藏。
        :return: 当前 Component 实例
        """
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = False
        return self

    def only_on_import(self):
        """
        指定元素只在导入文件时显示，其他页面隐藏。
        :return: 当前 Component 实例
        """
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = True
        return self

    def except_on_forms(self):
        """
        指定元素在表单页（创建页和编辑页）隐藏，其他页面显示。
        :return: 当前 Component 实例
        """
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = True
        return self

    def is_shown_on_update(self):
        """
        检查元素是否在编辑页显示。
        :return: 是否显示的布尔值
        """
        return self.show_on_update

    def is_shown_on_index(self):
        """
        检查元素是否在列表页显示。
        :return: 是否显示的布尔值
        """
        return self.show_on_index

    def is_shown_on_detail(self):
        """
        检查元素是否在详情页显示。
        :return: 是否显示的布尔值
        """
        return self.show_on_detail

    def is_shown_on_creation(self):
        """
        检查元素是否在创建页显示。
        :return: 是否显示的布尔值
        """
        return self.show_on_creation

    def is_shown_on_export(self):
        """
        检查元素是否在导出文件时显示。
        :return: 是否显示的布尔值
        """
        return self.show_on_export

    def is_shown_on_import(self):
        """
        检查元素是否在导入文件时显示。
        :return: 是否显示的布尔值
        """
        return self.show_on_import

    def get_value_enum(self):
        """
        获取当前列值的枚举，目前返回空字典，可根据实际需求实现。
        :return: 包含列值枚举的字典
        """
        return {}

    def set_callback(self, closure: Callable[[Dict[str, Any]], Any]):
        """
        设置回调函数。
        :param closure: 回调函数，接收一个字典参数并返回任意类型的值
        :return: 当前 Component 实例
        """
        if closure is not None:
            self.callback = closure
        return self

    def get_callback(self):
        """
        获取回调函数。
        :return: 回调函数或 None
        """
        return self.callback

    def set_api(self, api: str):
        """
        设置获取数据的接口地址。
        :param api: 接口地址字符串
        :return: 当前 Component 实例
        """
        self.api = api
        return self

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
        """
        设置组件的默认选中项。
        :param default_value: 默认选中项，可以是任意类型
        :return: 当前 Component 实例
        """
        self.default_value = default_value
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

