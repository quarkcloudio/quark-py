from typing import Any, Dict, List
from app.core.context import Context
from app.template.admin.resource.actions import ModalForm
from app.template.admin.resource.field import Field
from app.template.admin.component.form.fields.selectfield import Option
from app.template.admin.component.form import rule
from app.service.department_service import DepartmentService
from app.service.casbin_service import CasbinService
from app.service.role_service import RoleService


class DataScopeAction(ModalForm):
    def __init__(self, name="数据权限"):
        super().__init__()
        self.name = name
        self.type = "link"
        self.size = "small"
        self.destroy_on_close = True
        self.set_only_on_index_table_row(True)
        self.set_api_params(["id", "name"])

    def fields(self, ctx: Context) -> List[Any]:
        field = Field()
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
            .set_rules([rule.required("请选择数据范围")])
            .set_default(1),
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

    def data(self, ctx: Context) -> Dict[str, Any]:
        id_str = ctx.query.get("id")
        if not id_str:
            return {}

        try:
            role_id = int(id_str)
        except ValueError:
            return {}

        role = RoleService().get_info_by_id(role_id)
        if not role:
            return {}

        dept_ids = CasbinService().get_role_department_ids(role_id)

        return {
            "id": role.id,
            "name": role.name,
            "data_scope": role.data_scope,
            "department_ids": dept_ids,
        }

    async def handle(self, ctx: Context, db_model) -> Any:
        form = await ctx.parse_form(
            {"id": int, "data_scope": int, "department_ids": list}
        )

        try:
            RoleService().update_role_data_scope(
                form["id"], form["data_scope"], form.get("department_ids", [])
            )
            return ctx.cjson_ok("操作成功")
        except Exception as e:
            return ctx.cjson_error(str(e))
