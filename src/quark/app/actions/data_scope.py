from typing import Any, Dict, List

from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.component.form import field
from quark.component.form.fields.select import Option
from quark.component.form.rule import Rule
from quark.services.department import DepartmentService
from quark.services.role import RoleService
from quark.template.action import ModalForm


class DataScope(ModalForm):

    def __init__(self, name="数据权限"):
        self.name = name
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.set_only_on_index_table_row(True)
        self.set_api_params(["id", "name"])

    async def fields(self, request: Request) -> List[Any]:
        departments = DepartmentService().get_list()

        return [
            field.hidden("id", "ID"),
            field.text("name", "名称").set_disabled(True),
            field.select("data_scope", "数据范围")
            .set_options(
                [
                    Option(label="全部数据权限", value=1),
                    Option(label="自定数据权限", value=2),
                    Option(label="本部门数据权限", value=3),
                    Option(label="本部门及以下数据权限", value=4),
                    Option(label="仅本人数据权限", value=5),
                ]
            )
            .set_rules([Rule.required("请选择数据范围")])
            .set_default_value(1),
            field.dependency().set_when(
                "data_scope",
                2,
                lambda: [
                    field.tree("department_ids", "数据权限")
                    .set_default_expand_all(True)
                    .set_tree_data(departments, pid="pid", id="id", name="name")
                ],
            ),
        ]

    async def data(self, request: Request) -> Dict[str, Any]:
        id_str = request.query_params.get("id")
        if not id_str:
            return {}

        try:
            role_id = int(id_str)
        except ValueError:
            return {}

        role = RoleService().get_info_by_id(role_id)
        if not role:
            return {}

        # dept_ids = CasbinService().get_role_department_ids(role_id)
        dept_ids = []

        return {
            "id": role.id,
            "name": role.name,
            "data_scope": role.data_scope,
            "department_ids": dept_ids,
        }

    async def handle(self, request: Request, query: QuerySet):
        form = await request.body()

        try:
            RoleService().update_role_data_scope(
                form["id"], form["data_scope"], form.get("department_ids", [])
            )
            return Message.success("操作成功")
        except Exception as e:
            return Message.error(str(e))
