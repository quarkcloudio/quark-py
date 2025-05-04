from pydantic import BaseModel
from typing import Any, Optional, Callable
from ..component import Component

# 模拟 component.Element
class Element(BaseModel):
    component: str = ""
    key: str = ""
    crypt: bool = False

    def set_key(self, key: str, crypt: bool) -> 'Element':
        self.key = key
        self.crypt = crypt
        return self


# 模拟 Divider
class Divider(BaseModel):
    element: Element = Element()

    def init(self) -> 'Divider':
        self.element.component = "menuDivider"
        self.element.set_key("DEFAULT_KEY", False)
        return self


# 模拟 ItemGroup
class ItemGroup(BaseModel):
    element: Element = Element()
    title: str = ""
    items: Any = None

    def init(self) -> 'ItemGroup':
        self.element.component = "menuItemGroup"
        self.element.set_key("DEFAULT_KEY", False)
        return self

    def set_title(self, title: str) -> 'ItemGroup':
        self.title = title
        return self

    def set_items(self, items: Any) -> 'ItemGroup':
        self.items = items
        return self


# 模拟 Item
class Item(BaseModel):
    element: Element = Element()
    label: str = ""
    title: str = ""

    def init(self) -> 'Item':
        self.element.component = "menuItem"
        self.element.set_key("DEFAULT_KEY", False)
        return self

    def set_label(self, label: str) -> 'Item':
        self.label = label
        return self

    def set_title(self, title: str) -> 'Item':
        self.title = title
        return self


# 模拟 SubMenu
class SubMenu(BaseModel):
    element: Element = Element()
    title: str = ""
    items: Any = None

    def init(self) -> 'SubMenu':
        self.element.component = "menuSubMenu"
        self.element.set_key("DEFAULT_KEY", False)
        return self

    def set_title(self, title: str) -> 'SubMenu':
        self.title = title
        return self

    def set_items(self, items: Any) -> 'SubMenu':
        self.items = items
        return self


class Menu(Component):
    element: Element = Element()
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

    # 初始化组件
    @classmethod
    def new(cls) -> 'Component':
        return cls().init()

    # 获取Divider
    @staticmethod
    def new_divider() -> Divider:
        return Divider().init()

    # 获取ItemGroup
    @staticmethod
    def new_item_group() -> ItemGroup:
        return ItemGroup().init()

    # 获取Item
    @staticmethod
    def new_item() -> Item:
        return Item().init()

    # 获取SubMenu
    @staticmethod
    def new_sub_menu() -> SubMenu:
        return SubMenu().init()

    # 初始化
    def init(self) -> 'Component':
        self.element.component = "menu"
        self.inline_indent = 24
        self.mode = "vertical"
        self.sub_menu_close_delay = 0.1
        self.sub_menu_open_delay = 0
        self.theme = "light"
        self.trigger_sub_menu_action = "hover"
        self.element.set_key("DEFAULT_KEY", False)
        return self

    # 初始展开的 SubMenu 菜单项 key 数组
    def set_default_open_keys(self, default_open_keys: Any) -> 'Component':
        self.default_open_keys = default_open_keys
        return self

    # 初始选中的菜单项 key 数组
    def set_default_selected_keys(self, default_selected_keys: Any) -> 'Component':
        self.default_selected_keys = default_selected_keys
        return self

    # inline 时菜单是否收起状态
    def set_inline_collapsed(self, inline_collapsed: bool) -> 'Component':
        self.inline_collapsed = inline_collapsed
        return self

    # inline 模式的菜单缩进宽度
    def set_inline_indent(self, inline_indent: int) -> 'Component':
        self.inline_indent = inline_indent
        return self

    # 菜单类型，现在支持垂直、水平、和内嵌模式三种,vertical | horizontal | inline
    def set_mode(self, mode: str) -> 'Component':
        self.mode = mode
        return self

    # 是否允许多选
    def set_multiple(self, multiple: bool) -> 'Component':
        self.multiple = multiple
        return self

    # 是否允许选中
    def set_selectable(self, selectable: bool) -> 'Component':
        self.selectable = selectable
        return self

    # 用户鼠标离开子菜单后关闭延时，单位：秒
    def set_sub_menu_close_delay(self, sub_menu_close_delay: float) -> 'Component':
        self.sub_menu_close_delay = sub_menu_close_delay
        return self

    # 主题颜色,light | dark
    def set_theme(self, theme: str) -> 'Component':
        self.theme = theme
        return self

    # SubMenu 展开/关闭的触发行为,hover | click
    def set_trigger_sub_menu_action(self, trigger_sub_menu_action: str) -> 'Component':
        self.trigger_sub_menu_action = trigger_sub_menu_action
        return self

    # 设置菜单项
    def set_items(self, items: Any) -> 'Component':
        self.items = items
        return self

    # 菜单分隔符
    def divider(self) -> Divider:
        return Divider().init()

    # 菜单分组
    def item_group(self, title: str, items: Any) -> ItemGroup:
        return ItemGroup().init().set_title(title).set_items(items)

    # 菜单项
    def item(self, label: str, title: str) -> Item:
        return Item().init().set_label(label).set_title(title)

    # 子菜单
    def sub_menu(self, title: str, items: Any) -> SubMenu:
        return SubMenu().init().set_title(title).set_items(items)