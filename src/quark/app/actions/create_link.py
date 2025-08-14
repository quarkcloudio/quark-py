from quark import Request
from quark.template.action import Link


class CreateLink(Link):

    def __init__(self, title: str = ""):

        # 文字
        self.name = f"创建{title}"

        # 类型
        self.type = "primary"

        # 图标
        self.icon = "plus-circle"

        # 设置只在索引页显示
        self.set_only_on_index(True)

    async def get_href(self, request: Request) -> str:
        return "#/layout/index?api=" + request.url.path.replace("/index", "/create")
