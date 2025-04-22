from pydantic import Field, field_validator
from typing import Any, Dict, Optional
from ..component.element import Element

class Component(Element):
    dashed: bool = False
    orientation: str = "center"
    plain: bool = False
    type: str = "horizontal"
    body: Optional[Any] = None
    component: str = "divider"
    component_key: str = ""

    crypt: bool = Field(default=True, exclude=True)

    @field_validator('orientation')
    def validate_orientation(cls, v):
        limits = ["left", "right", "center"]
        if v not in limits:
            raise ValueError("Argument must be in 'left', 'right', 'center'!")
        return v

    @field_validator('type')
    def validate_type(cls, v):
        limits = ["vertical", "horizontal"]
        if v not in limits:
            raise ValueError("Argument must be in 'vertical', 'horizontal'!")
        return v

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

    def set_dashed(self, dashed: bool):
        self.dashed = dashed
        return self

    def set_orientation(self, orientation: str):
        self.orientation = orientation
        return self

    def set_plain(self, plain: bool):
        self.plain = plain
        return self

    def set_type(self, divider_type: str):
        self.type = divider_type
        return self

    def set_body(self, body: Any):
        self.body = body
        return self