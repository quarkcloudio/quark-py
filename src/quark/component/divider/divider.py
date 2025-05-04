from pydantic import model_validator, field_validator
from typing import Any, Dict, Optional
from ..component import Component

class Divider(Component):
    component: str = "divider"
    dashed: bool = False
    orientation: str = "center"
    plain: bool = False
    type: str = "horizontal"
    body: Optional[Any] = None

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

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self
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