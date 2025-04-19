from dataclasses import dataclass, field
from typing import Any, List, Optional

@dataclass
class Item:
    component: str = ""          # 组件名称
    condition: str = ""           # 条件：js表达式语句
    condition_name: str = ""      # 需要对比的字段名称
    condition_operator: str = ""  # 操作符，= <>
    option: Optional[Any] = None # 条件符合的属性值
    body: Optional[Any] = None    # 内容

@dataclass
class Component:
    component_key: str = ""  # 组件标识
    component: str = ""      # 组件名称
    items: List[Item] = field(default_factory=list)  # When组件中需要解析的元素

    def __post_init__(self):
        self.component = "when"
        self.set_key("", True)

    # 设置Key
    def set_key(self, key: str, crypt: bool) -> 'Component':
        self.component_key = key if not crypt else self._make_hex(key)
        return self

    def _make_hex(self, key: str) -> str:
        return key.encode().hex()

    # 设置When组件中需要解析的元素
    def set_items(self, items: List[Item]) -> 'Component':
        self.items = items
        return self