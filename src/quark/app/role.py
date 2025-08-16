from typing import Any, Dict, List

from quark import Request, Resource, models, services
from quark.app import actions, searches
from quark.component.form import field
from quark.component.form.rule import Rule


class Role(Resource):
    """
    角色管理
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "角色"

        # 模型
        self.model = models.Role

        return self

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("name", "名称")
            .set_rules(
                [
                    Rule.required("名称必须填写"),
                ]
            )
            .set_creation_rules(
                [
                    Rule.unique("roles", "name", "名称已存在"),
                ]
            )
            .set_update_rules(
                [
                    Rule.unique("roles", "name", "{id}", "名称已存在"),
                ]
            ),
            field.text("guard_name", "守卫名称").set_default_value("admin"),
            field.tree("menu_ids", "权限")
            .set_tree_data(await services.MenuService().get_list(), "pid", "id", "name")
            .only_on_forms(),
            field.datetime("created_at", "创建时间").only_on_index(),
            field.datetime("updated_at", "更新时间").only_on_index(),
            field.switch("status", "状态")
            .set_editable(True)
            .set_true_value("正常")
            .set_false_value("禁用")
            .set_default_value(True),
        ]

    async def searches(self, request: Request) -> List[Any]:
        """搜索项定义"""
        return [
            searches.Input("name", "名称"),
        ]

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.CreateLink(self.title),
            actions.BatchDelete(),
            actions.EditLink(),
            actions.Delete(),
            actions.FormSubmit(),
            actions.FormReset(),
            actions.FormBack(),
            actions.FormExtraBack(),
        ]

    async def before_editing(
        self, request: Request, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        编辑页面显示前回调
        """

        # 获取用户菜单
        data["menu_ids"] = await services.RoleService().get_menu_ids_by_role_id(
            data["id"]
        )

        # 返回数据
        return data

    async def after_saved(self, request, id, data, result):
        await services.RoleService().save_menus_by_role_id(id, data["menu_ids"])
