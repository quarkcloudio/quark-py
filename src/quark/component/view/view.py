from pydantic import BaseModel
from typing import Any, Dict
from ..component import Component

class View(Component):
    body: Any = None

    # 初始化组件
    @classmethod
    def new(cls) -> 'View':
        return cls().init()

    # 初始化
    def init(self) -> 'View':
        self.element.component = "view"
        self.element.set_key("DEFAULT_KEY", False)
        return self

    # Set style.
    def set_style(self, style: Dict[str, Any]) -> 'View':
        self.element.style = style
        return self

    # 容器控件里面的内容
    def set_body(self, body: Any) -> 'View':
        self.body = body
        return self