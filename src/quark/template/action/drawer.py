from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from quark_go_v3 import Context, Action


@dataclass
class Drawer(Action):
    """
    表示一个抽屉式弹窗组件，支持配置宽度和关闭时的行为。
    """
    width: int = 520  # 抽屉弹出层宽度，默认值为 520
    destroy_on_close: bool = False  # 关闭时销毁弹出层里的子元素，默认为 False

    def new(self, ctx: Context) -> "Drawer":
        """
        初始化方法，设置默认属性值。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            Drawer: 返回当前实例。
        """
        self.action_type = "drawer"
        return self

    def content(self, ctx: Context) -> Optional[Any]:
        """
        获取抽屉内容，可以是任意类型的数据。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            Optional[Any]: 返回内容数据，可以为空。
        """
        return None

    def data(self, ctx: Context) -> Dict[str, Any]:
        """
        异步获取数据。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            dict: 返回数据字典。
        """
        return {}

    @property
    def get_width(self) -> int:
        """获取抽屉弹出层宽度"""
        return self.width

    @property
    def get_destroy_on_close(self) -> bool:
        """关闭时销毁 Modal 里的子元素"""
        return self.destroy_on_close

    def get_body(self, ctx: Context) -> Optional[Any]:
        """获取弹窗主体内容"""
        return self.content(ctx)

    def get_actions(self, ctx: Context) -> List[Any]:
        """
        获取弹窗行为按钮列表。

        Args:
            ctx (Context): Quark 上下文对象.

        Returns:
            list: 返回行为按钮列表。
        """
        return []