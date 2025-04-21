from dataclasses import dataclass, field
from typing import Any, List, Dict


@dataclass
class Search:
    # 属性定义
    filter_type: str = ""
    search_text: str = ""
    reset_text: str = ""
    submit_text: str = ""
    label_width: int = 0
    span: int = 0
    class_name: str = ""
    default_collapsed: bool = False
    show_hidden_num: bool = False
    export_text: str = ""
    export_api: str = ""
    items: List[Any] = field(default_factory=list)
    style: Dict[str, Any] = field(default_factory=dict)

    # 固定字段，模拟组件元素
    component: str = field(init=False)
    key: str = field(init=False)
    crypt: str = field(init=False)

    def __post_init__(self):
        self.component = "search"
        self.default_collapsed = True
        self.reset_text = "重置"
        self.search_text = "查询"
        self.key = "defaultKey"
        self.crypt = "defaultCrypt"

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