from typing import Any, List, Optional, Dict, Union, Callable
from pydantic import BaseModel, Field
from enum import Enum
from ...component import Component

class LabelValueChild(BaseModel):
    """
    定义级联选择字段中 label、value 和 children 字段名的映射。
    """

    label: str = Field(..., description="选项显示文本的字段名")
    value: str = Field(..., description="选项值的字段名")
    children: str = Field(..., description="子节点列表字段名")


class CascaderOption(BaseModel):
    """
    级联选择器中的一个选项。
    """

    label: Optional[str] = Field(None, description="显示的标签文本")
    value: Any = Field(..., description="选项的实际值")
    disabled: bool = Field(False, description="是否禁用该选项")
    children: List["CascaderOption"] = Field([], description="子选项列表")
    is_leaf: bool = Field(False, description="标记是否为叶子节点，设置了 `loadData` 时有效")


class WhenItem(BaseModel):
    """
    When 组件的条件项，用于控制级联显示逻辑。
    """

    condition: str = Field(..., description="条件表达式字符串")
    body: List[Any] = Field([], description="满足条件时要渲染的内容")
    condition_name: str = Field("", description="关联字段名称")
    condition_operator: str = Field("", description="条件操作符")
    option: Any = Field(None, description="条件比较值")


class WhenComponent(BaseModel):
    """
    When 组件，包含多个条件项。
    """

    items: List[WhenItem] = Field([], description="条件项列表")

    def set_items(self, items: List[WhenItem]) -> "WhenComponent":
        self.items = items
        return self


