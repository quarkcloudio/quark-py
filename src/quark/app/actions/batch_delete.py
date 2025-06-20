from typing import List
from fastapi import Request
from app.core.context import Context
from app.template.admin.resource.actions import Action


class BatchDeleteAction(Action):
    def __init__(self, name: str = "批量删除"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.with_confirm(
            "确定要删除吗？", "删除后数据将无法恢复，请谨慎操作！", "modal"
        )
        self.set_only_on_index_table_alert(True)

    def get_api_params(self) -> List[str]:
        return ["id"]

    async def handle(self, ctx: Context, db_model):
        try:
            await db_model.all().delete()
            return ctx.cjson_ok("操作成功")
        except Exception as e:
            return ctx.cjson_error(str(e))
