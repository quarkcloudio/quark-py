from pydantic import Field, model_validator
from typing import Any, Dict, Union, List, Optional
from ..component import Component


class Column(Component):
    component: str = "column"
    title: str = None
    attribute: str = None
    align: str = "left"
    data_index: str = None
    fixed: Any = None
    tooltip: str = None
    ellipsis: bool = None
    copyable: bool = None
    value_enum: Optional[Union[Dict[Any, Any], List[Dict[str, Any]]]] = None
    value_type: str = None
    hide_in_search: bool = True
    hide_in_table: bool = None
    hide_in_form: bool = None
    filters: Optional[Union[bool, Dict[str, str], List[Dict[str, str]]]] = None
    order: int = None
    sorter: Any = None
    span: int = None
    width: int = None
    editable: Optional[Dict[str, Any]] = None
    actions: Optional[Any] = None
    form_item_props: Optional[Any] = None
    field_props: Optional[Any] = None
    style: Dict[str, Any] = None

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    # 设置方法（链式调用）
    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_attribute(self, attribute: str):
        self.componentkey = attribute
        self.data_index = attribute
        self.attribute = attribute
        return self

    def set_align(self, align: str):
        self.align = align
        return self

    def set_fixed(self, fixed: Any):
        self.fixed = fixed
        return self

    def set_tooltip(self, tooltip: str):
        self.tooltip = tooltip
        return self

    def set_ellipsis(self, ellipsis: bool):
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        self.copyable = copyable
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
            self.value_enum = value_enum_str or value_enum_int
        else:
            self.value_enum = value_enum
        return self

    def set_value_type(self, value_type: str):
        self.value_type = value_type
        return self

    def set_hide_in_search(self, hide: bool):
        self.hide_in_search = hide
        return self

    def set_hide_in_table(self, hide: bool):
        self.hide_in_table = hide
        return self

    def set_filters(self, filters: Union[bool, Dict[str, str], List[Dict[str, str]]]):
        if isinstance(filters, dict):
            self.filters = [{"text": v, "value": k} for k, v in filters.items()]
        else:
            self.filters = filters
        return self

    def set_order(self, order: int):
        self.order = order
        return self

    def set_sorter(self, sorter: Any):
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        self.span = span
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def set_editable(self, name: str, options: Any, action: str):
        get_options = []
        if name == "select" and isinstance(options, list):
            for idx, v in enumerate(options):
                get_options.append({"label": v, "value": idx})
        else:
            get_options = options

        self.editable = {
            "name": name,
            "options": get_options,
            "action": action,
        }
        return self

    def set_actions(self, actions: Any):
        self.actions = actions
        return self

    def set_form_item_props(self, form_item_props: Any):
        self.form_item_props = form_item_props
        return self

    def set_field_props(self, field_props: Any):
        self.field_props = field_props
        return self
