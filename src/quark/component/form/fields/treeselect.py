from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Callable, Union

class FieldNames(BaseModel):
    label: str
    value: str
    children: str

class TreeData(BaseModel):
    title: str
    value: Any
    children: List['TreeData'] = []
    disabled: bool = False
    disable_checkbox: bool = False
    selectable: bool = False
    checkable: bool = False

TreeData.update_forward_refs()

class Component(BaseModel):
    component_key: str
    component: str

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

    column: Optional[Any] = None
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
    rules: List[Any] = []
    creation_rules: List[Any] = []
    update_rules: List[Any] = []
    frontend_rules: List[Any] = []
    when: Optional[Any] = None
    when_item: List[Any] = []
    show_on_index: bool = True
    show_on_detail: bool = True
    show_on_creation: bool = True
    show_on_update: bool = True
    show_on_export: bool = True
    show_on_import: bool = True
    callback: Optional[Callable[[Dict[str, Any]], Any]] = None

    allow_clear: bool = True
    auto_clear_search_value: bool = False
    bordered: bool = True
    default_value: Optional[Any] = None
    disabled: bool = False
    popup_class_name: Optional[str] = None
    dropdown_match_select_width: Optional[Any] = None
    dropdown_style: Optional[Any] = None
    field_names: Optional[FieldNames] = None
    label_in_value: bool = False
    list_height: int = 256
    max_tag_count: int = 0
    max_tag_placeholder: Optional[str] = None
    max_tag_text_length: int = 0
    multiple: bool = False
    not_found_content: Optional[str] = None
    placeholder: Optional[str] = None
    placement: Optional[str] = None
    search_value: Optional[str] = None
    show_arrow: bool = True
    show_search: bool = False
    size: Optional[str] = None
    status: Optional[str] = None
    suffix_icon: Optional[Any] = None
    switcher_icon: Optional[Any] = None
    tree_checkable: bool = False
    tree_check_strictly: bool = False
    tree_data: List[TreeData] = []
    tree_data_simple_mode: Optional[Any] = None
    tree_default_expand_all: bool = True
    tree_default_expanded_keys: List[Any] = []
    tree_expand_action: Optional[Any] = None
    tree_expanded_keys: List[Any] = []
    tree_icon: bool = False
    tree_line: bool = True
    tree_node_filter_prop: Optional[str] = None
    tree_node_label_prop: Optional[str] = None
    value: Optional[Any] = None
    virtual: bool = True
    style: Optional[Dict[str, Any]] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.component = "treeSelectField"
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.allow_clear = True
        self.tree_default_expand_all = True
        self.tree_line = True
        self.set_width(200)
        self.set_key("DEFAULT_KEY", False)

    def set_key(self, key: str, crypt: bool) -> 'Component':
        # 这里简单模拟 hex.Make 函数的功能，实际需要实现具体逻辑
        self.component_key = key
        return self

    def set_tooltip(self, tooltip: str) -> 'Component':
        self.tooltip = tooltip
        return self

    def set_width(self, width: Any) -> 'Component':
        style = self.style or {}
        style["width"] = width
        self.style = style
        return self

    def set_row_props(self, row_props: Dict[str, Any]) -> 'Component':
        self.row_props = row_props
        return self

    def set_col_props(self, col_props: Dict[str, Any]) -> 'Component':
        self.col_props = col_props
        return self

    def set_secondary(self, secondary: bool) -> 'Component':
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool) -> 'Component':
        self.colon = colon
        return self

    def set_extra(self, extra: str) -> 'Component':
        self.extra = extra
        return self

    def set_has_feedback(self, has_feedback: bool) -> 'Component':
        self.has_feedback = has_feedback
        return self

    def set_help(self, help_text: str) -> 'Component':
        self.help = help_text
        return self

    def set_no_style(self) -> 'Component':
        self.no_style = True
        return self

    def set_label(self, label: str) -> 'Component':
        self.label = label
        return self

    def set_label_align(self, align: str) -> 'Component':
        self.label_align = align
        return self

    def set_label_col(self, col: Any) -> 'Component':
        self.label_col = col
        return self

    def set_name(self, name: str) -> 'Component':
        self.name = name
        return self

    def set_name_as_label(self) -> 'Component':
        # 这里简单模拟 strings.Title 函数的功能，实际需要实现具体逻辑
        self.label = name.title()
        return self

    def set_required(self) -> 'Component':
        self.required = True
        return self

    def build_frontend_rules(self, path: str) -> 'Component':
        uri = path.split("/")
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        rules = []
        creation_rules = []
        update_rules = []

        if self.rules:
            rules = self.rules  # 这里需要实现 ConvertToFrontendRules 函数
        if is_creating and self.creation_rules:
            creation_rules = self.creation_rules  # 这里需要实现 ConvertToFrontendRules 函数
        if is_editing and self.update_rules:
            update_rules = self.update_rules  # 这里需要实现 ConvertToFrontendRules 函数

        frontend_rules = []
        frontend_rules.extend(rules)
        frontend_rules.extend(creation_rules)
        frontend_rules.extend(update_rules)

        self.frontend_rules = frontend_rules
        return self

    def set_rules(self, rules: List[Any]) -> 'Component':
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Any]) -> 'Component':
        for rule in rules:
            rule.name = self.name
        self.creation_rules = rules
        return self

    def set_update_rules(self, rules: List[Any]) -> 'Component':
        for rule in rules:
            rule.name = self.name
        self.update_rules = rules
        return self

    def get_rules(self) -> List[Any]:
        return self.rules

    def get_creation_rules(self) -> List[Any]:
        return self.creation_rules

    def get_update_rules(self) -> List[Any]:
        return self.update_rules

    def set_value_prop_name(self, value_prop_name: str) -> 'Component':
        self.value_prop_name = value_prop_name
        return self

    def set_wrapper_col(self, col: Any) -> 'Component':
        self.wrapper_col = col
        return self

    def set_column(self, f: Callable[[Any], Any]) -> 'Component':
        self.column = f(self.column)
        return self

    def set_align(self, align: str) -> 'Component':
        self.align = align
        return self

    def set_fixed(self, fixed: Any) -> 'Component':
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool) -> 'Component':
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool) -> 'Component':
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool) -> 'Component':
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any) -> 'Component':
        if isinstance(filters, dict):
            tmp_filters = []
            for k, v in filters.items():
                tmp_filters.append({"text": v, "value": k})
            self.filters = tmp_filters
        else:
            self.filters = filters
        return self

    def set_order(self, order: int) -> 'Component':
        self.order = order
        return self

    def set_sorter(self, sorter: bool) -> 'Component':
        self.sorter = sorter
        return self

    def set_span(self, span: int) -> 'Component':
        self.span = span
        return self

    def set_column_width(self, width: int) -> 'Component':
        self.column_width = width
        return self

    def set_value(self, value: Any) -> 'Component':
        self.value = value
        return self

    def set_default(self, value: Any) -> 'Component':
        self.default_value = value
        return self

    def set_disabled(self, disabled: bool) -> 'Component':
        self.disabled = disabled
        return self

    def set_ignore(self, ignore: bool) -> 'Component':
        self.ignore = ignore
        return self

    def set_when(self, *value: Any) -> 'Component':
        # 这里需要实现 when 组件相关逻辑
        return self

    def get_when(self) -> Optional[Any]:
        return self.when

    def hide_from_index(self, callback: bool) -> 'Component':
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool) -> 'Component':
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool) -> 'Component':
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool) -> 'Component':
        self.show_on_update = not callback
        return self

    def hide_when_exporting(self, callback: bool) -> 'Component':
        self.show_on_export = not callback
        return self

    def hide_when_importing(self, callback: bool) -> 'Component':
        self.show_on_import = not callback
        return self

    def on_index_showing(self, callback: bool) -> 'Component':
        self.show_on_index = callback
        return self

    def on_detail_showing(self, callback: bool) -> 'Component':
        self.show_on_detail = callback
        return self

    def show_on_creating(self, callback: bool) -> 'Component':
        self.show_on_creation = callback
        return self

    def show_on_updating(self, callback: bool) -> 'Component':
        self.show_on_update = callback
        return self

    def show_on_exporting(self, callback: bool) -> 'Component':
        self.show_on_export = callback
        return self

    def show_on_importing(self, callback: bool) -> 'Component':
        self.show_on_import = callback
        return self

    def only_on_index(self) -> 'Component':
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_detail(self) -> 'Component':
        self.show_on_index = False
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_forms(self) -> 'Component':
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_creating(self) -> 'Component':
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_updating(self) -> 'Component':
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_export(self) -> 'Component':
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = False
        return self

    def only_on_import(self) -> 'Component':
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = True
        return self

    def except_on_forms(self) -> 'Component':
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = True
        return self

    def is_shown_on_update(self) -> bool:
        return self.show_on_update

    def is_shown_on_index(self) -> bool:
        return self.show_on_index

    def is_shown_on_detail(self) -> bool:
        return self.show_on_detail

    def is_shown_on_creation(self) -> bool:
        return self.show_on_creation

    def is_shown_on_export(self) -> bool:
        return self.show_on_export

    def is_shown_on_import(self) -> bool:
        return self.show_on_import

    def get_options(self) -> List[TreeData]:
        return self.tree_data

    def set_callback(self, closure: Optional[Callable[[Dict[str, Any]], Any]]) -> 'Component':
        if closure is not None:
            self.callback = closure
        return self

    def get_callback(self) -> Optional[Callable[[Dict[str, Any]], Any]]:
        return self.callback

    def set_api(self, api: str) -> 'Component':
        self.api = api
        return self

    def set_allow_clear(self, allow_clear: bool) -> 'Component':
        self.allow_clear = allow_clear
        return self

    def set_auto_clear_search_value(self, auto_clear_search_value: bool) -> 'Component':
        self.auto_clear_search_value = auto_clear_search_value
        return self

    def set_bordered(self, bordered: bool) -> 'Component':
        self.bordered = bordered
        return self

    def set_popup_class_name(self, popup_class_name: str) -> 'Component':
        self.popup_class_name = popup_class_name
        return self

    def set_dropdown_match_select_width(self, dropdown_match_select_width: Any) -> 'Component':
        self.dropdown_match_select_width = dropdown_match_select_width
        return self

    def set_dropdown_style(self, dropdown_style: Any) -> 'Component':
        self.dropdown_style = dropdown_style
        return self

    def set_field_names(self, field_names: FieldNames) -> 'Component':
        self.field_names = field_names
        return self

    def set_label_in_value(self, label_in_value: bool) -> 'Component':
        self.label_in_value = label_in_value
        return self

    def set_list_height(self, list_height: int) -> 'Component':
        self.list_height = list_height
        return self

    def set_max_tag_count(self, max_tag_count: int) -> 'Component':
        self.max_tag_count = max_tag_count
        return self

    def set_max_tag_placeholder(self, max_tag_placeholder: str) -> 'Component':
        self.max_tag_placeholder = max_tag_placeholder
        return self

    def set_max_tag_text_length(self, max_tag_text_length: int) -> 'Component':
        self.max_tag_text_length = max_tag_text_length
        return self

    def set_multiple(self, multiple: bool) -> 'Component':
        self.multiple = multiple
        return self

    def set_not_found_content(self, not_found_content: str) -> 'Component':
        self.not_found_content = not_found_content
        return self

    def set_placeholder(self, placeholder: str) -> 'Component':
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str) -> 'Component':
        self.placement = placement
        return self

    def set_search_value(self, search_value: str) -> 'Component':
        self.search_value = search_value
        return self

    def set_show_arrow(self, show_arrow: bool) -> 'Component':
        self.show_arrow = show_arrow
        return self

    def set_show_search(self, show_search: bool) -> 'Component':
        self.show_search = show_search
        return self

    def set_size(self, size: str) -> 'Component':
        self.size = size
        return self

    def set_status(self, status: str) -> 'Component':
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any) -> 'Component':
        self.suffix_icon = suffix_icon
        return self

    def set_switcher_icon(self, switcher_icon: Any) -> 'Component':
        self.switcher_icon = switcher_icon
        return self

    def set_tree_checkable(self, tree_checkable: bool) -> 'Component':
        self.tree_checkable = tree_checkable
        return self

    def set_tree_check_strictly(self, tree_check_strictly: bool) -> 'Component':
        self.tree_check_strictly = tree_check_strictly
        return self

    def build_tree(self, items: Any, pid: int, parent_key_name: str, title_name: str, value_name: str) -> List[TreeData]:
        # 这里需要实现反射构建树结构的逻辑
        return []

    def list_to_tree_data(self, list_data: Any, root_id: int, parent_key_name: str, title_name: str, value_name: str) -> List[TreeData]:
        return self.build_tree(list_data, root_id, parent_key_name, title_name, value_name)

    def set_tree_data(self, *tree_data: Any) -> 'Component':
        if len(tree_data) == 1:
            if isinstance(tree_data[0], list) and all(isinstance(item, TreeData) for item in tree_data[0]):
                self.tree_data = tree_data[0]
                return self
        if len(tree_data) == 4:
            self.tree_data = self.list_to_tree_data(tree_data[0], 0, tree_data[1], tree_data[2], tree_data[3])
        if len(tree_data) == 5:
            self.tree_data = self.list_to_tree_data(tree_data[0], tree_data[1], tree_data[2], tree_data[3], tree_data[4])
        return self

    def get_tree_data(self) -> List[TreeData]:
        return self.tree_data

    def get_data(self) -> List[TreeData]:
        return self.tree_data

    def set_tree_data_simple_mode(self, tree_data_simple_mode: Any) -> 'Component':
        self.tree_data_simple_mode = tree_data_simple_mode
        return self

    def set_tree_default_expand_all(self, tree_default_expand_all: bool) -> 'Component':
        self.tree_default_expand_all = tree_default_expand_all
        return self

    def set_tree_default_expanded_keys(self, tree_default_expanded_keys: List[Any]) -> 'Component':
        self.tree_default_expanded_keys = tree_default_expanded_keys
        return self

    def set_tree_expand_action(self, tree_expand_action: List[Any]) -> 'Component':
        self.tree_expand_action = tree_expand_action
        return self

    def set_tree_expanded_keys(self, tree_expanded_keys: List[Any]) -> 'Component':
        self.tree_expanded_keys = tree_expanded_keys
        return self

    def set_tree_icon(self, tree_icon: bool) -> 'Component':
        self.tree_icon = tree_icon
        return self

    def set_tree_line(self, tree_line: bool) -> 'Component':
        self.tree_line = tree_line
        return self

    def set_tree_node_filter_prop(self, tree_node_filter_prop: str) -> 'Component':
        self.tree_node_filter_prop = tree_node_filter_prop
        return self

    def set_tree_node_label_prop(self, tree_node_label_prop: str) -> 'Component':
        self.tree_node_label_prop = tree_node_label_prop
        return self

    def set_virtual(self, virtual: bool) -> 'Component':
        self.virtual = virtual
        return self

    def set_style(self, style: Dict[str, Any]) -> 'Component':
        self.style = style
        return self

def new() -> Component:
    return Component(component_key="", component="")