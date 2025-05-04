from pydantic import BaseModel, Field
from typing import Dict, List, Any, Callable, Optional
import json
import re

# 模拟 rule 模块
class Rule(BaseModel):
    name: str = ""

    @staticmethod
    def Required(required: bool, message: str):
        return Rule()

    @staticmethod
    def Min(min_value: int, message: str):
        return Rule()

    @staticmethod
    def Max(max_value: int, message: str):
        return Rule()

    @staticmethod
    def Unique(table: str, field: str, id_value: Any, message: str):
        return Rule()

# 模拟 when 模块
class WhenItem(BaseModel):
    body: Any = None
    condition: str = ""
    condition_name: str = ""
    condition_operator: str = ""
    option: Any = None

class WhenComponent(BaseModel):
    items: List[WhenItem] = []

    def set_items(self, items: List[WhenItem]):
        self.items = items
        return self

def new_when():
    return WhenComponent()

def new_when_item():
    return WhenItem()

# 模拟 table 模块
class TableColumn(BaseModel):
    def init(self):
        return self

class Component(BaseModel):
    """
    表单字段组件模型，用于定义表单字段的各种属性和行为。
    """
    component_key: str = Field("", alias="componentkey", description="组件标识")
    component: str = Field("", alias="component", description="组件名称")
    row_props: Optional[Dict[str, Any]] = Field(None, alias="rowProps", description="开启 grid 模式时传递给 Row, 仅在ProFormGroup, ProFormList, ProFormFieldSet 中有效，默认：{ gutter: 8 }")
    col_props: Optional[Dict[str, Any]] = Field(None, alias="colProps", description="开启 grid 模式时传递给 Col，默认：{ xs: 24 }")
    secondary: bool = Field(False, alias="secondary", description="是否是次要控件，只针对 LightFilter 下有效")
    colon: bool = Field(True, alias="colon", description="配合 label 属性使用，表示是否显示 label 后面的冒号")
    extra: str = Field("", alias="extra", description="额外的提示信息，和 help 类似，当需要错误信息和提示文案同时出现时，可以使用这个。")
    has_feedback: bool = Field(False, alias="hasFeedback", description="配合 validateStatus 属性使用，展示校验状态图标，建议只配合 Input 组件使用")
    help: str = Field("", alias="help", description="提示信息，如不设置，则会根据校验规则自动生成")
    hidden: bool = Field(False, alias="hidden", description="是否隐藏字段（依然会收集和校验字段）")
    initial_value: Optional[Any] = Field(None, alias="initialValue", description="设置子元素默认值，如果与 Form 的 initialValues 冲突则以 Form 为准")
    label: str = Field("", alias="label", description="label 标签的文本")
    label_align: str = Field("right", alias="labelAlign", description="标签文本对齐方式")
    label_col: Optional[Any] = Field(None, alias="labelCol", description="label 标签布局，同 <Col> 组件，设置 span offset 值，如 {span: 3, offset: 12} 或 sm: {span: 3, offset: 12}。你可以通过 Form 的 labelCol 进行统一设置，不会作用于嵌套 Item。当和 Form 同时设置时，以 Item 为准")
    name: str = Field("", alias="name", description="字段名，支持数组")
    no_style: bool = Field(False, alias="noStyle", description="为 true 时不带样式，作为纯字段控件使用")
    required: bool = Field(False, alias="required", description="必填样式设置。如不设置，则会根据校验规则自动生成")
    tooltip: str = Field("", alias="tooltip", description="会在 label 旁增加一个 icon，悬浮后展示配置的信息")
    value_prop_name: str = Field("", alias="valuePropName", description="子节点的值的属性，如 Switch 的是 'checked'。该属性为 getValueProps 的封装，自定义 getValueProps 后会失效")
    wrapper_col: Optional[Any] = Field(None, alias="wrapperCol", description="需要为输入控件设置布局样式时，使用该属性，用法同 labelCol。你可以通过 Form 的 wrapperCol 进行统一设置，不会作用于嵌套 Item。当和 Form 同时设置时，以 Item 为准")
    column: TableColumn = Field(TableColumn().init(), alias="Column", description="列表页、详情页中列属性")
    align: str = Field("", alias="Align", description="设置列的对齐方式,left | right | center，只在列表页、详情页中有效")
    fixed: Optional[Any] = Field(None, alias="Fixed", description="（IE 下无效）列是否固定，可选 true (等效于 left) left rightr，只在列表页中有效")
    editable: bool = Field(False, alias="Editable", description="表格列是否可编辑，只在列表页中有效")
    ellipsis: bool = Field(False, alias="Ellipsis", description="是否自动缩略，只在列表页、详情页中有效")
    copyable: bool = Field(False, alias="Copyable", description="是否支持复制，只在列表页、详情页中有效")
    filters: Optional[Any] = Field(None, alias="Filters", description="表头的筛选菜单项，当值为 true 时，自动使用 valueEnum 生成，只在列表页中有效")
    order: int = Field(0, alias="Order", description="查询表单中的权重，权重大排序靠前，只在列表页中有效")
    sorter: Optional[Any] = Field(None, alias="Sorter", description="可排序列，只在列表页中有效")
    span: int = Field(0, alias="Span", description="包含列的数量，只在详情页中有效")
    column_width: int = Field(0, alias="ColumnWidth", description="设置列宽，只在列表页中有效")
    api: str = Field("", alias="api", description="获取数据接口")
    ignore: bool = Field(False, alias="ignore", description="是否忽略保存到数据库，默认为 false")
    rules: List[Rule] = Field([], alias="Rules", description="全局校验规则")
    creation_rules: List[Rule] = Field([], alias="CreationRules", description="创建页校验规则")
    update_rules: List[Rule] = Field([], alias="UpdateRules", description="编辑页校验规则")
    frontend_rules: List[Rule] = Field([], alias="frontendRules", description="前端校验规则，设置字段的校验逻辑")
    when: Optional[WhenComponent] = Field(None, alias="when")
    when_item: List[WhenItem] = Field([], alias="WhenItem")
    show_on_index: bool = Field(False, alias="ShowOnIndex", description="在列表页展示")
    show_on_detail: bool = Field(False, alias="ShowOnDetail", description="在详情页展示")
    show_on_creation: bool = Field(True, alias="ShowOnCreation", description="在创建页面展示")
    show_on_update: bool = Field(True, alias="ShowOnUpdate", description="在编辑页面展示")
    show_on_export: bool = Field(False, alias="ShowOnExport", description="在导出的Excel上展示")
    show_on_import: bool = Field(False, alias="ShowOnImport", description="在导入Excel上展示")
    callback: Optional[Callable[[Dict[str, Any]], Any]] = Field(None, alias="Callback", description="回调函数")
    block: bool = Field(False, alias="block", description="将宽度调整为父元素宽度的选项,默认值false")
    direction: str = Field("", alias="direction", description="间距方向")
    size: str = Field("", alias="size", description="间距大小")
    body: Optional[Any] = Field(None, alias="body", description="组件内容")

    @classmethod
    def new(cls):
        """
        初始化组件，创建一个新的 Component 实例并调用 init 方法进行初始化。
        """
        return cls().init()

    def init(self):
        """
        初始化组件属性。
        """
        self.component = "compactField"
        self.colon = True
        self.label_align = "right"
        self.column = TableColumn().init()
        self.only_on_forms()
        # 这里无法实现 hex.Make，需要自定义实现
        # self.set_key(component.DEFAULT_KEY, component.DEFAULT_CRYPT)
        return self

    def set_key(self, key: str, crypt: bool):
        """
        设置组件的 key。
        :param key: 要设置的 key 值
        :param crypt: 是否加密
        :return: 当前组件实例
        """
        # 这里无法实现 hex.Make，需要自定义实现
        self.component_key = key
        return self

    def set_tooltip(self, tooltip: str):
        """
        设置 label 旁的提示信息。
        :param tooltip: 提示信息内容
        :return: 当前组件实例
        """
        self.tooltip = tooltip
        return self

    def set_row_props(self, row_props: Dict[str, Any]):
        """
        设置开启 grid 模式时传递给 Row 的属性。
        :param row_props: Row 的属性字典
        :return: 当前组件实例
        """
        self.row_props = row_props
        return self

    def set_col_props(self, col_props: Dict[str, Any]):
        """
        设置开启 grid 模式时传递给 Col 的属性。
        :param col_props: Col 的属性字典
        :return: 当前组件实例
        """
        self.col_props = col_props
        return self

    def set_secondary(self, secondary: bool):
        """
        设置是否为次要控件。
        :param secondary: 是否为次要控件的布尔值
        :return: 当前组件实例
        """
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool):
        """
        设置是否显示 label 后面的冒号。
        :param colon: 是否显示冒号的布尔值
        :return: 当前组件实例
        """
        self.colon = colon
        return self

    def set_extra(self, extra: str):
        """
        设置额外的提示信息。
        :param extra: 额外提示信息内容
        :return: 当前组件实例
        """
        self.extra = extra
        return self

    def set_has_feedback(self, has_feedback: bool):
        """
        设置是否展示校验状态图标。
        :param has_feedback: 是否展示图标的布尔值
        :return: 当前组件实例
        """
        self.has_feedback = has_feedback
        return self

    def set_help(self, help_text: str):
        """
        设置提示信息。
        :param help_text: 提示信息内容
        :return: 当前组件实例
        """
        self.help = help_text
        return self

    def set_no_style(self):
        """
        设置为不带样式的纯字段控件。
        :return: 当前组件实例
        """
        self.no_style = True
        return self

    def set_label(self, label: str):
        """
        设置 label 标签的文本。
        :param label: label 文本内容
        :return: 当前组件实例
        """
        self.label = label
        return self

    def set_label_align(self, align: str):
        """
        设置标签文本的对齐方式。
        :param align: 对齐方式字符串
        :return: 当前组件实例
        """
        self.label_align = align
        return self

    def set_label_col(self, col: Any):
        """
        设置 label 标签的布局。
        :param col: 布局设置
        :return: 当前组件实例
        """
        self.label_col = col
        return self

    def set_name(self, name: str):
        """
        设置字段名。
        :param name: 字段名
        :return: 当前组件实例
        """
        self.name = name
        return self

    def set_name_as_label(self):
        """
        将字段名转换为 label 文本。
        :return: 当前组件实例
        """
        self.label = self.name.title()
        return self

    def set_required(self):
        """
        设置字段为必填项。
        :return: 当前组件实例
        """
        self.required = True
        return self

    def build_frontend_rules(self, path: str):
        """
        生成前端验证规则。
        :param path: 当前路径
        :return: 当前组件实例
        """
        uri = re.split(r'/', path)
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        rules = []
        creation_rules = []
        update_rules = []

        if self.rules:
            # 这里无法实现 rule.ConvertToFrontendRules，需要自定义实现
            rules = self.rules
        if is_creating and self.creation_rules:
            # 这里无法实现 rule.ConvertToFrontendRules，需要自定义实现
            creation_rules = self.creation_rules
        if is_editing and self.update_rules:
            # 这里无法实现 rule.ConvertToFrontendRules，需要自定义实现
            update_rules = self.update_rules

        frontend_rules = []
        frontend_rules.extend(rules)
        frontend_rules.extend(creation_rules)
        frontend_rules.extend(update_rules)

        self.frontend_rules = frontend_rules
        return self

    def set_rules(self, rules: List[Rule]):
        """
        设置全局校验规则。
        :param rules: 校验规则列表
        :return: 当前组件实例
        """
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Rule]):
        """
        设置创建页校验规则。
        :param rules: 校验规则列表
        :return: 当前组件实例
        """
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    def set_update_rules(self, rules: List[Rule]):
        """
        设置编辑页校验规则。
        :param rules: 校验规则列表
        :return: 当前组件实例
        """
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self

    def get_rules(self):
        """
        获取全局校验规则。
        :return: 全局校验规则列表
        """
        return self.rules

    def get_creation_rules(self):
        """
        获取创建页校验规则。
        :return: 创建页校验规则列表
        """
        return self.creation_rules

    def get_update_rules(self):
        """
        获取编辑页校验规则。
        :return: 编辑页校验规则列表
        """
        return self.update_rules

    def set_value_prop_name(self, value_prop_name: str):
        """
        设置子节点的值的属性。
        :param value_prop_name: 属性名
        :return: 当前组件实例
        """
        self.value_prop_name = value_prop_name
        return self

    def set_wrapper_col(self, col: Any):
        """
        设置输入控件的布局样式。
        :param col: 布局设置
        :return: 当前组件实例
        """
        self.wrapper_col = col
        return self

    def set_column(self, f: Callable[[TableColumn], TableColumn]):
        """
        设置列表页、详情页中列属性。
        :param f: 处理列属性的函数
        :return: 当前组件实例
        """
        self.column = f(self.column)
        return self

    def set_align(self, align: str):
        """
        设置列的对齐方式。
        :param align: 对齐方式字符串
        :return: 当前组件实例
        """
        self.align = align
        return self

    def set_fixed(self, fixed: Any):
        """
        设置列是否固定。
        :param fixed: 固定设置
        :return: 当前组件实例
        """
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool):
        """
        设置表格列是否可编辑。
        :param editable: 是否可编辑的布尔值
        :return: 当前组件实例
        """
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool):
        """
        设置是否自动缩略。
        :param ellipsis: 是否自动缩略的布尔值
        :return: 当前组件实例
        """
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        """
        设置是否支持复制。
        :param copyable: 是否支持复制的布尔值
        :return: 当前组件实例
        """
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any):
        """
        设置表头的筛选菜单项。
        :param filters: 筛选菜单项设置
        :return: 当前组件实例
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
        :param order: 权重值
        :return: 当前组件实例
        """
        self.order = order
        return self

    def set_sorter(self, sorter: bool):
        """
        设置是否为可排序列。
        :param sorter: 是否可排序的布尔值
        :return: 当前组件实例
        """
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        """
        设置包含列的数量。
        :param span: 列数量
        :return: 当前组件实例
        """
        self.span = span
        return self

    def set_column_width(self, width: int):
        """
        设置列宽。
        :param width: 列宽值
        :return: 当前组件实例
        """
        self.column_width = width
        return self

    def set_ignore(self, ignore: bool):
        """
        设置是否忽略保存到数据库。
        :param ignore: 是否忽略的布尔值
        :return: 当前组件实例
        """
        self.ignore = ignore
        return self

    def set_when(self, *value):
        """
        设置 When 组件数据。
        :param value: 可变参数，根据不同情况设置条件和回调
        :return: 当前组件实例
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
                i.condition = f"<%=String({self.name}) => '{get_option}' %>"
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

    def get_when(self):
        """
        获取 When 组件数据。
        :return: When 组件实例
        """
        return self.when

    def hide_from_index(self, callback: bool):
        """
        指定元素是否在列表页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前组件实例
        """
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool):
        """
        指定元素是否在详情页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前组件实例
        """
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool):
        """
        指定元素是否在创建页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前组件实例
        """
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool):
        """
        指定元素是否在编辑页隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前组件实例
        """
        self.show_on_update = not callback
        return self

    def hide_when_exporting(self, callback: bool):
        """
        指定元素是否在导出文件时隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前组件实例
        """
        self.show_on_export = not callback
        return self

    def hide_when_importing(self, callback: bool):
        """
        指定元素是否在导入文件时隐藏。
        :param callback: 是否隐藏的布尔值
        :return: 当前组件实例
        """
        self.show_on_import = not callback
        return self

    def on_index_showing(self, callback: bool):
        """
        指定元素是否在列表页显示。
        :param callback: 是否显示的布尔值
        :return: 当前组件实例
        """
        self.show_on_index = callback
        return self

    def on_detail_showing(self, callback: bool):
        """
        指定元素是否在详情页显示。
        :param callback: 是否显示的布尔值
        :return: 当前组件实例
        """
        self.show_on_detail = callback
        return self

    def show_on_creating(self, callback: bool):
        """
        指定元素是否在创建页显示。
        :param callback: 是否显示的布尔值
        :return: 当前组件实例
        """
        self.show_on_creation = callback
        return self

    def show_on_updating(self, callback: bool):
        """
        指定元素是否在编辑页显示。
        :param callback: 是否显示的布尔值
        :return: 当前组件实例
        """
        self.show_on_update = callback
        return self

    def show_on_exporting(self, callback: bool):
        """
        指定元素是否在导出文件时显示。
        :param callback: 是否显示的布尔值
        :return: 当前组件实例
        """
        self.show_on_export = callback
        return self

    def show_on_importing(self, callback: bool):
        """
        指定元素是否在导入文件时显示。
        :param callback: 是否显示的布尔值
        :return: 当前组件实例
        """
        self.show_on_import = callback
        return self

    def only_on_index(self):
        """
        指定元素只在列表页显示。
        :return: 当前组件实例
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
        :return: 当前组件实例
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
        :return: 当前组件实例
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
        :return: 当前组件实例
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
        :return: 当前组件实例
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
        指定元素只在导出文件时显示。
        :return: 当前组件实例
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
        指定元素只在导入文件时显示。
        :return: 当前组件实例
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
        :return: 当前组件实例
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
        获取当前列值的枚举。
        :return: 枚举字典
        """
        return {}

    def set_callback(self, closure: Callable[[Dict[str, Any]], Any]):
        """
        设置回调函数。
        :param closure: 回调函数
        :return: 当前组件实例
        """
        if closure is not None:
            self.callback = closure
        return self

    def get_callback(self):
        """
        获取回调函数。
        :return: 回调函数
        """
        return self.callback

    def set_api(self, api: str):
        """
        设置获取数据接口。
        :param api: 接口地址
        :return: 当前组件实例
        """
        self.api = api
        return self

    def set_block(self, block: bool):
        """
        设置是否将宽度调整为父元素宽度。
        :param block: 是否调整的布尔值
        :return: 当前组件实例
        """
        self.block = block
        return self

    def set_direction(self, direction: str):
        """
        设置间距方向。
        :param direction: 间距方向字符串
        :return: 当前组件实例
        """
        self.direction = direction
        return self

    def set_size(self, size: str):
        """
        设置间距大小。
        :param size: 间距大小字符串
        :return: 当前组件实例
        """
        self.size = size
        return self

    def set_body(self, body: Any):
        """
        设置容器控件里面的内容。
        :param body: 组件内容
        :return: 当前组件实例
        """
        self.body = body
        return self