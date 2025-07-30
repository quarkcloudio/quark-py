from pydantic import Field, model_validator
from typing import Any, List, Dict
from ..component import Component


class Search(Component):
    component: str = "search"
    filter_type: str = None
    search_text: str = None
    reset_text: str = None
    submit_text: str = None
    label_width: int = None
    span: int = None
    class_name: str = None
    default_collapsed: bool = True
    show_hidden_num: bool = False
    export_text: str = None
    export_api: str = None
    items: List[Any] = Field(default_factory=list)
    style: Dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    # 设置方法（链式调用）
    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_filter_type(self, filter_type: str):
        self.filter_type = filter_type
        return self

    def set_collapsed(self, collapsed: bool):
        self.default_collapsed = collapsed
        return self

    def set_search_text(self, search_text: str):
        self.search_text = search_text
        return self

    def set_reset_text(self, reset_text: str):
        self.reset_text = reset_text
        return self

    def set_submit_text(self, submit_text: str):
        self.submit_text = submit_text
        return self

    def set_class_name(self, class_name: str):
        self.class_name = class_name
        return self

    def set_label_width(self, label_width: int):
        self.label_width = label_width
        return self

    def set_span(self, span: int):
        self.span = span
        return self

    def set_split(self, show_hidden_num: bool):
        self.show_hidden_num = show_hidden_num
        return self

    def set_export_text(self, export_text: str):
        self.export_text = export_text
        return self

    def set_export_api(self, export_api: str):
        self.export_api = export_api
        return self

    def set_items(self, item: Any):
        self.items.append(item)
        return self
