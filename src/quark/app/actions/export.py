from typing import Any, Optional


class ExportAction:
    def __init__(self, name: Optional[str] = None):
        self.name = name or "导出"
        self.type = "link"
        self.size = "small"
        self.target = "_blank"
        self.only_on_index_table_row = True

    def init(self, ctx) -> Any:
        # 这里可以根据需要，添加初始化逻辑
        self.type = "link"
        self.size = "small"
        self.target = "_blank"
        self.only_on_index_table_row = True
        return self

    def get_href(self, ctx) -> str:
        # ctx.Path() 类似获取当前路径，ctx.Token() 获取token
        path = ctx.Path()
        token = ctx.Token()
        # 替换路径中的 /index 为 /export?id=${id}&token=xxx
        # 其中 ${id} 在前端会自动替换，后端不用处理
        href = path.replace("/index", f"/export?id=${{id}}&token={token}")
        return href
