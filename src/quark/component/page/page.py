from pydantic import Field, model_validator
from typing import Any, Dict, Optional
from ..component import Component

class Page(Component):
    component: str = Field(default="page")
    title: str = Field(..., description="标题")
    body: Any = Field(..., description="内容")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key("page")
        return self

    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_title(self, title: str):
        # 设置标题
        self.title = title
        return self

    def set_body(self, body: Any):
        # 设置内容
        self.body = body
        return self