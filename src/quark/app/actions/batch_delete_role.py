from typing import List
from fastapi import Request
from pydantic import BaseModel
from app.core.context import Context  # 模拟 quark.Context
from app.services.casbin_service import CasbinService
from app.template.admin.resource.actions import Action


class BatchDeleteRoleAction(Action):

    def __init__(self):
        super().__init__()
        self.name = "批量删除"
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
        id_param = ctx.query.get("id")

        if not id_param:
            return ctx.cjson_error("参数错误")

        try:
            ids = id_param.split(",")
            id_list = [int(i) for i in ids]

            # 删除角色
            await db_model.filter(id__in=id_list).delete()

            # 清理 casbin 权限
            casbin_service = CasbinService()
            for id_int in id_list:
                await casbin_service.remove_role_menu_and_permissions(id_int)

            return ctx.cjson_ok("操作成功")
        except Exception as e:
            return ctx.cjson_error(str(e))
