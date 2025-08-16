from typing import Any, List

from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.template.action import Action


class BatchDeleteRole(Action):

    def __init__(self):
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

    async def handle(self, request: Request, query: QuerySet) -> Any:
        id_param = request.query_params.get("id")

        if not id_param:
            return Message.error("参数错误")

        try:
            ids = id_param.split(",")
            id_list = [int(i) for i in ids]

            # 删除角色
            await query.filter(id__in=id_list).delete()

            # 清理 casbin 权限
            # casbin_service = CasbinService()
            # for id_int in id_list:
            #     await casbin_service.remove_role_menu_and_permissions(id_int)

            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
