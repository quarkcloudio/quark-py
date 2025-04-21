from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Union, List


@dataclass
class Column:
    # 字段定义
    ComponentKey: str = ""
    Title: str = ""
    Attribute: str = ""
    Align: str = "left"
    DataIndex: str = ""
    Fixed: Any = None
    Tooltip: str = ""
    Ellipsis: bool = False
    Copyable: bool = False
    ValueEnum: Any = None
    ValueType: str = ""
    HideInSearch: bool = True
    HideInTable: bool = False
    HideInForm: bool = False
    Filters: Any = False
    Order: int = 0
    Sorter: Any = None
    Span: int = 0
    Width: int = 0
    Editable: Any = False
    Actions: Any = False
    FormItemProps: Any = None
    FieldProps: Any = None
    Style: Dict[str, Any] = field(default_factory=dict)

    # 内部字段（不暴露）
    component: str = field(default="column", init=False)
    key: str = field(default="defaultKey", init=False)

    def set_key(self, key: str, crypt: bool = False):
        self.key = key
        return self

    def set_style(self, style: Dict[str, Any]):
        self.Style = style
        return self

    def set_title(self, title: str):
        self.Title = title
        return self

    def set_attribute(self, attribute: str):
        self.set_key(attribute)
        self.ComponentKey = attribute
        self.DataIndex = attribute
        self.Attribute = attribute
        return self

    def set_align(self, align: str):
        self.Align = align
        return self

    def set_fixed(self, fixed: Any):
        self.Fixed = fixed
        return self

    def set_tooltip(self, tooltip: str):
        self.Tooltip = tooltip
        return self

    def set_ellipsis(self, ellipsis: bool):
        self.Ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        self.Copyable = copyable
        return self

    def set_value_enum(self, value_enum: Union[Dict[Any, Any], List[Dict[str, Any]]]):
        if isinstance(value_enum, dict):
            value_enum_str = {}
            value_enum_int = {}
            for k, v in value_enum.items():
                if isinstance(k, str):
                    value_enum_str[k] = v
                else:
                    value_enum_int[int(k)] = v
            self.ValueEnum = value_enum_str or value_enum_int
        else:
            self.ValueEnum = value_enum
        return self

    def set_value_type(self, value_type: str):
        self.ValueType = value_type
        return self

    def set_hide_in_search(self, hide: bool):
        self.HideInSearch = hide
        return self

    def set_hide_in_table(self, hide: bool):
        self.HideInTable = hide
        return self

    def set_filters(self, filters: Union[bool, Dict[str, str], List[Dict[str, str]]]):
        if isinstance(filters, dict):
            self.Filters = [{"text": v, "value": k} for k, v in filters.items()]
        else:
            self.Filters = filters
        return self

    def set_order(self, order: int):
        self.Order = order
        return self

    def set_sorter(self, sorter: Any):
        self.Sorter = sorter
        return self

    def set_span(self, span: int):
        self.Span = span
        return self

    def set_width(self, width: int):
        self.Width = width
        return self

    def set_editable(self, name: str, options: Any, action: str):
        get_options = []
        if name == "select" and isinstance(options, list):
            for idx, v in enumerate(options):
                get_options.append({"label": v, "value": idx})
        else:
            get_options = options

        self.Editable = {
            "name": name,
            "options": get_options,
            "action": action,
        }
        return self

    def set_actions(self, actions: Any):
        self.Actions = actions
        return self

    def set_form_item_props(self, form_item_props: Any):
        self.FormItemProps = form_item_props
        return self

    def set_field_props(self, field_props: Any):
        self.FieldProps = field_props
        return self
