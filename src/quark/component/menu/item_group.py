from ..component import Component
from typing import Any

class ItemGroup(Component):
    title: str
    items: Any

    # 初始化
    def init(self) -> 'ItemGroup':
        self.element.component = "menuItemGroup"
        self.element.set_key("DEFAULT_KEY", False)
        return self

    # 设置收缩时展示的悬浮标题
    def set_title(self, title: str) -> 'ItemGroup':
        self.title = title
        return self

    # 设置按钮文字
    def set_items(self, items: Any) -> 'ItemGroup':
        self.items = items
        return self