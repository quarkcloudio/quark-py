from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
import json
from ..component.element import Element

def parse_initial_values(values: Dict[str, Any]) -> Dict[str, Any]:
    parsed = {}
    for k, v in values.items():
        if isinstance(v, str):
            try:
                parsed[k] = json.loads(v)
            except json.JSONDecodeError:
                parsed[k] = v
        else:
            parsed[k] = v
    return parsed


@dataclass
class Component(Element):
    component: str = "form"
    title: str = ""
    width: str = ""
    colon: bool = True
    values: Dict[str, Any] = field(default_factory=dict)
    initial_values: Dict[str, Any] = field(default_factory=dict)
    label_align: str = "right"
    name: str = ""
    preserve: bool = True
    required_mark: bool = True
    scroll_to_first_error: bool = False
    size: str = "default"
    date_formatter: str = "string"
    layout: str = "horizontal"
    grid: bool = False
    row_props: Dict[str, Any] = field(default_factory=dict)
    label_col: Dict[str, Any] = field(default_factory=dict)
    wrapper_col: Dict[str, Any] = field(default_factory=dict)
    button_wrapper_col: Dict[str, Any] = field(default_factory=dict)
    api: str = ""
    api_type: str = "POST"
    target_blank: bool = False
    init_api: str = ""
    body: List[Any] = field(default_factory=list)
    actions: List[Any] = field(default_factory=list)
    component_key: str = ""

    def __post_init__(self):
        self.label_col = {"span": 4}
        self.wrapper_col = {"span": 20}
        self.button_wrapper_col = {"offset": 4, "span": 20}
        self.set_key("", True)

    def set_title(self, title: str):
        self.title = title
        return self

    def set_width(self, width: str):
        self.width = width
        return self

    def set_colon(self, colon: bool):
        self.colon = colon
        return self

    def set_label_align(self, label_align: str):
        self.label_align = label_align
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def set_preserve(self, preserve: bool):
        self.preserve = preserve
        return self

    def set_required_mark(self, required_mark: bool):
        self.required_mark = required_mark
        return self

    def set_scroll_to_first_error(self, scroll: bool):
        self.scroll_to_first_error = scroll
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_date_formatter(self, formatter: str):
        self.date_formatter = formatter
        return self

    def set_layout(self, layout: str):
        self.layout = layout
        if layout == "vertical":
            self.label_col = {}
            self.wrapper_col = {}
            self.button_wrapper_col = {}
        return self

    def set_label_col(self, label_col: Dict[str, Any]):
        self.label_col = label_col
        return self

    def set_wrapper_col(self, wrapper_col: Dict[str, Any]):
        if self.layout == "vertical":
            raise ValueError("Can't set wrapper_col in vertical layout")
        self.wrapper_col = wrapper_col
        return self

    def set_button_wrapper_col(self, button_wrapper_col: Dict[str, Any]):
        if self.layout == "vertical":
            raise ValueError("Can't set button_wrapper_col in vertical layout")
        self.button_wrapper_col = button_wrapper_col
        return self

    def set_api(self, api: str):
        self.api = api
        return self

    def set_api_type(self, api_type: str):
        self.api_type = api_type
        return self

    def set_target_blank(self, target_blank: bool):
        self.target_blank = target_blank
        return self

    def set_init_api(self, init_api: str):
        self.init_api = init_api
        return self

    def set_body(self, body: List[Any]):
        self.body = body
        return self

    def set_actions(self, actions: List[Any]):
        self.actions = actions
        return self

    def set_initial_values(self, values: Dict[str, Any]):
        self.initial_values = parse_initial_values(values)
        return self

    def parse_submit_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        result = {}
        for key, val in data.items():
            if isinstance(val, dict):
                result[key] = json.dumps(val)
            else:
                result[key] = val
        return result