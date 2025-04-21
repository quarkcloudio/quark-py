from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from ..component.element import Element


@dataclass
class ToolBar(Element):
    title: Optional[str] = None
    sub_title: Optional[str] = None
    description: Optional[str] = None
    search: Any = None
    actions: Any = None
    filter_: Any = None
    multiple_line: bool = False
    menu: Any = None
    tabs: Any = None

    def __post_init__(self):
        self.component = "toolBar"
        self.set_key("toolBar", True)  # 对应 component.DEFAULT_CRYPT = true

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_sub_title(self, subtitle: str):
        self.sub_title = subtitle
        return self

    def set_description(self, description: str):
        self.description = description
        return self

    def set_search(self, search: Any):
        self.search = search
        return self

    def set_action(self, callback: Any):
        # 由于 callback(p.action) 未实现，这里仅保留结构
        # 如果你有 action 的默认值或调用形式，可以添加进去
        return self

    def set_actions(self, actions: Any):
        self.actions = actions
        return self

    def set_filter(self, filter_: Any):
        self.filter_ = filter_
        return self

    def set_multiple_line(self, multiple_line: bool):
        self.multiple_line = multiple_line
        return self

    def set_menu(self, menu: Any):
        self.menu = menu
        return self

    def set_tabs(self, tabs: Any):
        self.tabs = tabs
        return self