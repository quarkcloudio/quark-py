from typing import List
from app.core.context import Context
from app.template.admin.resource.actions import Action


class ChangeStatusAction(Action):
    def __init__(self, name: str = "<%= (status==1 ? '禁用' : '启用') %>"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.set_only_on_index_table_row(True)
        self.with_confirm(
            "确定要<%= (status==1 ? '禁用' : '启用') %>数据吗？", "", "pop"
        )

    def get_api_params(self) -> List[str]:
        return ["id", "status"]

    async def handle(self, ctx: Context, db_model):
        status = ctx.query.get("status")
        if status is None:
            return ctx.cjson_error("参数错误")

        try:
            # 切换状态逻辑
            field_status = 0 if status == "1" else 1

            id_param = ctx.query.get("id")
            if not id_param:
                return ctx.cjson_error("缺少 ID 参数")

            ids = [int(i) for i in id_param.split(",")]
            await db_model.filter(id__in=ids).update(status=field_status)

            return ctx.cjson_ok("操作成功")
        except Exception as e:
            return ctx.cjson_error(str(e))
