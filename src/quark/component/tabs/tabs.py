from pydantic import Field, model_validator
from typing import Any, Dict, Optional
from ..component import Component

class Tabs(Component):
    centered: bool = False
    default_active_key: str = None
    size: str = "default"
    tab_bar_extra_content: Any = None
    tab_bar_gutter: int = 35
    tab_bar_style: Optional[Dict[str, Any]] = Field(default_factory=dict)
    tab_position: str = "top"
    type: str = "line"
    tab_panes: Any = None
    component: str = "tabs"

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self
    # 设置方法（链式调用）
    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_centered(self, centered: bool):
        self.centered = centered
        return self

    def set_default_active_key(self, key: str):
        self.default_active_key = key
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_tab_bar_extra_content(self, content: Any):
        self.tab_bar_extra_content = content
        return self

    def set_tab_bar_gutter(self, gutter: int):
        self.tab_bar_gutter = gutter
        return self

    def set_tab_bar_style(self, style: Dict[str, Any]):
        self.tab_bar_style = style
        return self

    def set_tab_position(self, position: str):
        self.tab_position = position
        return self

    def set_type(self, tab_type: str):
        self.type = tab_type
        return self

    def set_tab_panes(self, panes: Any):
        self.tab_panes = panes
        return self