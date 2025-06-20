from app.core.context import Context
from app.template.admin.resource.actions import Link


class BatchExportAction(Link):
    def __init__(self, name: str = "批量导出"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.target = "_blank"
        self.set_only_on_index_table_alert(True)
        self.with_confirm("确定要导出数据吗？", "导出数据可能会等待时间较长！", "modal")

    def get_href(self, ctx: Context) -> str:
        # 构造链接，把 /index 替换为 /export，并拼接 ID 和 token
        path = ctx.path.replace("/index", "")
        return f"{path}/export?id=${{id}}&token={ctx.token}"
