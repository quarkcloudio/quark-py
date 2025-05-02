from dataclasses import dataclass
from typing import Any
from quark_go_v3 import Context, Action


@dataclass
class Link(Action):
    """
    表示一个链接行为组件，用于页面跳转。
    """
    href: str = ""  # 获取跳转链接，默认为空字符串
    target: str = "_self"  # 相当于 a 链接的 target 属性，href 存在时生效，默认为 _self

    def new(self, ctx: Context) -> "Link":
        """
        初始化方法，设置默认属性值。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            Link: 返回当前实例。
        """
        self.action_type = "link"
        self.target = "_self"
        return self

    def get_href(self, ctx: Context) -> str:
        """
        获取跳转链接地址。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            str: 返回链接地址。
        """
        return self.href

    def get_target(self, ctx: Context) -> str:
        """
        获取链接打开方式，相当于 a 标签的 target 属性。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            str: 返回 target 值，如 _self、_blank 等。
        """
        return self.target