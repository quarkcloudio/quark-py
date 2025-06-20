from typing import List
from app.core.context import Context
from app.template.admin.resource.actions import Action


class DeleteSpecialAction(Action):
    def __init__(self, name=None):
        super().__init__()
        # 名称支持动态表达式，Python中可用字符串或模板渲染实现
        self.name = name or "<%= (id==1 ? '' : '删除') %>"
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.with_confirm(
            "确定要删除吗？", "删除后数据将无法恢复，请谨慎操作！", "modal"
        )
        self.set_only_on_index_table_row(True)
        self.set_api_params(["id"])

    def get_api_params(self) -> List[str]:
        return ["id"]

    async def handle(self, ctx: Context, query) -> any:
        try:
            await query.delete()
            return ctx.cjson_ok("操作成功")
        except Exception as e:
            return ctx.cjson_error(str(e))
