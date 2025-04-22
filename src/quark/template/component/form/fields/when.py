from pydantic import Field, field_validator
from typing import Any, List, Optional
from ...component.element import Element

class Item(Element):
    component: str = ""          # 组件名称
    condition: str = ""           # 条件：js表达式语句
    condition_name: str = ""      # 需要对比的字段名称
    condition_operator: str = ""  # 操作符，= <>
    option: Optional[Any] = None # 条件符合的属性值
    body: Optional[Any] = None    # 内容

class Component(Element):
    component_key: str = ""
    component: str = ""
    items: List[Item] = Field(default_factory=list)

    crypt: bool = Field(default=False, exclude=True)

    @field_validator('component', mode="before")
    def set_component(cls, v):
        return "when"

    @field_validator('component_key', mode="before")
    def set_key(cls, v, values):
        crypt = values.get('crypt', False)
        return v if not crypt else cls._make_hex(v)

    @staticmethod
    def _make_hex(key: str) -> str:
        return key.encode().hex()

    # 设置When组件中需要解析的元素
    def set_items(self, items: List[Item]) -> 'Component':
        self.items = items
        return self