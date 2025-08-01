from pydantic import model_validator
from typing import Union, List, Dict, Optional
from ..component import Component
from .item import Item


class Dropdown(Component):
    component: str = "dropdown"

    # 按钮文字
    label: Optional[Union[str, List[str]]] = None

    # 是否调整按钮为父元素宽度
    block: Optional[bool] = None

    # 是否为危险按钮
    danger: Optional[bool] = None

    # 按钮是否禁用
    disabled: Optional[bool] = None

    # 幽灵按钮，背景透明
    ghost: Optional[bool] = None

    # 按钮图标
    icon: Optional[Union[str, List[str]]] = None

    # 按钮形状
    shape: Optional[str] = None

    # 按钮大小
    size: Optional[str] = "default"

    # 按钮类型
    type: Optional[str] = "default"

    # 下拉框箭头是否显示
    arrow: Optional[bool] = None

    # 关闭后是否销毁 Dropdown
    destroy_popup_on_hide: Optional[bool] = None

    # 下拉菜单内容
    menu: Optional[Union[List[Item], str]] = None

    # 下拉根元素的类名称
    overlay_class_name: Optional[str] = None

    # 下拉根元素的样式
    overlay_style: Optional[Dict[str, str]] = None

    # 菜单弹出位置
    placement: Optional[str] = "bottomLeft"

    # 触发下拉的行为
    trigger: Optional[List[str]] = ["click"]

    # 菜单是否显示
    visible: Optional[bool] = None

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: Dict[str, str]) -> "Dropdown":
        """
        设置组件样式

        :param style: 样式字典
        :return: 返回当前组件实例
        """
        self.overlay_style = style
        return self

    def set_label(self, label: Union[str, List[str]]) -> "Dropdown":
        """
        设置按钮文字

        :param label: 按钮文字
        :return: 返回当前组件实例
        """
        self.label = label
        return self

    def set_block(self, block: bool) -> "Dropdown":
        """
        设置按钮宽度调整为其父宽度

        :param block: 是否为块级元素
        :return: 返回当前组件实例
        """
        self.block = block
        return self

    def set_danger(self, danger: bool) -> "Dropdown":
        """
        设置是否为危险按钮

        :param danger: 是否为危险按钮
        :return: 返回当前组件实例
        """
        self.danger = danger
        return self

    def set_disabled(self, disabled: bool) -> "Dropdown":
        """
        设置按钮是否禁用

        :param disabled: 是否禁用
        :return: 返回当前组件实例
        """
        self.disabled = disabled
        return self

    def set_ghost(self, ghost: bool) -> "Dropdown":
        """
        设置幽灵按钮，背景透明

        :param ghost: 是否为幽灵按钮
        :return: 返回当前组件实例
        """
        self.ghost = ghost
        return self

    def set_icon(self, icon: Union[str, List[str]]) -> "Dropdown":
        """
        设置按钮图标

        :param icon: 图标，可以是字符串或字符串列表
        :return: 返回当前组件实例
        """
        if isinstance(icon, str):
            self.icon = f"icon-{icon}"
        elif isinstance(icon, list) and len(icon) == 2:
            self.icon = [f"icon-{icon[0]}", f"icon-{icon[1]}"]
        return self

    def set_shape(self, shape: str) -> "Dropdown":
        """
        设置按钮形状

        :param shape: 按钮形状 (circle | round)
        :return: 返回当前组件实例
        """
        self.shape = shape
        return self

    def set_type(self, button_type: str, danger: bool = False) -> "Dropdown":
        """
        设置按钮类型

        :param button_type: 按钮类型
        :param danger: 是否为危险按钮
        :return: 返回当前组件实例
        """
        self.type = button_type
        self.danger = danger
        return self

    def set_size(self, size: str) -> "Dropdown":
        """
        设置按钮大小

        :param size: 按钮大小 (large | middle | small | default)
        :return: 返回当前组件实例
        """
        self.size = size
        return self

    def set_arrow(self, arrow: bool) -> "Dropdown":
        """
        设置下拉框箭头是否显示

        :param arrow: 是否显示箭头
        :return: 返回当前组件实例
        """
        self.arrow = arrow
        return self

    def set_destroy_popup_on_hide(self, destroy_popup_on_hide: bool) -> "Dropdown":
        """
        设置关闭后是否销毁 Dropdown

        :param destroy_popup_on_hide: 是否销毁
        :return: 返回当前组件实例
        """
        self.destroy_popup_on_hide = destroy_popup_on_hide
        return self

    def set_menu(self, menu: Union[List[Item], str]) -> "Dropdown":
        """
        设置菜单内容

        :param menu: 菜单，可以是列表或字符串
        :return: 返回当前组件实例
        """
        self.menu = menu
        return self

    def set_overlay_class_name(self, overlay_class_name: str) -> "Dropdown":
        """
        设置下拉根元素的类名称

        :param overlay_class_name: 类名称
        :return: 返回当前组件实例
        """
        self.overlay_class_name = overlay_class_name
        return self

    def set_overlay_style(self, overlay_style: Dict[str, str]) -> "Dropdown":
        """
        设置下拉根元素的样式

        :param overlay_style: 样式字典
        :return: 返回当前组件实例
        """
        self.overlay_style = overlay_style
        return self

    def set_placement(self, placement: str) -> "Dropdown":
        """
        设置菜单弹出位置

        :param placement: 菜单弹出位置
        :return: 返回当前组件实例
        """
        self.placement = placement
        return self

    def set_trigger(self, trigger: List[str]) -> "Dropdown":
        """
        设置触发下拉的行为

        :param trigger: 触发行为 (click | hover | contextMenu)
        :return: 返回当前组件实例
        """
        self.trigger = trigger
        return self

    def set_visible(self, visible: bool) -> "Dropdown":
        """
        设置菜单是否显示

        :param visible: 是否显示菜单
        :return: 返回当前组件实例
        """
        self.visible = visible
        return self
