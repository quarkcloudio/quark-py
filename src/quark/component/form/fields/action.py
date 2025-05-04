from typing import Optional, List, Dict, Any, Union, Callable, TypeVar
from pydantic import BaseModel, Field
from enum import Enum

# 主组件类
class ActionField(BaseModel):
    component_key: str = Field("", description="组件标识")
    component: str = Field("actionField", description="组件名称")

    # 表单布局相关
    row_props: Optional[Dict[str, Any]] = Field({"gutter": 8}, description="开启 grid 模式时传递给 Row，默认：{ gutter: 8 }")
    col_props: Optional[Dict[str, Any]] = Field({"xs": 24}, description="开启 grid 模式时传递给 Col，默认：{ xs: 24 }")
    secondary: bool = Field(False, description="是否是次要控件，只针对 LightFilter 下有效")
    colon: bool = Field(True, description="配合 label 属性使用，表示是否显示 label 后面的冒号")
    extra: str = Field("", description="额外的提示信息，和 help 类似")
    has_feedback: bool = Field(False, description="展示校验状态图标，建议只配合 Input 组件使用")
    help: str = Field("", description="提示信息")
    hidden: bool = Field(False, description="是否隐藏字段（依然会收集和校验字段）")
    initial_value: Optional[Any] = Field(None, description="设置子元素默认值")
    label: str = Field("", description="label 标签的文本")
    label_align: str = Field("right", description="标签文本对齐方式")
    label_col: Optional[Any] = Field(None, description="label 标签布局，同 <Col> 组件")
    name: str = Field("", description="字段名，支持数组")
    no_style: bool = Field(False, description="为 true 时不带样式，作为纯字段控件使用")
    required: bool = Field(False, description="必填样式设置。如不设置，则会根据校验规则自动生成")
    tooltip: str = Field("", description="会在 label 旁增加一个 icon")
    value_prop_name: str = Field("", description="子节点的值的属性，如 Switch 的是 'checked'")
    wrapper_col: Optional[Any] = Field(None, description="需要为输入控件设置布局样式时使用")

    # 列表页、详情页中列属性
    column: Optional[Table.Column] = Field(Table.Column().init(), description="列表页、详情页中列属性")
    align: str = Field("", description="设置列的对齐方式")
    fixed: Optional[Any] = Field(None, description="列是否固定")
    editable: bool = Field(False, description="表格列是否可编辑")
    ellipsis: bool = Field(False, description="是否自动缩略")
    copyable: bool = Field(False, description="是否支持复制")
    filters: Optional[Any] = Field(None, description="表头的筛选菜单项")
    order: int = Field(0, description="查询表单中的权重")
    sorter: Optional[Any] = Field(None, description="可排序列")
    span: int = Field(0, description="包含列的数量")
    column_width: int = Field(0, description="设置列宽")

    # 接口与校验
    api: str = Field("", description="获取数据接口")
    ignore: bool = Field(False, description="是否忽略保存到数据库")
    rules: List[Rule] = Field([], description="全局校验规则")
    creation_rules: List[Rule] = Field([], description="创建页校验规则")
    update_rules: List[Rule] = Field([], description="编辑页校验规则")
    frontend_rules: List[Rule] = Field([], description="前端校验规则")
    when: Optional[When.Component] = Field(When.Component(), description="条件渲染组件")
    when_item: List[When.Item] = Field([], description="条件渲染条目")
    show_on_index: bool = Field(True, description="在列表页展示")
    show_on_detail: bool = Field(True, description="在详情页展示")
    show_on_creation: bool = Field(False, description="在创建页面展示")
    show_on_update: bool = Field(False, description="在编辑页面展示")
    show_on_export: bool = Field(False, description="在导出Excel上展示")
    show_on_import: bool = Field(False, description="在导入Excel上展示")
    callback: Optional[Callable[[Dict[str, Any]], Any]] = Field(None, description="回调函数")

    items: Optional[Any] = Field(None, description="具体行为项")
    style: Optional[Dict[str, Any]] = Field({}, description="自定义样式")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init()

    def init(self) -> "ActionField":
        """初始化"""
        self.component = "actionField"
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        self.column = Table.Column().init()
        self.set_key(DEFAULT_KEY, DEFAULT_CRYPT)
        return self

    def set_key(self, key: str, crypt: bool) -> "ActionField":
        """设置 Key"""
        self.component_key = f"encrypted_{key}" if crypt else key
        return self

    def set_style(self, style: dict) -> "ActionField":
        """设置样式"""
        self.style = style
        return self

    def set_tooltip(self, tooltip: str) -> "ActionField":
        """设置 Tooltip 提示"""
        self.tooltip = tooltip
        return self

    def set_width(self, width: Any) -> "ActionField":
        """设置宽度"""
        self.style["width"] = width
        return self

    def set_label(self, label: str) -> "ActionField":
        """设置 Label 文本"""
        self.label = label
        return self

    def set_name(self, name: str) -> "ActionField":
        """设置字段名"""
        self.name = name
        return self

    def set_required(self) -> "ActionField":
        """标记为必填"""
        self.required = True
        return self

    def set_when(self, *args) -> "ActionField":
        """设置 When 条件渲染"""
        w = When.Component()
        i = When.Item()

        if len(args) == 2:
            operator = "="
            option = args[0]
            callback = args[1]
            i.body = callback()
        elif len(args) == 3:
            operator = args[0]
            option = args[1]
            callback = args[2]
            i.body = callback()
        else:
            raise ValueError("SetWhen requires 2 or 3 arguments.")

        option_str = str(option)
        if operator == "!=":
            i.condition = f"<%=String({self.name}) !== '{option_str}' %>"
        elif operator == "=":
            i.condition = f"<%=String({self.name}) === '{option_str}' %>"
        elif operator == ">":
            i.condition = f"<%=String({self.name}) > '{option_str}' %>"
        elif operator == "<":
            i.condition = f"<%=String({self.name}) < '{option_str}' %>"
        elif operator == "<=":
            i.condition = f"<%=String({self.name}) <= '{option_str}' %>"
        elif operator == ">=":
            i.condition = f"<%=String({self.name}) => '{option_str}' %>"
        elif operator == "has":
            i.condition = f"<%=(String({self.name}).indexOf('{option_str}') != -1) %>"
        elif operator == "in":
            import json
            json_str = json.dumps(option)
            i.condition = f"<%=({json_str}.indexOf({self.name}) != -1) %>"
        else:
            i.condition = f"<%=String({self.name}) === '{option_str}' %>"

        i.condition_name = self.name
        i.condition_operator = operator
        i.option = option
        self.when_item.append(i)
        self.when = w.set_items(self.when_item)
        return self

    def only_on_index(self) -> "ActionField":
        """仅在列表页展示"""
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_forms(self) -> "ActionField":
        """仅在表单页展示"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_creating(self) -> "ActionField":
        """仅在创建页展示"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_updating(self) -> "ActionField":
        """仅在更新页展示"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def build_frontend_rules(self, path: str) -> "ActionField":
        """生成前端验证规则"""
        uri = path.split("/")
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        frontend_rules = []
        if self.rules:
            frontend_rules.extend(self.rules)
        if is_creating and self.creation_rules:
            frontend_rules.extend(self.creation_rules)
        if is_editing and self.update_rules:
            frontend_rules.extend(self.update_rules)

        self.frontend_rules = frontend_rules
        return self

    def set_rules(self, rules: List[Rule]) -> "ActionField":
        """设置全局校验规则"""
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Rule]) -> "ActionField":
        """设置创建页校验规则"""
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    def set_update_rules(self, rules: List[Rule]) -> "ActionField":
        """设置更新页校验规则"""
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self

    def set_callback(self, closure: Callable[[Dict[str, Any]], Any]) -> "ActionField":
        """设置回调函数"""
        self.callback = closure
        return self

    def set_items(self, items: list) -> "ActionField":
        """设置行为项"""
        self.items = items
        return self