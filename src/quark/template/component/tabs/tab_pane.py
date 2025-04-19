from dataclasses import dataclass, field, asdict
from typing import Any, Dict
from ..component.element import Element

@dataclass
class TabPane(Element):
    title: str = ""
    body: Any = None

    def __post_init__(self):
        self.component = "tabPane"
        self.set_key("", crypt=True)

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_body(self, body: Any):
        self.body = body
        return self
