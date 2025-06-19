from pydantic import model_validator
from typing import Any
from ..component import Component
from .item import Item
from .sub_menu import SubMenu
from .item_group import ItemGroup
from .divider import Divider


class Menu(Component):
    component: str = "menu"
    default_open_keys: Any = None
    default_selected_keys: Any = None
    inline_collapsed: bool = False
    inline_indent: int = 24
    mode: str = "vertical"
    multiple: bool = False
    selectable: bool = True
    sub_menu_close_delay: float = 0.1
    sub_menu_open_delay: float = 0
    theme: str = "light"
    trigger_sub_menu_action: str = "hover"
    items: Any = None

    @model_validator(mode="after")
    def init(self):
        self.set_key("DEFAULT_KEY", False)
        return self

    # 初始展开的 SubMenu 菜单项 key 数组
    def set_default_open_keys(self, default_open_keys: Any) -> "Component":
        self.default_open_keys = default_open_keys
        return self

    # 初始选中的菜单项 key 数组
    def set_default_selected_keys(self, default_selected_keys: Any) -> "Component":
        self.default_selected_keys = default_selected_keys
        return self

    # inline 时菜单是否收起状态
    def set_inline_collapsed(self, inline_collapsed: bool) -> "Component":
        self.inline_collapsed = inline_collapsed
        return self

    # inline 模式的菜单缩进宽度
    def set_inline_indent(self, inline_indent: int) -> "Component":
        self.inline_indent = inline_indent
        return self

    # 菜单类型，现在支持垂直、水平、和内嵌模式三种,vertical | horizontal | inline
    def set_mode(self, mode: str) -> "Component":
        self.mode = mode
        return self

    # 是否允许多选
    def set_multiple(self, multiple: bool) -> "Component":
        self.multiple = multiple
        return self

    # 是否允许选中
    def set_selectable(self, selectable: bool) -> "Component":
        self.selectable = selectable
        return self

    # 用户鼠标离开子菜单后关闭延时，单位：秒
    def set_sub_menu_close_delay(self, sub_menu_close_delay: float) -> "Component":
        self.sub_menu_close_delay = sub_menu_close_delay
        return self

    # 主题颜色,light | dark
    def set_theme(self, theme: str) -> "Component":
        self.theme = theme
        return self

    # SubMenu 展开/关闭的触发行为,hover | click
    def set_trigger_sub_menu_action(self, trigger_sub_menu_action: str) -> "Component":
        self.trigger_sub_menu_action = trigger_sub_menu_action
        return self

    # 设置菜单项
    def set_items(self, items: Any) -> "Component":
        self.items = items
        return self

    # 菜单分隔符
    def divider(self) -> Divider:
        return Divider()

    # 菜单分组
    def item_group(self, title: str, items: Any) -> ItemGroup:
        return ItemGroup().set_title(title).set_items(items)

    # 菜单项
    def item(self, label: str, title: str) -> Item:
        return Item().set_label(label).set_title(title)

    # 子菜单
    def sub_menu(self, title: str, items: Any) -> SubMenu:
        return SubMenu().set_title(title).set_items(items)
