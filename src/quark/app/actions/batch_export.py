from quark import Request
from quark.services.auth import AuthService
from quark.template.action import Link


class BatchExport(Link):

    def __init__(self, name: str = "批量导出"):
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.target = "_blank"
        self.set_only_on_index_table_alert(True)
        self.with_confirm("确定要导出数据吗？", "导出数据可能会等待时间较长！", "modal")

    async def get_href(self, request: Request) -> str:
        path = request.url.path.replace("/index", "")
        token = AuthService(request).get_token()
        return f"{path}/export?id=${{id}}&token={token}"
