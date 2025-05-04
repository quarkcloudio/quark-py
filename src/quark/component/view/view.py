from pydantic import BaseModel
from typing import Any, Dict

# 模拟 component.Element
class Element(BaseModel):
    component: str = ""
    key: str = ""
    crypt: bool = False
    style: Dict[str, Any] = {}

    def set_key(self, key: str, crypt: bool) -> 'Element':
        self.key = key
        self.crypt = crypt
        return self


class Component(BaseModel):
    element: Element = Element()
    body: Any = None

    # 初始化组件
    @classmethod
    def new(cls) -> 'Component':
        return cls().init()

    # 初始化
    def init(self) -> 'Component':
        self.element.component = "view"
        self.element.set_key("DEFAULT_KEY", False)
        return self

    # Set style.
    def set_style(self, style: Dict[str, Any]) -> 'Component':
        self.element.style = style
        return self

    # 容器控件里面的内容
    def set_body(self, body: Any) -> 'Component':
        self.body = body
        return self