from pydantic import Field, model_validator
from typing import Any, List, Optional, Union, Callable
from ...component.element import Element
from ...table.column import Column
from ..rule import Rule
from .when import Component as When, Item as WhenItem
import json
import string

class Component(Element):
    component: str = "textField"
    row_props: Optional[dict] = None
    col_props: Optional[dict] = None
    secondary: bool = False
    colon: bool = True
    extra: str = None
    has_feedback: bool = False
    help: str = None
    hidden: bool = False
    initial_value: Optional[Any] = None
    label: str = None
    label_align: str = "right"
    label_col: Optional[Union[dict, str]] = None
    name: str = None
    no_style: bool = None
    required: bool = False
    tooltip: str = None
    value_prop_name: str = None
    wrapper_col: Optional[Union[dict, str]] = None

    column: Column = Field(default_factory=Column)
    align: str = None
    fixed: Optional[Union[bool, str]] = None
    editable: bool = False
    ellipsis: bool = False
    copyable: bool = False
    filters: Optional[Any] = None
    order: int = 0
    sorter: Optional[Union[bool, dict]] = None
    span: int = 0
    column_width: int = 0

    api: str = None
    ignore: bool = False
    rules: List[Rule] = Field(default_factory=list)
    creation_rules: List[Rule] = Field(default_factory=list)
    update_rules: List[Rule] = Field(default_factory=list)
    frontend_rules: List[Rule] = Field(default_factory=list)
    when: Optional[When] = None
    when_item: List[WhenItem] = Field(default_factory=list)
    show_on_index: bool = True
    show_on_detail: bool = True
    show_on_creation: bool = True
    show_on_update: bool = True
    show_on_export: bool = True
    show_on_import: bool = True
    callback: Optional[Callable] = None

    addon_after: Optional[Any] = None
    addon_before: Optional[Any] = None
    allow_clear: bool = False
    bordered: bool = True
    default_value: Optional[Any] = None
    disabled: Optional[Union[bool, str]] = None
    id: str = None
    max_length: int = 200
    show_count: bool = False
    status: str = None
    prefix: Optional[Any] = None
    size: str = None
    suffix: Optional[Any] = None
    type: str = None
    value: Optional[Any] = None
    placeholder: str = "请输入"
    style: dict = Field(default_factory=dict)

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: dict):
        self.style = style
        return self

    def set_tooltip(self, tooltip: str):
        self.tooltip = tooltip
        return self

    def set_width(self, width: Union[int, str]):
        self.style["width"] = width
        return self

    def set_row_props(self, row_props: dict):
        self.row_props = row_props
        return self

    def set_col_props(self, col_props: dict):
        self.col_props = col_props
        return self

    def set_secondary(self, secondary: bool):
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool):
        self.colon = colon
        return self

    def set_extra(self, extra: str):
        self.extra = extra
        return self

    def set_has_feedback(self, has_feedback: bool):
        self.has_feedback = has_feedback
        return self

    def set_help(self, help: str):
        self.help = help
        return self

    def set_no_style(self):
        self.no_style = True
        return self

    def set_label(self, label: str):
        self.label = label
        return self

    def set_label_align(self, align: str):
        self.label_align = align
        return self

    def set_label_col(self, col: Union[dict, str]):
        self.label_col = col
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def set_name_as_label(self):
        self.label = string.capwords(self.name)
        return self

    def set_required(self):
        self.required = True
        return self

    def build_frontend_rules(self, path: str):
        frontend_rules = []
        rules = [rule for rule in self.rules]
        uri = path.split("/")
        is_creating = uri[-1] in ["create", "store"]
        is_editing = uri[-1] in ["edit", "update"]

        if is_creating:
            rules.extend(self.creation_rules)
        if is_editing:
            rules.extend(self.update_rules)

        self.frontend_rules = [self._convert_to_frontend_rule(rule) for rule in rules]
        return self

    def _convert_to_frontend_rule(self, rule: Rule) -> Rule:
        return rule

    def set_rules(self, rules: List[Rule]):
        for rule in rules:
            rule.name = self.name
        self.rules = rules
        return self

    def set_creation_rules(self, rules: List[Rule]):
        self.creation_rules = [Rule(name=self.name, rule=rule.rule, message=rule.message) for rule in rules]
        return self

    def set_update_rules(self, rules: List[Rule]):
        self.update_rules = [Rule(name=self.name, rule=rule.rule, message=rule.message) for rule in rules]
        return self

    def get_rules(self) -> List[Rule]:
        return self.rules

    def get_creation_rules(self) -> List[Rule]:
        return self.creation_rules

    def get_update_rules(self) -> List[Rule]:
        return self.update_rules

    def set_value_prop_name(self, value_prop_name: str):
        self.value_prop_name = value_prop_name
        return self

    def set_wrapper_col(self, col: Union[dict, str]):
        self.wrapper_col = col
        return self

    def set_column(self, f):
        self.column = f(self.column)
        return self

    def set_align(self, align: str):
        self.align = align
        return self

    def set_fixed(self, fixed: Union[bool, str]):
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool):
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool):
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any):
        if isinstance(filters, dict):
            self.filters = [{"text": v, "value": k} for k, v in filters.items()]
        else:
            self.filters = filters
        return self

    def set_order(self, order: int):
        self.order = order
        return self

    def set_sorter(self, sorter: Union[bool, dict]):
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        self.span = span
        return self

    def set_column_width(self, width: int):
        self.column_width = width
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_default(self, value: Any):
        self.default_value = value
        return self

    def set_disabled(self, disabled: Union[bool, str]):
        self.disabled = disabled
        return self

    def set_ignore(self, ignore: bool):
        self.ignore = ignore
        return self

    def set_when(self, *value):
        w = When()
        i = WhenItem("", "", "", None, None)

        if len(value) == 2:
            operator = "="
            option = value[0]
            callback = value[1]

            i.body = callback()

        if len(value) == 3:
            operator = value[0]
            option = value[1]
            callback = value[2]

            i.body = callback()

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
            i.condition = f"<%=String({self.name}) >= '{option_str}' %>"
        elif operator == "has":
            i.condition = f"<%=(String({self.name}).indexOf('{option_str}') !=-1) %>"
        elif operator == "in":
            json_str = json.dumps(option)
            i.condition = f"<%=({json_str}.indexOf({self.name}) !=-1) %>"
        else:
            i.condition = f"<%=String({self.name}) === '{option_str}' %>"

        i.condition_name = self.name
        i.condition_operator = operator
        i.option = option
        self.when_item.append(i)
        self.when = w.set_items(self.when_item)

        return self

    def get_when(self) -> Optional[When]:
        return self.when

    def hide_from_index(self, callback: bool):
        self.show_on_index = not callback
        return self

    def hide_from_detail(self, callback: bool):
        self.show_on_detail = not callback
        return self

    def hide_when_creating(self, callback: bool):
        self.show_on_creation = not callback
        return self

    def hide_when_updating(self, callback: bool):
        self.show_on_update = not callback
        return self

    def hide_when_exporting(self, callback: bool):
        self.show_on_export = not callback
        return self

    def hide_when_importing(self, callback: bool):
        self.show_on_import = not callback
        return self

    def on_index_showing(self, callback: bool):
        self.show_on_index = callback
        return self

    def on_detail_showing(self, callback: bool):
        self.show_on_detail = callback
        return self

    def show_on_creating(self, callback: bool):
        self.show_on_creation = callback
        return self

    def show_on_updating(self, callback: bool):
        self.show_on_update = callback
        return self

    def show_on_exporting(self, callback: bool):
        self.show_on_export = callback
        return self

    def show_on_importing(self, callback: bool):
        self.show_on_import = callback
        return self

    def only_on_index(self):
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_detail(self):
        self.show_on_index = False
        self.show_on_detail = True
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_forms(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_creating(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = True
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_updating(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = True
        self.show_on_export = False
        self.show_on_import = False
        return self

    def only_on_export(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = True
        self.show_on_import = False
        return self

    def only_on_import(self):
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = True
        return self

    def except_on_forms(self):
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

    def get_value_enum(self) -> dict:
        return {}

    def set_callback(self, closure: Callable):
        if closure:
            self.callback = closure
        return self

    def get_callback(self) -> Optional[Callable]:
        return self.callback

    def set_api(self, api: str):
        self.api = api
        return self

    def set_addon_after(self, addon_after: Any):
        self.addon_after = addon_after
        return self

    def set_addon_before(self, addon_before: Any):
        self.addon_before = addon_before
        return self

    def set_allow_clear(self, allow_clear: bool):
        self.allow_clear = allow_clear
        return self

    def set_bordered(self, bordered: bool):
        self.bordered = bordered
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_id(self, id: str):
        self.id = id
        return self

    def set_max_length(self, max_length: int):
        self.max_length = max_length
        return self

    def set_show_count(self, show_count: bool):
        self.show_count = show_count
        return self

    def set_status(self, status: str):
        self.status = status
        return self

    def set_placeholder(self, placeholder: str):
        self.placeholder = placeholder
        return self

    def set_prefix(self, prefix: Any):
        self.prefix = prefix
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_suffix(self, suffix: Any):
        self.suffix = suffix
        return self

    def set_type(self, type: str):
        self.type = type
        return self