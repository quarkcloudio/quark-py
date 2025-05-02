from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Union
from quark_go_v3 import Context, Action, Resourcer
from quark_go_v3.component.menu import Menu


@dataclass
class Dropdown(Action):
    """
    表示一个下拉菜单组件，支持配置触发方式、位置、样式等。
    """
    arrow: bool = False  # 是否显示箭头图标，默认不显示
    placement: str = "bottomLeft"  # 菜单弹出位置，默认为 bottomLeft
    trigger: List[str] = ("hover",)  # 触发下拉的行为，默认为 ["hover"]
    overlay_style: Dict[str, Any] = None  # 下拉根元素的样式，默认为空字典
    actions: List[Any] = ()  # 下拉菜单行为列表

    def __post_init__(self):
        if self.overlay_style is None:
            self.overlay_style = {}

    def new(self, ctx: Context) -> "Dropdown":
        """
        初始化方法，设置默认属性值。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            Dropdown: 返回当前实例。
        """
        self.action_type = "dropdown"
        self.placement = "bottomLeft"
        self.trigger = ["hover"]
        return self

    def get_arrow(self) -> bool:
        """获取是否显示箭头图标"""
        return self.arrow

    def get_placement(self) -> str:
        """获取菜单弹出位置：bottomLeft, bottomCenter, bottomRight 等"""
        return self.placement

    def get_trigger(self) -> List[str]:
        """获取触发下拉的行为，移动端不支持 hover"""
        return self.trigger

    def get_overlay_style(self) -> Dict[str, Any]:
        """获取下拉根元素的样式"""
        return self.overlay_style

    def get_menu(self, ctx: Context) -> Menu:
        """
        构建下拉菜单内容。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            Menu: 返回构建好的菜单组件。
        """
        items = []

        # 获取模板实例
        template: Resourcer = ctx.template

        # 获取行为
        actions = self.get_actions()

        # 解析行为并构建菜单项
        for action in actions:
            action_instance = action()
            action_instance.new(ctx)
            action_instance.init(ctx)
            items.append(template.build_action(ctx, action_instance))

        return Menu().init().set_items(items)

    def set_actions(self, actions: List[Any]) -> "Dropdown":
        """
        设置下拉菜单行为。

        Args:
            actions (List[Any]): 行为列表。

        Returns:
            Dropdown: 返回当前实例。
        """
        self.actions = actions
        return self

    def get_actions(self) -> List[Any]:
        """
        获取下拉菜单行为。

        Returns:
            List[Any]: 返回行为列表。
        """
        return self.actions