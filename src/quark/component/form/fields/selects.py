"""
此模块定义了 Selects 组件，用于创建多选选择框组件。
使用 pydantic 进行数据验证和序列化，支持多种配置选项和方法。
"""
import json
from typing import Dict, List, Optional, Any, Callable, Union
from pydantic import BaseModel

# 模拟依赖的模块和类
class TableColumn:
    """模拟表格列对象，用于列表和详情页列属性配置。"""
    def __init__(self):
        self.init()

    def init(self):
        """初始化列对象。"""
        return self


class Rule(BaseModel):
    """模拟验证规则对象，用于字段验证逻辑。"""
    name: Optional[str] = None


class WhenComponent(BaseModel):
    """模拟 When 组件对象，用于条件显示逻辑。"""
    items: List[Any] = []

    def set_items(self, items: List[Any]):
        """
        设置 When 组件的条件项列表。

        Args:
            items (List[Any]): 条件项列表。

        Returns:
            WhenComponent: 返回当前实例，支持链式调用。
        """
        self.items = items
        return self


class WhenItem(BaseModel):
    """模拟 When 组件的条件项对象，定义条件项属性。"""
    body: Any = None
    condition: str = ""
    condition_name: str = ""
    condition_operator: str = ""
    option: Any = None


class Component(BaseModel):
    """
    表示多选选择框组件的类，使用 pydantic 进行数据验证和序列化。

    Attributes:
        component_key (str): 组件标识。
        component (str): 组件名称，默认为 "selects"。
        row_props (Optional[Dict[str, Any]]): 开启 grid 模式时传递给 Row 的属性，
            仅在 ProFormGroup、ProFormList、ProFormFieldSet 中有效，默认值为 None。
        col_props (Optional[Dict[str, Any]]): 开启 grid 模式时传递给 Col 的属性，默认值为 None。
        secondary (bool): 是否是次要控件，只针对 LightFilter 下有效，默认值为 False。
        colon (bool): 配合 label 属性使用，表示是否显示 label 后面的冒号，默认值为 True。
        extra (Optional[str]): 额外的提示信息，和 help 类似，
            当需要错误信息和提示文案同时出现时使用，默认值为 None。
        has_feedback (bool): 配合 validateStatus 属性使用，展示校验状态图标，
            建议只配合 Input 组件使用，默认值为 False。
        help (Optional[str]): 提示信息，如不设置，则会根据校验规则自动生成，默认值为 None。
        hidden (bool): 是否隐藏字段（依然会收集和校验字段），默认值为 False。
        initial_value (Optional[Any]): 设置子元素默认值，如果与 Form 的 initialValues 冲突则以 Form 为准，默认值为 None。
        label (Optional[str]): label 标签的文本，默认值为 None。
        label_align (str): 标签文本对齐方式，默认为 "right"。
        label_col (Optional[Any]): label 标签布局，同 <Col> 组件，设置 span offset 值，
            可以通过 Form 的 labelCol 进行统一设置，默认值为 None。
        name (Optional[str]): 字段名，支持数组，默认值为 None。
        no_style (bool): 为 True 时不带样式，作为纯字段控件使用，默认值为 False。
        required (bool): 必填样式设置。如不设置，则会根据校验规则自动生成，默认值为 False。
        tooltip (Optional[str]): 会在 label 旁增加一个 icon，悬浮后展示配置的信息，默认值为 None。
        value_prop_name (Optional[str]): 子节点的值的属性，如 Switch 的是 'checked'，默认值为 None。
        wrapper_col (Optional[Any]): 需要为输入控件设置布局样式时使用，用法同 labelCol，默认值为 None。

        column (TableColumn): 列表页、详情页中列属性。
        align (str): 设置列的对齐方式,left | right | center，只在列表页、详情页中有效。
        fixed (Optional[Any]): （IE 下无效）列是否固定，可选 true (等效于 left) left rightr，只在列表页中有效。
        editable (bool): 表格列是否可编辑，只在列表页中有效，默认值为 False。
        ellipsis (bool): 是否自动缩略，只在列表页、详情页中有效，默认值为 False。
        copyable (bool): 是否支持复制，只在列表页、详情页中有效，默认值为 False。
        filters (Optional[Any]): 表头的筛选菜单项，当值为 true 时，自动使用 valueEnum 生成，只在列表页中有效。
        order (int): 查询表单中的权重，权重大排序靠前，只在列表页中有效，默认值为 0。
        sorter (Optional[Any]): 可排序列，只在列表页中有效。
        span (int): 包含列的数量，只在详情页中有效，默认值为 0。
        column_width (int): 设置列宽，只在列表页中有效，默认值为 0。

        api (Optional[str]): 获取数据接口。
        ignore (bool): 是否忽略保存到数据库，默认为 False。
        rules (List[Rule]): 全局校验规则。
        creation_rules (List[Rule]): 创建页校验规则。
        update_rules (List[Rule]): 编辑页校验规则。
        frontend_rules (List[Rule]): 前端校验规则，设置字段的校验逻辑。
        when (WhenComponent): When 组件。
        when_item (List[WhenItem]): When 组件条件项列表。
        show_on_index (bool): 在列表页展示，默认值为 True。
        show_on_detail (bool): 在详情页展示，默认值为 True。
        show_on_creation (bool): 在创建页面展示，默认值为 True。
        show_on_update (bool): 在编辑页面展示，默认值为 True。
        show_on_export (bool): 在导出的 Excel 上展示，默认值为 True。
        show_on_import (bool): 在导入 Excel 上展示，默认值为 True。
        callback (Optional[Any]): 回调函数。

        body (Any): 组件内容。
    """
    component_key: str = ""
    component: str = "selects"

    row_props: Optional[Dict[str, Any]] = None
    col_props: Optional[Dict[str, Any]] = None
    secondary: bool = False
    colon: bool = True
    extra: Optional[str] = None
    has_feedback: bool = False
    help: Optional[str] = None
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

    column: TableColumn = TableColumn()
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

    body: Any

    class Config:
        """pydantic 配置类，允许使用别名。"""
        arbitrary_types_allowed = True

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
        self.component = "selects"
        self.colon = True
        self.label_align = "right"
        self.column = TableColumn().init()
        self.only_on_forms()
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
            self.label = self.name.title()
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
        获取当前列值的枚举 valueEnum。

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

    def set_body(self, body: Any):
        """
        设置组件内容。

        Args:
            body (Any): 组件内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.body = body
        return self