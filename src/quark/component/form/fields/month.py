import json
from typing import Dict, List, Optional, Any, Callable
from .base import Base

class Month(Base):
    """
    表示月份选择组件的类，使用 pydantic 进行数据验证和序列化。

    Attributes:
        component (str): 组件名称，默认为 "monthField"。
        allow_clear (bool): 是否支持清除，默认值为 True。
        auto_focus (bool): 自动获取焦点，默认值为 False。
        bordered (bool): 是否有边框，默认值为 True。
        class_name (str): 自定义类名。
        default_value (Optional[Any]): 默认的选中项。
        disabled (Optional[Any]): 禁用。
        format (str): 设置日期格式，为数组时支持多格式匹配，展示以第一个为准。
        popup_class_name (str): 额外的弹出日历 className。
        input_read_only (bool): 设置输入框为只读（避免在移动设备上打开虚拟键盘）。
        locale (Optional[Any]): 国际化配置。
        mode (str): 日期面板的状态 time | date | month | year | decade。
        next_icon (Optional[Any]): 自定义下一个图标。
        open (bool): 控制浮层显隐。
        picker (str): 设置选择器类型 date | week | month | quarter | year。
        placeholder (str): 输入框占位文本，默认为 "请选择"。
        placement (str): 浮层预设位置，bottomLeft bottomRight topLeft topRight。
        popup_style (Optional[Any]): 额外的弹出日历样式。
        prev_icon (Optional[Any]): 自定义上一个图标。
        size (str): 输入框大小，large | middle | small。
        status (str): 设置校验状态，'error' | 'warning'。
        style (Dict[str, Any]): 自定义样式。
        suffix_icon (Optional[Any]): 自定义的选择框后缀图标。
        super_next_icon (Optional[Any]): 自定义 << 切换图标。
        super_prev_icon (Optional[Any]): 自定义 >> 切换图标。
        value (Optional[Any]): 指定选中项,string[] | number[]。
        default_picker_value (str): 默认面板日期。
        show_now (bool): 当设定了 show_time 的时候，面板是否显示“此刻”按钮。
        show_time (Optional[Any]): 增加时间选择功能。
        show_today (bool): 是否展示“今天”按钮。
    """
    component: str = "monthField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    组件名称
    """

    auto_focus: bool = False
    """
    组件名称
    """

    bordered: bool = True
    """
    组件名称
    """

    class_name: str = ""
    default_value: Optional[Any] = None
    disabled: Optional[Any] = None
    format: str = ""
    popup_class_name: str = ""
    input_read_only: bool = False
    locale: Optional[Any] = None
    mode: str = ""
    next_icon: Optional[Any] = None
    open: bool = False
    picker: str = ""
    placeholder: str = "请选择"
    placement: str = ""
    popup_style: Optional[Any] = None
    prev_icon: Optional[Any] = None
    size: str = ""
    status: str = ""
    style: Dict[str, Any] = {}
    suffix_icon: Optional[Any] = None
    super_next_icon: Optional[Any] = None
    super_prev_icon: Optional[Any] = None
    value: Optional[Any] = None
    default_picker_value: str = ""
    show_now: bool = False
    show_time: Optional[Any] = None
    show_today: bool = False

    @classmethod
    def new(cls):
        """
        创建并初始化组件实例。

        Returns:
            Component: 初始化后的组件实例。
        """
        return cls().init()

    def init(self):
        """
        初始化组件属性。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.component = "monthField"
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

    def set_key(self, key: str, crypt: bool):
        """
        设置组件 key。

        Args:
            key (str): 要设置的 key 值。
            crypt (bool): 是否加密。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        # 模拟 hex.Make 函数
        self.component_key = key
        return self

    def set_style(self, style: Dict[str, Any]):
        """
        设置自定义样式。

        Args:
            style (Dict[str, Any]): 样式字典。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.style = style
        return self

    def set_tooltip(self, tooltip: str):
        """
        设置 label 旁提示信息。

        Args:
            tooltip (str): 提示信息内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.tooltip = tooltip
        return self

    def set_width(self, width: Any):
        """
        设置组件宽度。

        Args:
            width (Any): 宽度值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        style = self.style.copy()
        style["width"] = width
        self.style = style
        return self

    def set_row_props(self, row_props: Dict[str, Any]):
        """
        设置 grid 模式下 Row 属性。

        Args:
            row_props (Dict[str, Any]): 属性字典。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.row_props = row_props
        return self

    def set_col_props(self, col_props: Dict[str, Any]):
        """
        设置 grid 模式下 Col 属性。

        Args:
            col_props (Dict[str, Any]): 属性字典。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.col_props = col_props
        return self

    def set_secondary(self, secondary: bool):
        """
        设置是否为次要控件。

        Args:
            secondary (bool): 是否为次要控件。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool):
        """
        设置是否显示 label 后的冒号。

        Args:
            colon (bool): 是否显示冒号。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.colon = colon
        return self

    def set_extra(self, extra: str):
        """
        设置额外提示信息。

        Args:
            extra (str): 额外提示信息内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.extra = extra
        return self

    def set_has_feedback(self, has_feedback: bool):
        """
        设置是否展示校验状态图标。

        Args:
            has_feedback (bool): 是否展示图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.has_feedback = has_feedback
        return self

    def set_help(self, help_text: str):
        """
        设置提示信息。

        Args:
            help_text (str): 提示信息内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.help = help_text
        return self

    def set_no_style(self):
        """
        设置组件无样式。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.no_style = True
        return self

    def set_label(self, label: str):
        """
        设置 label 标签文本。

        Args:
            label (str): 标签文本内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.label = label
        return self

    def set_label_align(self, align: str):
        """
        设置标签文本对齐方式。

        Args:
            align (str): 对齐方式，如 'left', 'right', 'center'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.label_align = align
        return self

    def set_label_col(self, col: Any):
        """
        设置 label 标签布局。

        Args:
            col (Any): 布局信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.label_col = col
        return self

    def set_name(self, name: str):
        """
        设置字段名。

        Args:
            name (str): 字段名。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.name = name
        return self

    def set_name_as_label(self):
        """
        将字段名转为 label 标签文本。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if self.name:
            self.label = Case.of(self.name).to(Style.Title)
        return self

    def set_required(self):
        """
        设置字段为必填项。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.required = True
        return self

    def build_frontend_rules(self, path: str):
        """
        生成前端验证规则。

        Args:
            path (str): 当前路径，判断创建或编辑操作。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        frontend_rules: List[Rule] = []
        rules: List[Rule] = []
        creation_rules: List[Rule] = []
        update_rules: List[Rule] = []

        uri = path.split("/")
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        if self.rules:
            rules = self.rules
        if is_creating and self.creation_rules:
            creation_rules = self.creation_rules
        if is_editing and self.update_rules:
            update_rules = self.update_rules

        frontend_rules.extend(rules)
        frontend_rules.extend(creation_rules)
        frontend_rules.extend(update_rules)

        self.frontend_rules = frontend_rules
        return self

    def set_rules(self, rules: List[Rule]):
        """
        设置全局校验规则。

        Args:
            rules (List[Rule]): 校验规则列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Rule]):
        """
        设置创建页校验规则。

        Args:
            rules (List[Rule]): 校验规则列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    def set_update_rules(self, rules: List[Rule]):
        """
        设置编辑页校验规则。

        Args:
            rules (List[Rule]): 校验规则列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self

    def get_rules(self) -> List[Rule]:
        """
        获取全局校验规则。

        Returns:
            List[Rule]: 全局校验规则列表。
        """
        return self.rules

    def get_creation_rules(self) -> List[Rule]:
        """
        获取创建页校验规则。

        Returns:
            List[Rule]: 创建页校验规则列表。
        """
        return self.creation_rules

    def get_update_rules(self) -> List[Rule]:
        """
        获取编辑页校验规则。

        Returns:
            List[Rule]: 编辑页校验规则列表。
        """
        return self.update_rules

    def set_value_prop_name(self, value_prop_name: str):
        """
        设置子节点值属性名。

        Args:
            value_prop_name (str): 属性名。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.value_prop_name = value_prop_name
        return self

    def set_wrapper_col(self, col: Any):
        """
        设置输入控件布局样式。

        Args:
            col (Any): 布局信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.wrapper_col = col
        return self

    def set_column(self, f: Callable[[TableColumn], TableColumn]):
        """
        设置列表页、详情页中列属性。

        Args:
            f (Callable[[TableColumn], TableColumn]): 处理列属性的函数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.column = f(self.column)
        return self

    def set_align(self, align: str):
        """
        设置列的对齐方式。

        Args:
            align (str): 对齐方式，如 'left', 'right', 'center'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.align = align
        return self

    def set_fixed(self, fixed: Any):
        """
        设置列是否固定。

        Args:
            fixed (Any): 固定状态。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool):
        """
        设置表格列是否可编辑。

        Args:
            editable (bool): 是否可编辑。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool):
        """
        设置是否自动缩略。

        Args:
            ellipsis (bool): 是否自动缩略。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        """
        设置是否支持复制。

        Args:
            copyable (bool): 是否支持复制。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any):
        """
        设置表头筛选菜单项。

        Args:
            filters (Any): 筛选菜单项信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        try:
            get_filters = dict(filters)
            tmp_filters = []
            for k, v in get_filters.items():
                tmp_filters.append({"text": v, "value": k})
            self.filters = tmp_filters
        except (TypeError, ValueError):
            self.filters = filters
        return self

    def set_order(self, order: int):
        """
        设置查询表单权重。

        Args:
            order (int): 权重值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.order = order
        return self

    def set_sorter(self, sorter: bool):
        """
        设置可排序列。

        Args:
            sorter (bool): 是否可排序。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        """
        设置详情页包含列数量。

        Args:
            span (int): 列数量。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.span = span
        return self

    def set_column_width(self, width: int):
        """
        设置列表页列宽。

        Args:
            width (int): 列宽值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.column_width = width
        return self

    def set_value(self, value: Any):
        """
        设置指定选中项。

        Args:
            value (Any): 指定选中项。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.value = value
        return self

    def set_default(self, value: Any):
        """
        设置默认选中项。

        Args:
            value (Any): 默认选中项。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_value = value
        return self

    def set_disabled(self, disabled: bool):
        """
        设置是否禁用状态。

        Args:
            disabled (bool): 是否禁用。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.disabled = disabled
        return self

    def set_ignore(self, ignore: bool):
        """
        设置是否忽略保存到数据库。

        Args:
            ignore (bool): 是否忽略。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.ignore = ignore
        return self

    def set_when(self, *value: Any):
        """
        设置 When 组件数据。

        Args:
            *value: 可变参数，不同数量有不同含义。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        w = WhenComponent()
        i = WhenItem()
        operator: str = ""
        option: Any = None

        if len(value) == 2:
            operator = "="
            option = value[0]
            callback = value[1]
            if callable(callback):
                i.body = callback()
        elif len(value) == 3:
            operator = value[0]
            option = value[1]
            callback = value[2]
            if callable(callback):
                i.body = callback()

        def any_to_string(o: Any) -> str:
            return str(o)

        get_option = any_to_string(option)
        if self.name:
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

    def get_when(self) -> WhenComponent:
        """
        获取 When 组件数据。

        Returns:
            WhenComponent: When 组件实例。
        """
        return self.when

    def hide_from_index(self, callback: bool):
        """
        指定元素是否在列表页隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool):
        """
        指定元素是否在详情页隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool):
        """
        指定元素是否在创建页隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool):
        """
        指定元素是否在编辑页隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_update = not callback
        return self

    def hide_when_exporting(self, callback: bool):
        """
        指定元素是否在导出 Excel 隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_export = not callback
        return self

    def hide_when_importing(self, callback: bool):
        """
        指定元素是否在导入 Excel 隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_import = not callback
        return self

    def on_index_showing(self, callback: bool):
        """
        指定元素是否在列表页显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_index = callback
        return self

    def on_detail_showing(self, callback: bool):
        """
        指定元素是否在详情页显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_detail = callback
        return self

    def show_on_creating(self, callback: bool):
        """
        指定元素是否在创建页显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_creation = callback
        return self

    def show_on_updating(self, callback: bool):
        """
        指定元素是否在编辑页显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_update = callback
        return self

    def show_on_exporting(self, callback: bool):
        """
        指定元素是否在导出 Excel 显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_export = callback
        return self

    def show_on_importing(self, callback: bool):
        """
        指定元素是否在导入 Excel 显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_import = callback
        return self

    def only_on_index(self):
        """
        指定元素只在列表页显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
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
        指定元素只在详情页显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
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
        指定元素只在表单页显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
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
        指定元素只在创建页显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
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
        指定元素只在编辑页显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
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
        指定元素只在导出 Excel 显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
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
        指定元素只在导入 Excel 显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
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
        指定元素在表单页隐藏。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = True
        return self

    def is_shown_on_update(self) -> bool:
        """
        检查元素是否在编辑页显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_update

    def is_shown_on_index(self) -> bool:
        """
        检查元素是否在列表页显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_index

    def is_shown_on_detail(self) -> bool:
        """
        检查元素是否在详情页显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_detail

    def is_shown_on_creation(self) -> bool:
        """
        检查元素是否在创建页显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_creation

    def is_shown_on_export(self) -> bool:
        """
        检查元素是否在导出 Excel 显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_export

    def is_shown_on_import(self) -> bool:
        """
        检查元素是否在导入 Excel 显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_import

    def get_value_enum(self) -> Dict[Any, Any]:
        """
        获取当前列值枚举。

        Returns:
            Dict[Any, Any]: 列值枚举字典。
        """
        data: Dict[Any, Any] = {}
        return data

    def set_callback(self, closure: Optional[Callable[[Dict[str, Any]], Any]]):
        """
        设置回调函数。

        Args:
            closure (Optional[Callable[[Dict[str, Any]], Any]]): 回调函数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if closure is not None:
            self.callback = closure
        return self

    def get_callback(self) -> Any:
        """
        获取回调函数。

        Returns:
            Any: 回调函数。
        """
        return self.callback

    def set_api(self, api: str):
        """
        设置获取数据接口。

        Args:
            api (str): 接口地址。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.api = api
        return self

    def set_allow_clear(self, allow_clear: bool):
        """
        设置是否支持清除。

        Args:
            allow_clear (bool): 是否支持清除。

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
            class_name (str): 类名。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.class_name = class_name
        return self

    def set_default_value(self, default_value: Any):
        """
        设置默认选中项。

        Args:
            default_value (Any): 默认选中项。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_value = default_value
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
            open (bool): 是否显示浮层。

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
        设置输入框大小。

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
            show_now (bool): 是否显示“此刻”按钮。

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
            show_today (bool): 是否展示“今天”按钮。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_today = show_today
        return self