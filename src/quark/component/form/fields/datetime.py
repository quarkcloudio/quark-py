"""
此模块定义了 `Component` 类，用于处理日期时间相关的表单字段组件。
包含组件属性的定义和一系列方法，用于设置和获取组件的各种属性。
"""
from pydantic import BaseModel
from typing import Dict, Any, List, Optional, Callable, Union

# 假设 table.Column 和 rule.Rule 是其他模块定义的类，这里简单模拟
class Column(BaseModel):
    """模拟表格列的类，用于表示列表页、详情页中列属性。"""
    pass


class Rule(BaseModel):
    """模拟校验规则的类，用于定义字段的校验逻辑。"""
    name: Optional[str] = None


class WhenItem(BaseModel):
    """
    表示 When 组件中的条件项，用于根据特定条件显示不同内容。

    Attributes:
        body (Any): 条件满足时的执行内容。
        condition (str): 条件表达式，用于判断条件是否满足。
        condition_name (str): 条件关联的字段名。
        condition_operator (str): 条件操作符，如 "=", "!=" 等。
        option (Any): 条件操作数。
    """
    body: Any
    condition: str
    condition_name: str
    condition_operator: str
    option: Any


class WhenComponent(BaseModel):
    """
    表示 When 组件，用于根据条件显示不同内容。

    Attributes:
        items (List[WhenItem]): 条件项列表，包含多个 WhenItem 实例。
    """
    items: List[WhenItem] = []

    def set_items(self, items: List[WhenItem]):
        """
        设置 When 组件的条件项列表。

        Args:
            items (List[WhenItem]): 要设置的条件项列表。

        Returns:
            WhenComponent: 返回当前 WhenComponent 实例，支持链式调用。
        """
        self.items = items
        return self


