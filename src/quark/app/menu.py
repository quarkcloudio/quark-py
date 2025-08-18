from typing import Any, Dict, List

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field
from quark.component.form.rule import Rule
from quark.services import MenuService, PermissionService


class Menu(Resource):
    """
    菜单管理
    """

    async def init(self, request: Request):
        self.title = "菜单"
        self.model = models.Menu
        self.table_list_to_tree = True
        self.query_order = "sort"
        self.page_size = False

        return self

    # 字段
    async def fields(self, request: Request) -> List[Any]:

        # 权限列表
        permissions = await PermissionService().data_source()

        # 菜单列表
        menus = await MenuService().get_list_with_root()

        return [
            field.hidden("id", "ID"),
            field.hidden("pid", "PID").only_on_index(),
            field.group(
                [
                    field.text("name", "名称").set_rules(
                        [Rule.required("名称必须填写")]
                    ),
                    field.text("guard_name", "守卫")
                    .set_rules([Rule.required("守卫必须填写")])
                    .set_default_value("admin")
                    .only_on_forms(),
                    field.icon("icon", "图标").only_on_forms(),
                ]
            ),
            field.group(
                [
                    field.number("sort", "排序")
                    .set_editable(True)
                    .set_default_value(0),
                    field.tree_select("pid", "父节点")
                    .set_tree_data(menus, -1, "pid", "name", "id")
                    .set_default_value(0)
                    .only_on_forms(),
                    field.switch("status", "状态")
                    .set_true_value("正常")
                    .set_false_value("禁用")
                    .set_editable(True)
                    .set_default_value(True),
                ]
            ),
            field.group(
                [
                    field.radio("type", "类型")
                    .set_options(
                        [
                            field.radio_option("目录", 1),
                            field.radio_option("菜单", 2),
                            field.radio_option("按钮", 3),
                        ]
                    )
                    .set_rules([Rule.required("类型必须选择")])
                    .set_default_value(1),
                    field.switch("show", "显示")
                    .set_true_value("显示")
                    .set_false_value("隐藏")
                    .set_editable(True)
                    .set_default_value(True),
                ]
            ),
            field.dependency().set_when(
                "type",
                1,
                lambda: [
                    field.text("path", "路由")
                    .set_rules([Rule.required("路由必须填写")])
                    .set_editable(True)
                    .set_help("前端路由")
                    .set_width(400),
                ],
            ),
            field.dependency().set_when(
                "type",
                2,
                lambda: [
                    field.switch("is_engine", "引擎组件")
                    .set_true_value("是")
                    .set_false_value("否")
                    .set_default_value(True),
                    field.switch("is_link", "外部链接")
                    .set_true_value("是")
                    .set_false_value("否")
                    .set_default_value(False),
                    field.text("path", "路由")
                    .set_rules([Rule.required("路由必须填写")])
                    .set_editable(True)
                    .set_help("前端路由或后端api")
                    .set_width(400)
                    .only_on_forms(),
                ],
            ),
            field.dependency().set_when(
                "type",
                3,
                lambda: [
                    field.transfer("permission_ids", "绑定权限")
                    .set_data_source(permissions)
                    .set_list_style({"width": 320, "height": 300})
                    .set_show_search(True)
                    .only_on_forms(),
                ],
            ),
        ]

    # 搜索
    async def searches(self, request: Request) -> List[Any]:
        return [
            searches.Input("name", "名称"),
            searches.Input("path", "路由"),
            searches.Status(),
        ]

    # 行为
    async def actions(self, request: Request) -> List[Any]:
        return [
            actions.MenuCreateDrawer(self),
            actions.BatchDelete(),
            actions.BatchDisable(),
            actions.BatchEnable(),
            actions.ChangeStatus(),
            actions.MenuEditDrawer(self),
            actions.Delete(),
        ]

    # 编辑页面显示前回调
    async def before_editing(
        self, request: Request, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        id_val = request.query_params.get("id", "")
        try:
            id_int = int(id_val) if id_val else None
        except Exception:
            id_int = None

        if id_int:
            permission_ids: List[int] = []
            permissions = await PermissionService().get_menu_permissions(id_int)
            for v in permissions:
                permission_ids.append(v.permission_id)
            data["permission_ids"] = permission_ids

        return data

    # 保存后回调
    async def after_saved(self, request, id, data, result):
        if data.get("permission_ids") is not None:
            await PermissionService().add_menu_permission(id, data["permission_ids"])
