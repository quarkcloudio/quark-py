from pydantic import BaseModel, Field, field_validator
from typing import Any, Dict
from ..component.element import Element

class TabPane(BaseModel, Element):
    title: str = ""
    body: Any = None
    component: str = "tabPane"
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

    def set_title(self, title: str):
        self.title = title
        return self

    def set_body(self, body: Any):
        self.body = body
        return self