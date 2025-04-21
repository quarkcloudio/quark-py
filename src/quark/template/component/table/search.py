from dataclasses import dataclass, field
from typing import Any, List, Dict


@dataclass
class Search:
    # 属性定义
    FilterType: str = ""
    SearchText: str = ""
    ResetText: str = ""
    SubmitText: str = ""
    LabelWidth: int = 0
    Span: int = 0
    ClassName: str = ""
    DefaultCollapsed: bool = False
    ShowHiddenNum: bool = False
    ExportText: str = ""
    ExportApi: str = ""
    Items: List[Any] = field(default_factory=list)
    Style: Dict[str, Any] = field(default_factory=dict)

    # 固定字段，模拟组件元素
    Component: str = field(init=False)
    Key: str = field(init=False)
    Crypt: str = field(init=False)

    def __post_init__(self):
        self.Component = "search"
        self.DefaultCollapsed = True
        self.ResetText = "重置"
        self.SearchText = "查询"
        self.Key = "defaultKey"
        self.Crypt = "defaultCrypt"

    def set_style(self, style: Dict[str, Any]):
        self.Style = style
        return self

    def set_filter_type(self, filter_type: str):
        self.FilterType = filter_type
        return self

    def set_collapsed(self, collapsed: bool):
        self.DefaultCollapsed = collapsed
        return self

    def set_search_text(self, search_text: str):
        self.SearchText = search_text
        return self

    def set_reset_text(self, reset_text: str):
        self.ResetText = reset_text
        return self

    def set_submit_text(self, submit_text: str):
        self.SubmitText = submit_text
        return self

    def set_class_name(self, class_name: str):
        self.ClassName = class_name
        return self

    def set_label_width(self, label_width: int):
        self.LabelWidth = label_width
        return self

    def set_span(self, span: int):
        self.Span = span
        return self

    def set_split(self, show_hidden_num: bool):
        self.ShowHiddenNum = show_hidden_num
        return self

    def set_export_text(self, export_text: str):
        self.ExportText = export_text
        return self

    def set_export_api(self, export_api: str):
        self.ExportApi = export_api
        return self

    def set_items(self, item: Any):
        self.Items.append(item)
        return self
