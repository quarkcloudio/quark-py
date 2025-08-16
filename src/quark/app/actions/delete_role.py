from typing import Any, List

from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.template.action import Action


class DeleteRole(Action):

    def __init__(self):
        self.name = "删除"
        self.type = "link"
        self.size = "small"
        self.reload = "table"
        self.set_only_on_index_table_row(True)
        self.with_confirm(
            "确定要删除吗？", "删除后数据将无法恢复，请谨慎操作！", "modal"
        )

    def get_api_params(self) -> List[str]:
        return ["id"]

    async def handle(self, request: Request, query: QuerySet) -> Any:
        id_str = request.query_params.get("id")
        if not id_str:
            return Message.error("参数错误")

        ids = id_str.split(",")
        try:
            ids_int = [int(i) for i in ids]
        except ValueError as e:
            return Message.error(f"参数转换错误: {str(e)}")

        try:
            # 先删除数据库中的记录
            await query.filter(id__in=ids_int).delete()

            # 清理 Casbin 中对应角色的权限
            # casbin_service = CasbinService()
            # for role_id in ids_int:
            #     await casbin_service.remove_role_menu_and_permissions(role_id)

            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
