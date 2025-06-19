from typing import List, Dict, Any, Optional
from .action import Action
from fastapi import Request


class Drawer(Action):
    """
    表示一个抽屉式弹窗组件，支持配置宽度和关闭时的行为。
    """

    # 抽屉弹出层宽度，默认值为 520
    width: int = 520

    # 关闭时销毁弹出层里的子元素，默认为 False
    destroy_on_close: bool = False

    def __init__(self):
        self.action_type = "drawer"

    def content(self, request: Request) -> Optional[Any]:
        """
        获取抽屉内容，可以是任意类型的数据
        """
        return None

    def data(self, request: Request) -> Dict[str, Any]:
        """
        异步获取数据
        """
        return {}

    def get_width(self) -> int:
        """获取抽屉弹出层宽度"""
        return self.width

    def get_destroy_on_close(self) -> bool:
        """关闭时销毁 Modal 里的子元素"""
        return self.destroy_on_close

    def get_body(self, request: Request) -> Optional[Any]:
        """获取弹窗主体内容"""
        return self.content(request)

    def get_actions(self, request: Request) -> List[Any]:
        """
        获取弹窗行为按钮列表
        """
        return []
