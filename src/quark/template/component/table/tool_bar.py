from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from element import Element


@dataclass
class ToolBar(Element):
    Title: Optional[str] = None
    SubTitle: Optional[str] = None
    Description: Optional[str] = None
    Search: Any = None
    Actions: Any = None
    Filter: Any = None
    MultipleLine: bool = False
    Menu: Any = None
    Tabs: Any = None

    def __post_init__(self):
        self.Component = "toolBar"
        self.set_key("toolBar", True)  # 对应 component.DEFAULT_CRYPT = true

    def set_style(self, style: Dict[str, Any]):
        self.Style = style
        return self

    def set_title(self, title: str):
        self.Title = title
        return self

    def set_sub_title(self, subtitle: str):
        self.SubTitle = subtitle
        return self

    def set_description(self, description: str):
        self.Description = description
        return self

    def set_search(self, search: Any):
        self.Search = search
        return self

    def set_action(self, callback: Any):
        # 由于 callback(p.action) 未实现，这里仅保留结构
        # 如果你有 action 的默认值或调用形式，可以添加进去
        return self

    def set_actions(self, actions: Any):
        self.Actions = actions
        return self

    def set_filter(self, filter_: Any):
        self.Filter = filter_
        return self

    def set_multiple_line(self, multiple_line: bool):
        self.MultipleLine = multiple_line
        return self

    def set_menu(self, menu: Any):
        self.Menu = menu
        return self

    def set_tabs(self, tabs: Any):
        self.Tabs = tabs
        return self