class TableColAlign(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"


class TableColumn(BaseModel):
    """
    表格列配置，适用于列表页和详情页。
    """

    align: Optional[TableColAlign] = Field(None, description="列对齐方式")
    fixed: Optional[Union[bool, str]] = Field(None, description="列是否固定")
    editable: bool = Field(False, description="表格列是否可编辑")
    ellipsis: bool = Field(False, description="是否自动缩略")
    copyable: bool = Field(False, description="是否支持复制")
    filters: Optional[Any] = Field(None, description="表头筛选菜单项")
    order: int = Field(0, description="查询表单中的权重")
    sorter: Optional[Any] = Field(None, description="排序规则")
    span: int = Field(1, description="包含列的数量（详情页）")
    width: int = Field(100, description="列宽（列表页）")


class FormItemStyle(BaseModel):
    width: Union[int, str] = Field("auto", description="组件宽度")


class CascaderFieldRule(BaseModel):
    """
    校验规则模型。
    """

    name: str = Field("", description="字段名")
    required: bool = Field(False, description="是否必填")
    message: str = Field("", description="校验失败提示信息")
    min_length: Optional[int] = Field(None, description="最小长度限制")
    max_length: Optional[int] = Field(None, description="最大长度限制")


class Cascader(Component):
    """
    级联选择组件的核心配置。
    """

    # 基础属性
    component_key: str = Field("", description="组件唯一标识")
    component: str = Field("cascaderField", description="组件名称")
    row_props: Dict[str, Any] = Field({}, description="Grid 模式下传递给 Row 的属性")
    col_props: Dict[str, Any] = Field({"xs": 24}, description="Grid 模式下传递给 Col 的属性")
    secondary: bool = Field(False, description="是否是次要控件（仅 LightFilter 下有效）")
    colon: bool = Field(True, description="是否显示 label 后面的冒号")
    extra: str = Field("", description="额外提示信息")
    has_feedback: bool = Field(False, description="是否展示校验状态图标")
    help: str = Field("", description="帮助信息")
    hidden: bool = Field(False, description="是否隐藏字段")
    initial_value: Any = Field(None, description="初始值")
    label: str = Field("", description="label 文本")
    label_align: str = Field("right", description="标签文本对齐方式")
    label_col: Any = Field(None, description="label 标签布局")
    name: str = Field("", description="字段名")
    no_style: bool = Field(False, description="是否不带样式")
    required: bool = Field(False, description="是否必填")
    tooltip: str = Field("", description="悬浮提示信息")
    value_prop_name: str = Field("", description="子节点值的属性名")
    wrapper_col: Any = Field(None, description="输入控件布局样式")

    # 列表/详情页相关属性
    column: TableColumn = Field(TableColumn(), description="表格列配置")
    align: Optional[TableColAlign] = Field(None, description="列对齐方式")
    fixed: Any = Field(None, description="列是否固定")
    editable: bool = Field(False, description="表格列是否可编辑")
    ellipsis: bool = Field(False, description="是否自动缩略")
    copyable: bool = Field(False, description="是否支持复制")
    filters: Any = Field(None, description="表头筛选菜单项")
    order: int = Field(0, description="查询表单中的权重")
    sorter: Any = Field(None, description="排序规则")
    span: int = Field(1, description="包含列的数量（详情页）")
    column_width: int = Field(100, description="设置列宽（列表页）")

    # 校验规则
    rules: List[CascaderFieldRule] = Field([], description="全局校验规则")
    creation_rules: List[CascaderFieldRule] = Field([], description="创建页校验规则")
    update_rules: List[CascaderFieldRule] = Field([], description="更新页校验规则")
    frontend_rules: List[CascaderFieldRule] = Field([], description="前端校验规则")

    # 显示控制
    show_on_index: bool = Field(True, description="在列表页展示")
    show_on_detail: bool = Field(True, description="在详情页展示")
    show_on_creation: bool = Field(True, description="在创建页面展示")
    show_on_update: bool = Field(True, description="在编辑页面展示")
    show_on_export: bool = Field(True, description="在导出 Excel 上展示")
    show_on_import: bool = Field(True, description="在导入 Excel 上展示")

    # 级联选择特有属性
    allow_clear: bool = Field(True, description="是否允许清除选择")
    auto_focus: bool = Field(False, description="是否自动获取焦点")
    bordered: bool = Field(True, description="是否有边框")
    clear_icon: Any = Field(None, description="自定义清除图标")
    change_on_select: bool = Field(False, description="点选每级菜单选项值都会发生变化")
    class_name: str = Field("", description="自定义类名")
    default_value: Any = Field(None, description="默认选中项")
    disabled: Any = Field(False, description="是否禁用")
    popup_class_name: str = Field("", description="浮层自定义类名")
    expand_icon: Any = Field(None, description="次级菜单展开图标")
    expand_trigger: str = Field("click", description="次级菜单展开方式（click 或 hover）")
    field_names: LabelValueChild = Field(LabelValueChild(label="label", value="value", children="children"), description="自定义 options 中 label、value、children 的字段")
    max_tag_count: int = Field(5, description="最多显示多少个 tag")
    max_tag_placeholder: str = Field("+更多", description="隐藏 tag 时显示的内容")
    max_tag_text_length: int = Field(10, description="最大显示的 tag 文本长度")
    not_found_content: str = Field("无匹配结果", description="当下拉列表为空时显示的内容")
    open: bool = Field(False, description="控制浮层显隐")
    options: List[CascaderOption] = Field([], description="可选项数据源")
    placeholder: str = Field("请选择", description="输入框占位文本")
    placement: str = Field("bottomLeft", description="浮层预设位置")
    show_search: bool = Field(False, description="是否在选择框中显示搜索框")
    size: str = Field("middle", description="输入框大小（large/middle/small）")
    status: str = Field("", description="校验状态（error/warning）")
    style: Dict[str, Any] = Field({}, description="自定义样式")
    suffix_icon: Any = Field(None, description="自定义选择框后缀图标")
    value: Any = Field(None, description="当前选中值")
    multiple: bool = Field(False, description="是否支持多选")
    show_checked_strategy: str = Field("SHOW_CHILD", description="选中项回填策略")
    remove_icon: Any = Field(None, description="自定义多选框清除图标")
    search_value: str = Field("", description="搜索值")
    dropdown_menu_column_style: Any = Field(None, description="下拉菜单列的样式")

    # 其他属性
    when: Optional[WhenComponent] = Field(None, description="When 组件，用于条件渲染")
    when_item: List[WhenItem] = Field([], description="When 组件的条件项")
    callback: Optional[Callable[[Dict[str, Any]], Any]] = Field(None, description="回调函数")
    api: str = Field("", description="获取数据接口")
    ignore: bool = Field(False, description="是否忽略保存到数据库")

    def init(self) -> "CascaderFieldComponent":
        """
        初始化级联选择组件的默认值。
        """
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.column = TableColumn()
        self.placeholder = "请选择"
        self.set_key(component.DEFAULT_KEY, component.DEFAULT_CRYPT)
        self.set_width(400)
        return self

    def set_key(self, key: str, crypt: bool) -> "CascaderFieldComponent":
        """
        设置组件密钥。
        """
        self.component_key = hex_make(key, crypt)
        return self

    def set_width(self, width: Union[int, str]) -> "CascaderFieldComponent":
        """
        设置组件宽度。
        """
        self.style["width"] = width
        return self

    def set_tooltip(self, tooltip: str) -> "CascaderFieldComponent":
        """
        设置提示信息。
        """
        self.tooltip = tooltip
        return self

    def set_options(self, *args: Any) -> "CascaderFieldComponent":
        """
        设置选项数据源。
        支持多种参数形式：
        - 单个选项列表
        - 使用 list 转换为选项
        - 指定 rootId、parentKeyName、labelName、valueName 构建树形结构
        """
        if len(args) == 1:
            if isinstance(args[0], list):
                self.options = args[0]
                return self
        elif len(args) >= 4:
            root_id = args[1] if len(args) > 1 else 0
            parent_key_name = args[2]
            label_name = args[3]
            value_name = args[4] if len(args) > 4 else "id"
            self.options = self.list_to_options(args[0], root_id, parent_key_name, label_name, value_name)
            return self
        return self

    def list_to_options(
        self,
        data: List[Dict[str, Any]],
        root_id: int,
        parent_key_name: str,
        label_name: str,
        value_name: str
    ) -> List[CascaderOption]:
        """
        将扁平列表转换为级联选项树。
        """
        tree = []
        for item in data:
            pid = item.get(parent_key_name)
            if pid == root_id:
                children = self.build_tree(data, item.get(value_name), parent_key_name, label_name, value_name)
                tree.append(CascaderOption(
                    label=item[label_name],
                    value=item[value_name],
                    children=children
                ))
        return tree

    def build_tree(
        self,
        data: List[Dict[str, Any]],
        pid: int,
        parent_key_name: str,
        label_name: str,
        value_name: str
    ) -> List[CascaderOption]:
        """
        递归构建树结构。
        """
        children = []
        for item in data:
            if item.get(parent_key_name) == pid:
                child = CascaderOption(
                    label=item[label_name],
                    value=item[value_name],
                    children=self.build_tree(data, item[value_name], parent_key_name, label_name, value_name)
                )
                children.append(child)
        return children

    def set_when(self, *value: Any) -> "CascaderFieldComponent":
        """
        设置 When 条件渲染逻辑。
        """
        w = WhenComponent(items=[])
        i = WhenItem(condition="", body=[], condition_name=self.name, option=None)

        if len(value) == 2:
            operator = "="
            option = value[0]
            callback = value[1]

            i.condition = f"<%={self.name} === '{option}' %>"
            i.body = callback() if callable(callback) else []
            i.option = option
            i.condition_operator = operator

        elif len(value) == 3:
            operator = value[0]
            option = value[1]
            callback = value[2]

            conditions = {
                "!=": f"<%={self.name} !== '{option}' %>",
                "=": f"<%={self.name} === '{option}' %>",
                ">": f"<%={self.name} > '{option}' %>",
                "<": f"<%={self.name} < '{option}' %>",
                "<=": f"<%={self.name} <= '{option}' %>",
                ">=": f"<%={self.name} >= '{option}' %>",
                "has": f"<%={self.name}.indexOf('{option}') != -1 %>",
                "in": f"<%= {option} in {self.name} %>",
            }

            i.condition = conditions.get(operator, f"<%={self.name} === '{option}' %>")
            i.body = callback() if callable(callback) else []
            i.option = option
            i.condition_operator = operator

        self.when_item.append(i)
        self.when = w.set_items(self.when_item)
        return self

    def hide_from_index(self, callback: bool) -> "CascaderFieldComponent":
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool) -> "CascaderFieldComponent":
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool) -> "CascaderFieldComponent":
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool) -> "CascaderFieldComponent":
        self.show_on_update = not callback
        return self

    def only_on_index(self) -> "CascaderFieldComponent":
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_forms(self) -> "CascaderFieldComponent":
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_creating(self) -> "CascaderFieldComponent":
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_updating(self) -> "CascaderFieldComponent":
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def except_on_forms(self) -> "CascaderFieldComponent":
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = True
        return self

    def set_api(self, api: str) -> "CascaderFieldComponent":
        self.api = api
        return self

    def set_callback(self, closure: Callable[[Dict[str, Any]], Any]) -> "CascaderFieldComponent":
        self.callback = closure
        return self

    def get_callback(self) -> Optional[Callable[[Dict[str, Any]], Any]]:
        return self.callback

    def set_allow_clear(self, allow_clear: bool) -> "CascaderFieldComponent":
        self.allow_clear = allow_clear
        return self

    def set_auto_focus(self, auto_focus: bool) -> "CascaderFieldComponent":
        self.auto_focus = auto_focus
        return self

    def set_bordered(self, bordered: bool) -> "CascaderFieldComponent":
        self.bordered = bordered
        return self

    def set_clear_icon(self, clear_icon: Any) -> "CascaderFieldComponent":
        self.clear_icon = clear_icon
        return self

    def set_change_on_select(self, change_on_select: bool) -> "CascaderFieldComponent":
        self.change_on_select = change_on_select
        return self

    def set_class_name(self, class_name: str) -> "CascaderFieldComponent":
        self.class_name = class_name
        return self

    def set_default_value(self, default_value: Any) -> "CascaderFieldComponent":
        self.default_value = default_value
        return self

    def set_popup_class_name(self, popup_class_name: str) -> "CascaderFieldComponent":
        self.popup_class_name = popup_class_name
        return self

    def set_expand_icon(self, expand_icon: Any) -> "CascaderFieldComponent":
        self.expand_icon = expand_icon
        return self

    def set_expand_trigger(self, expand_trigger: str) -> "CascaderFieldComponent":
        self.expand_trigger = expand_trigger
        return self

    def set_field_names(self, field_names: LabelValueChild) -> "CascaderFieldComponent":
        self.field_names = field_names
        return self

    def set_max_tag_count(self, max_tag_count: int) -> "CascaderFieldComponent":
        self.max_tag_count = max_tag_count
        return self

    def set_max_tag_placeholder(self, max_tag_placeholder: str) -> "CascaderFieldComponent":
        self.max_tag_placeholder = max_tag_placeholder
        return self

    def set_max_tag_text_length(self, max_tag_text_length: int) -> "CascaderFieldComponent":
        self.max_tag_text_length = max_tag_text_length
        return self

    def set_not_found_content(self, not_found_content: str) -> "CascaderFieldComponent":
        self.not_found_content = not_found_content
        return self

    def set_open(self, open: bool) -> "CascaderFieldComponent":
        self.open = open
        return self

    def set_placeholder(self, placeholder: str) -> "CascaderFieldComponent":
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str) -> "CascaderFieldComponent":
        self.placement = placement
        return self

    def set_show_search(self, show_search: bool) -> "CascaderFieldComponent":
        self.show_search = show_search
        return self

    def set_size(self, size: str) -> "CascaderFieldComponent":
        self.size = size
        return self

    def set_status(self, status: str) -> "CascaderFieldComponent":
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any) -> "CascaderFieldComponent":
        self.suffix_icon = suffix_icon
        return self

    def set_multiple(self, multiple: bool) -> "CascaderFieldComponent":
        self.multiple = multiple
        return self

    def set_show_checked_strategy(self, strategy: str) -> "CascaderFieldComponent":
        self.show_checked_strategy = strategy
        return self

    def set_remove_icon(self, icon: Any) -> "CascaderFieldComponent":
        self.remove_icon = icon
        return self

    def set_search_value(self, value: str) -> "CascaderFieldComponent":
        self.search_value = value
        return self

    def set_dropdown_menu_column_style(self, style: Any) -> "CascaderFieldComponent":
        self.dropdown_menu_column_style = style
        return self