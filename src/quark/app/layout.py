from quark import Layout, Request


class Index(Layout):
    """后台布局"""

    async def init(self, request: Request):
        return self
