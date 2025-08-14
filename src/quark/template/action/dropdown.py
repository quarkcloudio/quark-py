from typing import Any, Dict, List

from quark import Request

from ...component.menu.menu import Menu
from ..resolves_actions import ResolvesActions
from .action import Action


class Dropdown(Action):
    """
    表示一个下拉菜单组件，支持配置触发方式、位置、样式等。
    """

    # 是否显示箭头图标，默认不显示
    arrow: bool = False

    # 下拉菜单类型
    action_type: str = "dropdown"

    # 菜单弹出位置，默认为 bottomLeft
    placement: str = "bottomLeft"

    # 触发下拉的行为，默认为 ["hover"]
    trigger: List[str] = ["hover"]

    # 下拉根元素的样式，默认为空字典
    overlay_style: Dict[str, Any] = None

    # 下拉菜单行为列表
    actions: List[Any] = None

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

    async def get_menu(self, request: Request) -> Menu:
        """
        构建下拉菜单内容
        """
        items = []

        # 获取行为
        actions = self.get_actions()

        # 解析行为并构建菜单项
        for action in actions:
            items.append(await ResolvesActions(request).build_action(action))

        return Menu().set_items(items)

    def set_actions(self, actions: List[Any]) -> Any:
        """
        设置下拉菜单行为
        """
        self.actions = actions
        return self

    def get_actions(self) -> List[Any]:
        """
        获取下拉菜单行为
        """
        return self.actions