class Component(BaseModel):
    """
    表示日期时间表单字段组件，包含组件的各种属性和方法。

    Attributes:
        component_key (str): 组件标识，用于唯一标识组件。
        component (str): 组件名称，默认为 "datetimeField"。
        row_props (Optional[Dict[str, Any]]): 开启 grid 模式时传递给 Row 的属性。
        col_props (Optional[Dict[str, Any]]): 开启 grid 模式时传递给 Col 的属性。
        secondary (bool): 是否是次要控件，默认为 False，仅在 LightFilter 下有效。
        colon (bool): 配合 label 属性使用，表示是否显示 label 后面的冒号，默认为 True。
        extra (Optional[str]): 额外的提示信息，和 help 类似。
        has_feedback (bool): 配合 validateStatus 属性使用，展示校验状态图标，默认为 False。
        help_text (Optional[str]): 提示信息，如不设置，会根据校验规则自动生成。
        hidden (bool): 是否隐藏字段，默认为 False，但依然会收集和校验字段。
        initial_value (Optional[Any]): 设置子元素默认值，若与 Form 的 initialValues 冲突以 Form 为准。
        label (Optional[str]): label 标签的文本。
        label_align (str): 标签文本对齐方式，默认为 "right"。
        label_col (Optional[Any]): label 标签布局，同 <Col> 组件。
        name (Optional[str]): 字段名，支持数组形式。
        no_style (bool): 为 True 时不带样式，作为纯字段控件使用，默认为 False。
        required (bool): 必填样式设置，默认为 False，如不设置，会根据校验规则自动生成。
        tooltip (Optional[str]): 会在 label 旁增加一个 icon，悬浮后展示配置的信息。
        value_prop_name (Optional[str]): 子节点的值的属性，如 Switch 的是 'checked'。
        wrapper_col (Optional[Any]): 需要为输入控件设置布局样式时使用的属性，用法同 label_col。
        column (Column): 列表页、详情页中列属性，默认为 Column 实例。
        align (str): 设置列的对齐方式，取值为 'left', 'right', 'center'。
        fixed (Optional[Any]): 列是否固定，可选 true (等效于 left)、left、right，仅在列表页有效。
        editable (bool): 表格列是否可编辑，默认为 False，仅在列表页有效。
        ellipsis (bool): 是否自动缩略，默认为 False，仅在列表页、详情页有效。
        copyable (bool): 是否支持复制，默认为 False，仅在列表页、详情页有效。
        filters (Optional[Any]): 表头的筛选菜单项，当值为 true 时，自动使用 valueEnum 生成，仅在列表页有效。
        order (int): 查询表单中的权重，权重大排序靠前，默认为 0，仅在列表页有效。
        sorter (Optional[Any]): 可排序列，仅在列表页有效。
        span (int): 包含列的数量，默认为 0，仅在详情页有效。
        column_width (int): 设置列宽，默认为 0，仅在列表页有效。
        api (Optional[str]): 获取数据接口。
        ignore (bool): 是否忽略保存到数据库，默认为 False。
        rules (List[Rule]): 全局校验规则，默认为空列表。
        creation_rules (List[Rule]): 创建页校验规则，默认为空列表。
        update_rules (List[Rule]): 编辑页校验规则，默认为空列表。
        frontend_rules (List[Rule]): 前端校验规则，设置字段的校验逻辑。
        when (WhenComponent): When 组件，用于根据条件显示不同内容。
        when_item (List[WhenItem]): When 组件的条件项列表，默认为空列表。
        show_on_index (bool): 在列表页展示，默认为 True。
        show_on_detail (bool): 在详情页展示，默认为 True。
        show_on_creation (bool): 在创建页面展示，默认为 True。
        show_on_update (bool): 在编辑页面展示，默认为 True。
        show_on_export (bool): 在导出的 Excel 上展示，默认为 True。
        show_on_import (bool): 在导入 Excel 上展示，默认为 True。
        callback (Optional[Any]): 回调函数。
        allow_clear (bool): 是否支持清除，默认为 True。
        auto_focus (bool): 自动获取焦点，默认为 False。
        bordered (bool): 是否有边框，默认为 True。
        class_name (Optional[str]): 自定义类名。
        default_value (Optional[Any]): 默认的选中项。
        disabled (Optional[Any]): 禁用状态。
        format_str (Optional[str]): 设置日期格式，为数组时支持多格式匹配，展示以第一个为准。
        popup_class_name (Optional[str]): 额外的弹出日历 className。
        input_read_only (bool): 设置输入框为只读，默认为 False，避免在移动设备上打开虚拟键盘。
        locale (Optional[Any]): 国际化配置。
        mode (Optional[str]): 日期面板的状态，取值为 'time', 'date', 'month', 'year', 'decade'。
        next_icon (Optional[Any]): 自定义下一个图标。
        open_flag (bool): 控制浮层显隐，默认为 False。
        picker (Optional[str]): 设置选择器类型，取值为 'date', 'week', 'month', 'quarter', 'year'。
        placeholder (Optional[str]): 输入框占位文本，默认为 "请选择"。
        placement (Optional[str]): 浮层预设位置，取值为 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'。
        popup_style (Optional[Any]): 额外的弹出日历样式。
        prev_icon (Optional[Any]): 自定义上一个图标。
        size (Optional[str]): 输入框大小，取值为 'large', 'middle', 'small'。
        status (Optional[str]): 设置校验状态，取值为 'error', 'warning'。
        style (Optional[Dict[str, Any]]): 自定义样式。
        suffix_icon (Optional[Any]): 自定义的选择框后缀图标。
        super_next_icon (Optional[Any]): 自定义 << 切换图标。
        super_prev_icon (Optional[Any]): 自定义 >> 切换图标。
        value (Optional[Any]): 指定选中项，类型为 string[] | number[]。
        default_picker_value (Optional[str]): 默认面板日期。
        show_now (bool): 当设定了 show_time 的时候，面板是否显示“此刻”按钮，默认为 False。
        show_time (Optional[Any]): 增加时间选择功能。
        show_today (bool): 是否展示“今天”按钮，默认为 False。
    """
    component_key: str
    component: str = "datetimeField"

    row_props: Optional[Dict[str, Any]] = None
    col_props: Optional[Dict[str, Any]] = None
    secondary: bool = False
    colon: bool = True
    extra: Optional[str] = None
    has_feedback: bool = False
    help_text: Optional[str] = None
    hidden: bool = False
    initial_value: Optional[Any] = None
    label: Optional[str] = None
    label_align: str = "right"
    label_col: Optional[Any] = None
    name: Optional[str] = None
    no_style: bool = False
    required: bool = False
    tooltip: Optional[str] = None
    value_prop_name: Optional[str] = None
    wrapper_col: Optional[Any] = None

    column: Column = Column()
    align: str = ""
    fixed: Optional[Any] = None
    editable: bool = False
    ellipsis: bool = False
    copyable: bool = False
    filters: Optional[Any] = None
    order: int = 0
    sorter: Optional[Any] = None
    span: int = 0
    column_width: int = 0

    api: Optional[str] = None
    ignore: bool = False
    rules: List[Rule] = []
    creation_rules: List[Rule] = []
    update_rules: List[Rule] = []
    frontend_rules: List[Rule] = []
    when: WhenComponent = WhenComponent()
    when_item: List[WhenItem] = []
    show_on_index: bool = True
    show_on_detail: bool = True
    show_on_creation: bool = True
    show_on_update: bool = True
    show_on_export: bool = True
    show_on_import: bool = True
    callback: Optional[Any] = None

    allow_clear: bool = True
    auto_focus: bool = False
    bordered: bool = True
    class_name: Optional[str] = None
    default_value: Optional[Any] = None
    disabled: Optional[Any] = None
    format_str: Optional[str] = "YYYY-MM-DD HH:mm:ss"
    popup_class_name: Optional[str] = None
    input_read_only: bool = False
    locale: Optional[Any] = None
    mode: Optional[str] = None
    next_icon: Optional[Any] = None
    open_flag: bool = False
    picker: Optional[str] = None
    placeholder: Optional[str] = "请选择"
    placement: Optional[str] = None
    popup_style: Optional[Any] = None
    prev_icon: Optional[Any] = None
    size: Optional[str] = None
    status: Optional[str] = None
    style: Optional[Dict[str, Any]] = None
    suffix_icon: Optional[Any] = None
    super_next_icon: Optional[Any] = None
    super_prev_icon: Optional[Any] = None
    value: Optional[Any] = None
    default_picker_value: Optional[str] = None
    show_now: bool = False
    show_time: Optional[Any] = None
    show_today: bool = False

    @classmethod
    def new(cls):
        """
        初始化组件实例。

        Returns:
            Component: 返回初始化后的 Component 实例。
        """
        return cls().init()

    def init(self):
        """
        初始化组件属性。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.column = Column()
        self.placeholder = "请选择"
        self.format_str = "YYYY-MM-DD HH:mm:ss"
        return self

    def set_key(self, key: str, crypt: bool):
        """
        设置组件标识。

        Args:
            key (str): 要设置的标识字符串。
            crypt (bool): 是否加密。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        # 这里假设 hex.make 函数在 Python 中有对应实现，暂时用 key 替代
        self.component_key = key
        return self

    def set_style(self, style: Dict[str, Any]):
        """
        设置组件样式。

        Args:
            style (Dict[str, Any]): 要设置的样式字典。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.style = style
        return self

    def set_tooltip(self, tooltip: str):
        """
        设置 label 旁的提示信息。

        Args:
            tooltip (str): 提示信息内容。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.tooltip = tooltip
        return self

    def set_width(self, width: Any):
        """
        设置组件宽度。

        Args:
            width (Any): 要设置的宽度值。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        style = self.style.copy() if self.style else {}
        style["width"] = width
        self.style = style
        return self

    def set_row_props(self, row_props: Dict[str, Any]):
        """
        设置开启 grid 模式时传递给 Row 的属性，仅在 ProFormGroup、ProFormList、ProFormFieldSet 中有效。

        Args:
            row_props (Dict[str, Any]): 要设置的属性字典，默认：{ 'gutter': 8 }。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.row_props = row_props
        return self

    def set_col_props(self, col_props: Dict[str, Any]):
        """
        设置开启 grid 模式时传递给 Col 的属性。

        Args:
            col_props (Dict[str, Any]): 要设置的属性字典，默认：{ 'xs': 24 }。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.col_props = col_props
        return self

    def set_secondary(self, secondary: bool):
        """
        设置是否为次要控件，只针对 LightFilter 下有效。

        Args:
            secondary (bool): 是否为次要控件。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool):
        """
        设置是否显示 label 后面的冒号。

        Args:
            colon (bool): 是否显示冒号。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.colon = colon
        return self

    def set_extra(self, extra: str):
        """
        设置额外的提示信息，和 help 类似，当需要错误信息和提示文案同时出现时使用。

        Args:
            extra (str): 额外提示信息内容。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.extra = extra
        return self

    def set_has_feedback(self, has_feedback: bool):
        """
        设置是否展示校验状态图标，建议只配合 Input 组件使用。

        Args:
            has_feedback (bool): 是否展示图标。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.has_feedback = has_feedback
        return self

    def set_help_text(self, help_text: str):
        """
        设置提示信息，如不设置，则会根据校验规则自动生成。

        Args:
            help_text (str): 提示信息内容。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.help_text = help_text
        return self

    def set_no_style(self):
        """
        设置组件不带样式，作为纯字段控件使用。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.no_style = True
        return self

    def set_label(self, label: str):
        """
        设置 label 标签的文本。

        Args:
            label (str): 标签文本内容。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.label = label
        return self

    def set_label_align(self, align: str):
        """
        设置标签文本对齐方式。

        Args:
            align (str): 对齐方式字符串，取值为 'left', 'right', 'center'。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.label_align = align
        return self

    def set_label_col(self, col: Any):
        """
        设置 label 标签布局，同 <Col> 组件，设置 span offset 值。
        可通过 Form 的 label_col 进行统一设置，当和 Form 同时设置时，以 Item 为准。

        Args:
            col (Any): 布局信息，如 { 'span': 3, 'offset': 12 } 或 { 'sm': { 'span': 3, 'offset': 12 } }。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.label_col = col
        return self

    def set_name(self, name: str):
        """
        设置字段名，支持数组形式。

        Args:
            name (str): 字段名。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.name = name
        return self

    def set_name_as_label(self):
        """
        将字段名转换为 label 标签文本，只支持英文。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.label = self.name.title()
        return self

    def set_required(self):
        """
        设置字段为必填项，如不设置，则会根据校验规则自动生成。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.required = True
        return self

    def build_frontend_rules(self, path: str):
        """
        生成前端验证规则。

        Args:
            path (str): 当前路径字符串，用于判断是创建还是编辑操作。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
            rules (List[Rule]): 要设置的校验规则列表。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Rule]):
        """
        设置创建页校验规则，只在创建表单提交时生效。

        Args:
            rules (List[Rule]): 要设置的校验规则列表。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    def set_update_rules(self, rules: List[Rule]):
        """
        设置编辑页校验规则，只在更新表单提交时生效。

        Args:
            rules (List[Rule]): 要设置的校验规则列表。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        设置子节点的值的属性，如 Switch 的是 'checked'。
        该属性为 getValueProps 的封装，自定义 getValueProps 后会失效。

        Args:
            value_prop_name (str): 属性名。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.value_prop_name = value_prop_name
        return self

    def set_wrapper_col(self, col: Any):
        """
        设置输入控件的布局样式，用法同 label_col。
        可通过 Form 的 wrapper_col 进行统一设置，当和 Form 同时设置时，以 Item 为准。

        Args:
            col (Any): 布局信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.wrapper_col = col
        return self

    def set_column(self, f: Callable[[Column], Column]):
        """
        设置列表页、详情页中列属性。

        Args:
            f (Callable[[Column], Column]): 处理列属性的函数。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.column = f(self.column)
        return self

    def set_align(self, align: str):
        """
        设置列的对齐方式，取值为 'left', 'right', 'center'，只在列表页、详情页中有效。

        Args:
            align (str): 对齐方式字符串。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.align = align
        return self

    def set_fixed(self, fixed: Any):
        """
        设置列是否固定，可选 true (等效于 left)、left、right，（IE 下无效），只在列表页中有效。

        Args:
            fixed (Any): 固定状态信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool):
        """
        设置表格列是否可编辑，只在列表页中有效。

        Args:
            editable (bool): 是否可编辑。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool):
        """
        设置是否自动缩略，只在列表页、详情页中有效。

        Args:
            ellipsis (bool): 是否自动缩略。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        """
        设置是否支持复制，只在列表页、详情页中有效。

        Args:
            copyable (bool): 是否支持复制。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any):
        """
        设置表头的筛选菜单项，当值为 true 时，自动使用 valueEnum 生成，只在列表页中有效。

        Args:
            filters (Any): 筛选菜单项信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        设置查询表单中的权重，权重大排序靠前，只在列表页中有效。

        Args:
            order (int): 权重值。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.order = order
        return self

    def set_sorter(self, sorter: bool):
        """
        设置列是否可排序，只在列表页中有效。

        Args:
            sorter (bool): 是否可排序。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        """
        设置包含列的数量，只在详情页中有效。

        Args:
            span (int): 列的数量。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.span = span
        return self

    def set_column_width(self, width: int):
        """
        设置列宽，只在列表页中有效。

        Args:
            width (int): 列宽值。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.column_width = width
        return self

    def set_value(self, value: Any):
        """
        设置保存值。

        Args:
            value (Any): 要设置的值，类型为 string[] | number[]。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.value = value
        return self

    def set_default(self, value: Any):
        """
        设置默认值。

        Args:
            value (Any): 要设置的默认值。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.default_value = value
        return self

    def set_disabled(self, disabled: bool):
        """
        设置是否禁用状态，默认为 False。

        Args:
            disabled (bool): 是否禁用。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.disabled = disabled
        return self

    def set_ignore(self, ignore: bool):
        """
        设置是否忽略保存到数据库，默认为 False。

        Args:
            ignore (bool): 是否忽略。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.ignore = ignore
        return self

    def set_when(self, *value: Any):
        """
        设置 When 组件数据。

        示例:
            set_when(1, lambda: [field.Text("name", "姓名")])
            set_when(">", 1, lambda: [field.Text("name", "姓名")])

        Args:
            *value: 可变参数，根据不同数量有不同含义。
                当参数数量为 2 时，第一个参数为比较值，第二个参数为回调函数。
                当参数数量为 3 时，第一个参数为操作符，第二个参数为比较值，第三个参数为回调函数。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        w = WhenComponent()
        i = WhenItem(body=None, condition="", condition_name="", condition_operator="", option=None)
        operator = "="
        option = None

        if len(value) == 2:
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
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool):
        """
        指定元素是否在详情页隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool):
        """
        指定元素是否在创建页面隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool):
        """
        指定元素是否在编辑页面隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_update = not callback
        return self

    def hide_when_exporting(self, callback: bool):
        """
        指定元素是否在导出文件中隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_export = not callback
        return self

    def hide_when_importing(self, callback: bool):
        """
        指定元素是否在导入文件中隐藏。

        Args:
            callback (bool): 是否隐藏。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_import = not callback
        return self

    def on_index_showing(self, callback: bool):
        """
        指定元素是否在列表页显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_index = callback
        return self

    def on_detail_showing(self, callback: bool):
        """
        指定元素是否在详情页显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_detail = callback
        return self

    def show_on_creating(self, callback: bool):
        """
        指定元素是否在创建页面显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_creation = callback
        return self

    def show_on_updating(self, callback: bool):
        """
        指定元素是否在编辑页面显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_update = callback
        return self

    def show_on_exporting(self, callback: bool):
        """
        指定元素是否在导出文件中显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_export = callback
        return self

    def show_on_importing(self, callback: bool):
        """
        指定元素是否在导入文件中显示。

        Args:
            callback (bool): 是否显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_on_import = callback
        return self

    def only_on_index(self):
        """
        指定元素只在列表页显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
            Component: 返回当前 Component 实例，支持链式调用。
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
        指定元素只在表单页面显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        指定元素只在创建页面显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        指定元素只在编辑页面显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        指定元素只在导出文件中显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        指定元素只在导入文件中显示。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        指定元素在表单页面隐藏。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
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
        检查元素是否在编辑页面显示。

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
        检查元素是否在创建页面显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_creation

    def is_shown_on_export(self) -> bool:
        """
        检查元素是否在导出文件中显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_export

    def is_shown_on_import(self) -> bool:
        """
        检查元素是否在导入文件中显示。

        Returns:
            bool: 是否显示。
        """
        return self.show_on_import

    def get_value_enum(self) -> Dict[Any, Any]:
        """
        获取当前列值的枚举。

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
            Component: 返回当前 Component 实例，支持链式调用。
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
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.api = api
        return self

    def set_allow_clear(self, allow_clear: bool):
        """
        设置是否支持清除。

        Args:
            allow_clear (bool): 是否支持清除，默认 True。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.allow_clear = allow_clear
        return self

    def set_auto_focus(self, auto_focus: bool):
        """
        设置是否自动获取焦点。

        Args:
            auto_focus (bool): 是否自动获取焦点，默认 False。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.auto_focus = auto_focus
        return self

    def set_bordered(self, bordered: bool):
        """
        设置是否有边框。

        Args:
            bordered (bool): 是否有边框，默认 True。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.bordered = bordered
        return self

    def set_class_name(self, class_name: str):
        """
        设置自定义类名。

        Args:
            class_name (str): 自定义类名。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.class_name = class_name
        return self

    def set_default_value(self, default_value: Any):
        """
        设置默认的选中项。

        Args:
            default_value (Any): 默认选中项。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.default_value = default_value
        return self

    def set_format_str(self, format_str: str):
        """
        设置日期格式，为数组时支持多格式匹配，展示以第一个为准。

        Args:
            format_str (str): 日期格式字符串。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.format_str = format_str
        return self

    def set_popup_class_name(self, popup_class_name: str):
        """
        设置额外的弹出日历 className。

        Args:
            popup_class_name (str): className 字符串。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.popup_class_name = popup_class_name
        return self

    def set_input_read_only(self, input_read_only: bool):
        """
        设置输入框为只读，避免在移动设备上打开虚拟键盘。

        Args:
            input_read_only (bool): 是否只读。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.input_read_only = input_read_only
        return self

    def set_locale(self, locale: Any):
        """
        设置国际化配置。

        Args:
            locale (Any): 国际化配置信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.locale = locale
        return self

    def set_mode(self, mode: str):
        """
        设置日期面板的状态。

        Args:
            mode (str): 状态字符串，取值为 'time', 'date', 'month', 'year', 'decade'。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.mode = mode
        return self

    def set_next_icon(self, next_icon: Any):
        """
        设置自定义下一个图标。

        Args:
            next_icon (Any): 图标信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.next_icon = next_icon
        return self

    def set_open_flag(self, open_flag: bool):
        """
        控制浮层显隐。

        Args:
            open_flag (bool): 是否显示浮层。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.open_flag = open_flag
        return self

    def set_picker(self, picker: str):
        """
        设置选择器类型。

        Args:
            picker (str): 选择器类型字符串，取值为 'date', 'week', 'month', 'quarter', 'year'。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.picker = picker
        return self

    def set_placeholder(self, placeholder: str):
        """
        设置输入框占位文本。

        Args:
            placeholder (str): 占位文本。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str):
        """
        设置浮层预设位置。

        Args:
            placement (str): 预设位置字符串，取值为 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.placement = placement
        return self

    def set_popup_style(self, popup_style: Any):
        """
        设置额外的弹出日历样式。

        Args:
            popup_style (Any): 样式信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.popup_style = popup_style
        return self

    def set_prev_icon(self, prev_icon: Any):
        """
        设置自定义上一个图标。

        Args:
            prev_icon (Any): 图标信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.prev_icon = prev_icon
        return self

    def set_size(self, size: str):
        """
        设置输入框大小。

        Args:
            size (str): 大小字符串，取值为 'large', 'middle', 'small'。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.size = size
        return self

    def set_status(self, status: str):
        """
        设置校验状态。

        Args:
            status (str): 校验状态字符串，取值为 'error', 'warning'。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any):
        """
        设置自定义的选择框后缀图标。

        Args:
            suffix_icon (Any): 图标信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.suffix_icon = suffix_icon
        return self

    def set_super_next_icon(self, super_next_icon: Any):
        """
        设置自定义 << 切换图标。

        Args:
            super_next_icon (Any): 图标信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.super_next_icon = super_next_icon
        return self

    def set_super_prev_icon(self, super_prev_icon: Any):
        """
        设置自定义 >> 切换图标。

        Args:
            super_prev_icon (Any): 图标信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.super_prev_icon = super_prev_icon
        return self

    def set_default_picker_value(self, default_picker_value: str):
        """
        设置默认面板日期。

        Args:
            default_picker_value (str): 默认面板日期字符串。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.default_picker_value = default_picker_value
        return self

    def set_show_now(self, show_now: bool):
        """
        设置当设定了 show_time 的时候，面板是否显示“此刻”按钮。

        Args:
            show_now (bool): 是否显示“此刻”按钮。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_now = show_now
        return self

    def set_show_time(self, show_time: Any):
        """
        设置增加时间选择功能。

        Args:
            show_time (Any): 时间选择功能信息。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_time = show_time
        return self

    def set_show_today(self, show_today: bool):
        """
        设置是否展示“今天”按钮。

        Args:
            show_today (bool): 是否展示“今天”按钮。

        Returns:
            Component: 返回当前 Component 实例，支持链式调用。
        """
        self.show_today = show_today
        return self