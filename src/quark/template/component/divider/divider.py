from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from ..component.element import Element

@dataclass
class Component(Element):
    dashed: bool = False
    orientation: str = ""
    plain: bool = False
    type: str = ""
    body: Optional[Any] = None

    def __post_init__(self):
        self.component = "divider"
        self.type = "horizontal"
        self.orientation = "center"
        self.set_key("", True)

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_dashed(self, dashed: bool):
        self.dashed = dashed
        return self

    def set_orientation(self, orientation: str):
        limits = ["left", "right", "center"]
        if orientation not in limits:
            raise ValueError("Argument must be in 'left', 'right', 'center'!")
        self.orientation = orientation
        return self

    def set_plain(self, plain: bool):
        self.plain = plain
        return self

    def set_type(self, divider_type: str):
        limits = ["vertical", "horizontal"]
        if divider_type not in limits:
            raise ValueError("Argument must be in 'vertical', 'horizontal'!")
        self.type = divider_type
        return self

    def set_body(self, body: Any):
        self.body = body
        return self