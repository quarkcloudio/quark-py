from pydantic import model_validator
from typing import Any
from ..component import Component


class SubMenu(Component):
    component: str = "menuSubMenu"
    disabled: bool = False
    icon: str = ""
    popup_class_name: str = ""
    popup_offset: Any = None
    title: str = ""
    items: Any = None

    @model_validator(mode="after")
    def init(self):
        self.set_key("DEFAULT_KEY", False)
        return self

    # 是否禁用
    def set_disabled(self, disabled: bool) -> "SubMenu":
        self.disabled = disabled
        return self

    # 菜单图标
    def set_icon(self, icon: str) -> "SubMenu":
        self.icon = icon
        return self

    # 子菜单样式，mode="inline" 时无效
    def set_popup_class_name(self, popup_class_name: str) -> "SubMenu":
        self.popup_class_name = popup_class_name
        return self

    # 子菜单偏移量，mode="inline" 时无效
    def set_popup_offset(self, popup_offset: Any) -> "SubMenu":
        self.popup_offset = popup_offset
        return self

    # 子菜单项值
    def set_title(self, title: str) -> "SubMenu":
        self.title = title
        return self

    # 菜单项
    def set_items(self, items: Any) -> "SubMenu":
        self.items = items
        return self
