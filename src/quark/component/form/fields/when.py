from pydantic import Field, model_validator
from typing import Any, List, Optional
from ...component import Component

class Item(Component):
    component: str = "whenItem"     # 组件名称
    condition: str = None           # 条件：js表达式语句
    condition_name: str = None      # 需要对比的字段名称
    condition_operator: str = None  # 操作符，= <>
    option: Optional[Any] = None    # 条件符合的属性值
    body: Optional[Any] = None      # 内容

class When(Component):
    component: str = "when"
    items: List[Item] = Field(default_factory=list)

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    # 设置When组件中需要解析的元素
    def set_items(self, items: List[Item]) -> 'When':
        self.items = items
        return self