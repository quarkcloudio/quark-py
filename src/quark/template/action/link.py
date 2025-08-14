from quark import Request

from .action import Action


class Link(Action):
    """
    表示一个链接行为组件，用于页面跳转。
    """

    # 行为类型
    action_type: str = "link"

    # 获取跳转链接，默认为空字符串
    href: str = ""

    # 相当于 a 链接的 target 属性，href 存在时生效，默认为 _self
    target: str = "_self"

    async def get_href(self, request: Request) -> str:
        """
        获取跳转链接地址
        """
        return self.href

    async def get_target(self, request: Request) -> str:
        """
        获取链接打开方式，相当于 a 标签的 target 属性
        """
        return self.target
