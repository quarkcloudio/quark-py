import json
from typing import Any, Callable, Dict, List, Optional

from pydantic import Field, model_validator

from ...component import Component
from ...table.column import Column
from ..rule import Rule
from .when import Item, When


class Base(Component):

    row_props: Optional[Dict[str, Any]] = None
    """
    开启 grid 模式时传递给 Row, 仅在ProFormGroup, ProFormList, ProFormFieldSet 中有效，默认：{ gutter: 8 }
    """

    col_props: Optional[Dict[str, Any]] = None
    """
    开启 grid 模式时传递给 Col，默认：{ xs: 24 }
    """

    secondary: bool = False
    """
    是否是次要控件，只针对 LightFilter 下有效
    """

    colon: bool = True
    """
    配合 label 属性使用，表示是否显示 label 后面的冒号
    """

    extra: str = ""
    """
    额外的提示信息，和 help 类似，当需要错误信息和提示文案同时出现时，可以使用这个。
    """

    has_feedback: bool = False
    """
    配合 valiTextStatus 属性使用，展示校验状态图标，建议只配合 Input 组件使用
    """

    help: str = None
    """
    提示信息，如不设置，则会根据校验规则自动生成
    """

    hidden: bool = False
    """
    是否隐藏字段（依然会收集和校验字段）
    """

    initial_value: Optional[Any] = None
    """
    设置子元素默认值，如果与 Form 的 initialValues 冲突则以 Form 为准
    """

    label: str = ""
    """
    label 标签的文本
    """

    label_align: str = "right"
    """
    标签文本对齐方式
    """

    label_col: Optional[Any] = None
    """
    label 标签布局，同 <Col> 组件，设置 span offset 值，如 {span: 3, offset: 12} 或 sm: {span: 3, offset: 12}。你可以通过 Form 的 labelCol 进行统一设置，不会作用于嵌套 Item。当和 Form 同时设置时，以 Item 为准
    """

    name: str = ""
    """
    字段名，支持数组
    """

    no_style: bool = False
    """
    为 true 时不带样式，作为纯字段控件使用
    """

    required: bool = None
    """
    必填样式设置。如不设置，则会根据校验规则自动生成
    """

    tooltip: str = None
    """
    会在 label 旁增加一个 icon，悬浮后展示配置的信息
    """

    value_prop_name: str = None
    """
    子节点的值的属性，如 Switch 的是 'checked'。该属性为 getValueProps 的封装，自定义 getValueProps 后会失效
    """

    wrapper_col: Optional[Any] = None
    """
    需要为输入控件设置布局样式时，使用该属性，用法同 labelCol。你可以通过 Form 的 wrapperCol 进行统一设置，不会作用于嵌套 Item。当和 Form 同时设置时，以 Item 为准
    """

    column: Column = Field(default_factory=Column)
    """
    列表页、详情页中列属性
    """

    align: str = None
    """
    设置列的对齐方式,left | right | center，只在列表页、详情页中有效
    """

    fixed: Optional[Any] = None
    """
    （IE 下无效）列是否固定，可选 true (等效于 left) left rightr，只在列表页中有效
    """

    editable: bool = False
    """
    表格列是否可编辑，只在列表页中有效
    """

    ellipsis: bool = False
    """
    是否自动缩略，只在列表页、详情页中有效
    """

    copyable: bool = False
    """
    是否支持复制，只在列表页、详情页中有效
    """

    filters: Optional[Any] = None
    """
    表头的筛选菜单项，当值为 true 时，自动使用 valueEnum 生成，只在列表页中有效
    """

    order: int = None
    """
    查询表单中的权重，权重大排序靠前，只在列表页中有效
    """

    sorter: Optional[Any] = None
    """
    可排序列，只在列表页中有效
    """

    span: int = None
    """
    包含列的数量，只在详情页中有效
    """

    column_width: int = None
    """
    设置列宽，只在列表页中有效
    """

    api: str = ""
    """
    获取数据接口
    """

    ignore: bool = False
    """
    是否忽略保存到数据库，默认为 false
    """

    rules: List[Rule] = []
    """
    全局校验规则
    """

    creation_rules: List[Rule] = []
    """
    创建页校验规则
    """

    update_rules: List[Rule] = []
    """
    编辑页校验规则
    """

    frontend_rules: List[Rule] = []
    """
    前端校验规则，设置字段的校验逻辑
    """

    when: Optional[When] = None
    """
    When 组件
    """

    when_item: List[Item] = Field(default_factory=list)
    """
    When 组件的项
    """

    show_on_index: bool = True
    """
    在列表页展示
    """

    show_on_detail: bool = True
    """
    在详情页展示
    """

    show_on_creation: bool = True
    """
    在创建页面展示
    """

    show_on_update: bool = True
    """
    在编辑页面展示
    """

    show_on_export: bool = True
    """
    在导出的Excel上展示
    """

    show_on_import: bool = True
    """
    在导入Excel上展示
    """

    callback: Optional[Callable[[Dict[str, Any]], Any]] = Field(
        exclude=True, default=None
    )
    """
    回调函数
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式
    """

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: Dict[str, Any]):
        """设置组件的样式。"""
        self.style = style
        return self

    def set_tooltip(self, tooltip: str):
        """设置 tooltip 信息。"""
        self.tooltip = tooltip
        return self

    def set_width(self, width: Any):
        """设置组件的宽度。"""
        style = self.style.copy() if self.style else {}
        style["width"] = width
        self.style = style
        return self

    def set_row_props(self, row_props: Dict[str, Any]):
        """设置 Row 属性。"""
        self.row_props = row_props
        return self

    def set_col_props(self, col_props: Dict[str, Any]):
        """设置 Col 属性。"""
        self.col_props = col_props
        return self

    def set_secondary(self, secondary: bool):
        """设置是否为次要控件。"""
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool):
        """设置是否显示 label 后面的冒号。"""
        self.colon = colon
        return self

    def set_extra(self, extra: str):
        """设置额外的提示信息。"""
        self.extra = extra
        return self

    def set_has_feedback(self, has_feedback: bool):
        """设置是否展示校验状态图标。"""
        self.has_feedback = has_feedback
        return self

    def set_help(self, help: str):
        """设置提示信息。"""
        self.help = help
        return self

    def set_no_style(self):
        """设置为纯字段控件。"""
        self.no_style = True
        return self

    def set_label(self, label: str):
        """设置 label 标签的文本。"""
        self.label = label
        return self

    def set_label_align(self, align: str):
        """设置标签文本对齐方式。"""
        self.label_align = align
        return self

    def set_label_col(self, col: Any):
        """设置 label 标签布局。"""
        self.label_col = col
        return self

    def set_name(self, name: str):
        """设置字段名。"""
        self.name = name
        return self

    def set_name_as_label(self):
        """将字段名转换为 label。"""
        self.label = self.name.title()
        return self

    def set_required(self):
        """设置字段为必填。"""
        self.required = True
        return self

    def build_frontend_rules(self, path: str):
        rules = self.rules
        uri = path.split("/")
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        if is_creating:
            rules.extend(self.creation_rules)
        if is_editing:
            rules.extend(self.update_rules)

        self.frontend_rules = Rule.convert_to_frontend_rules(rules)
        return self

    def set_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    def set_update_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self

    def get_rules(self) -> List[Rule]:
        """获取全局验证规则。"""
        return self.rules

    def get_creation_rules(self) -> List[Rule]:
        """获取创建表单验证规则。"""
        return self.creation_rules

    def get_update_rules(self) -> List[Rule]:
        """获取更新表单验证规则。"""
        return self.update_rules

    def set_value_prop_name(self, value_prop_name: str):
        """设置子节点的值的属性。"""
        self.value_prop_name = value_prop_name
        return self

    def set_wrapper_col(self, col: Any):
        """设置输入控件的布局样式。"""
        self.wrapper_col = col
        return self

    def set_column(self, f: Callable[[Column], Column]):
        """设置列表页、详情页中列属性。"""
        self.column = f(self.column)
        return self

    def set_align(self, align: str):
        """设置列的对齐方式。"""
        self.align = align
        return self

    def set_fixed(self, fixed: Any):
        """设置列是否固定。"""
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool):
        """设置表格列是否可编辑。"""
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool):
        """设置是否自动缩略。"""
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        """设置是否支持复制。"""
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any):
        """设置表头的筛选菜单项。"""
        if isinstance(filters, dict):
            tmp_filters = [{"text": v, "value": k} for k, v in filters.items()]
            self.filters = tmp_filters
        else:
            self.filters = filters
        return self

    def set_order(self, order: int):
        """设置查询表单中的权重。"""
        self.order = order
        return self

    def set_sorter(self, sorter: bool):
        """设置可排序列。"""
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        """设置包含列的数量。"""
        self.span = span
        return self

    def set_column_width(self, width: int):
        """设置列宽。"""
        self.column_width = width
        return self

    def set_ignore(self, ignore: bool):
        """设置是否忽略保存到数据库。"""
        self.ignore = ignore
        return self

    def set_when(self, *value: Any):
        """设置 When 组件数据。"""
        w = When()
        i = Item(body=None)
        operator: str = "="
        option: Any = None

        if len(value) == 2:
            operator = "="
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

    def get_when(self) -> When:
        """获取 When 组件数据。"""
        return self.when

    def hide_from_index(self, callback: bool):
        """指定元素是否在列表页隐藏。"""
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool):
        """指定元素是否在详情页隐藏。"""
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool):
        """指定元素是否在创建页隐藏。"""
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool):
        """指定元素是否在编辑页隐藏。"""
        self.show_on_update = not callback
        return self

    def hide_when_exporting(self, callback: bool):
        """指定元素是否在导出文件中隐藏。"""
        self.show_on_export = not callback
        return self

    def hide_when_importing(self, callback: bool):
        """指定元素是否在导入文件中隐藏。"""
        self.show_on_import = not callback
        return self

    def on_index_showing(self, callback: bool):
        """指定元素是否在列表页显示。"""
        self.show_on_index = callback
        return self

    def on_detail_showing(self, callback: bool):
        """指定元素是否在详情页显示。"""
        self.show_on_detail = callback
        return self

    def show_on_creating(self, callback: bool):
        """指定元素是否在创建页显示。"""
        self.show_on_creation = callback
        return self

    def show_on_updating(self, callback: bool):
        """指定元素是否在编辑页显示。"""
        self.show_on_update = callback
        return self

    def show_on_exporting(self, callback: bool):
        """指定元素是否在导出文件中显示。"""
        self.show_on_export = callback
        return self

    def show_on_importing(self, callback: bool):
        """指定元素是否在导入文件中显示。"""
        self.show_on_import = callback
        return self

    def only_on_index(self):
        """指定元素只在列表页显示。"""
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_detail(self):
        """指定元素只在详情页显示。"""
        self.show_on_index = False
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_forms(self):
        """指定元素只在表单页显示。"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_creating(self):
        """指定元素只在创建页显示。"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_updating(self):
        """指定元素只在编辑页显示。"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_export(self):
        """指定元素只在导出文件中显示。"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = False
        return self

    def only_on_import(self):
        """指定元素只在导入文件中显示。"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = True
        return self

    def except_on_forms(self):
        """指定元素在表单页隐藏。"""
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = True
        return self

    def is_shown_on_update(self) -> bool:
        """检查元素是否在编辑页显示。"""
        return self.show_on_update

    def is_shown_on_index(self) -> bool:
        """检查元素是否在列表页显示。"""
        return self.show_on_index

    def is_shown_on_detail(self) -> bool:
        """检查元素是否在详情页显示。"""
        return self.show_on_detail

    def is_shown_on_creation(self) -> bool:
        """检查元素是否在创建页显示。"""
        return self.show_on_creation

    def is_shown_on_export(self) -> bool:
        """检查元素是否在导出文件中显示。"""
        return self.show_on_export

    def is_shown_on_import(self) -> bool:
        """检查元素是否在导入文件中显示。"""
        return self.show_on_import

    def get_value_enum(self) -> Dict[Any, Any]:
        """获取当前列值的枚举。"""
        data: Dict[Any, Any] = {}
        return data

    def set_callback(self, closure: Optional[Callable[[Dict[str, Any]], Any]]):
        """设置回调函数。"""
        if closure:
            self.callback = closure
        return self

    def get_callback(self) -> Optional[Callable[[Dict[str, Any]], Any]]:
        """获取回调函数。"""
        return self.callback

    def set_api(self, api: str):
        """设置获取数据接口。"""
        self.api = api
        return self
