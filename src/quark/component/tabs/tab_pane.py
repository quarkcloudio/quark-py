from pydantic import model_validator
from typing import Any, Dict
from ..component import Component

class TabPane(Component):
    title: str = None
    body: Any = None
    component: str = "tabPane"

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

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