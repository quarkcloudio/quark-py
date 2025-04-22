from pydantic import Field, field_validator
from typing import Any, Dict, Optional
from ..component.element import Element

class Component(Element):
    centered: bool = False
    default_active_key: str = ""
    size: str = "default"
    tab_bar_extra_content: Any = None
    tab_bar_gutter: int = 35
    tab_bar_style: Optional[Dict[str, Any]] = Field(default_factory=dict)
    tab_position: str = "top"
    type: str = "line"
    tab_panes: Any = None
    component: str = "tabs"
    component_key: str = ""

    crypt: bool = Field(default=True, exclude=True)

    @field_validator('component_key', mode="before")
    def set_key(cls, v, values):
        crypt = values.get('crypt', False)
        return v if not crypt else cls._make_hex(v)

    @staticmethod
    def _make_hex(key: str) -> str:
        return key.encode().hex()

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