from typing import List
from app.core.context import Context
from app.template.admin.resource.actions import Action


class BatchDisableAction(Action):
    def __init__(self, name: str = "批量禁用"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.set_only_on_index_table_alert(True)
        self.with_confirm(
            "确定要禁用吗？", "禁用后数据将无法使用，请谨慎操作！", "modal"
        )

    def get_api_params(self) -> List[str]:
        return ["id"]

    async def handle(self, ctx: Context, db_model):
        id_param = ctx.query.get("id")
        if not id_param:
            return ctx.cjson_error("参数错误")

        try:
            ids = [int(i) for i in id_param.split(",")]

            # 更新 status 字段为 0
            await db_model.filter(id__in=ids).update(status=0)

            return ctx.cjson_ok("操作成功")
        except Exception as e:
            return ctx.cjson_error(str(e))
