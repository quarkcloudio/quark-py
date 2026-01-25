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
        self.query_order = ["sort"]
        self.page_size = False

        return self

    # 字段
    async def fields(self, request: Request) -> List[Any]:

        # 权限列表
        permissions = await PermissionService().data_source()

        # 菜单列表
        menus = await MenuService().get_list_with_root()

        return [
            field.hidden("id", "ID"),  # 列表读取且不展示的字段
            field.hidden("pid", "PID").only_on_index(),  # 列表读取且不展示的字段
            field.hidden("query", "查询参数"),
            field.hidden("api", "API接口"),
            field.hidden("url", "URL地址"),
            field.hidden("component", "组件"),
            field.group(
                [
                    field.text("name", "名称").set_rules(
                        [Rule.required("名称必须填写")]
                    ),
                    field.text("guard_name", "守卫")
                    .set_rules([Rule.required("守卫必须填写")])
                    .set_default_value("admin")
                    .only_on_forms(),
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
                ]
            ),
            field.group(
                [
                    field.icon("icon", "图标").only_on_forms(),
                    field.number("sort", "排序")
                    .set_editable(True)
                    .set_default_value(0),
                    field.tree_select("pid", "上级菜单")
                    .set_tree_data(menus, -1, "pid", "name", "id")
                    .set_default_value(0)
                    .only_on_forms(),
                ]
            ),
            field.dependency().set_when(
                "type",
                1,
                lambda: [
                    field.text("path", "路由")
                    .set_rules([Rule.required("路由必须填写")])
                    .set_editable(True)
                    .set_help("访问的路由地址，如：`user`")
                    .set_width("400px"),
                ],
            ),
            field.dependency().set_when(
                "type",
                2,
                lambda: [
                    field.radio("page_type", "页面类型")
                    .set_options(
                        [
                            field.radio_option("默认", 1),
                            field.radio_option("引擎", 2),
                            field.radio_option("外链", 3),
                            field.radio_option("iframe", 4),
                        ]
                    )
                    .set_rules([Rule.required("页面类型必须选择")])
                    .set_default_value(1)
                    .only_on_forms(),
                    field.dependency().set_when(
                        "page_type",
                        1,
                        lambda: [
                            field.text("path", "路由地址")
                            .set_rules([Rule.required("路由地址必须填写")])
                            .set_editable(True)
                            .set_help("访问的路由地址，如：`user`")
                            .set_width("400px")
                            .only_on_forms(),
                            field.text("component", "组件路径")
                            .set_rules([Rule.required("组件路径必须填写")])
                            .set_editable(True)
                            .set_help("访问的组件路径，如：`user/index`")
                            .set_width("400px")
                            .only_on_forms(),
                        ],
                    ),
                    field.dependency().set_when(
                        "page_type",
                        2,
                        lambda: [
                            field.text("path", "路由地址")
                            .set_rules([Rule.required("路由地址必须填写")])
                            .set_editable(True)
                            .set_help("访问的路由地址，如：`user`")
                            .set_width("400px")
                            .only_on_forms(),
                            field.text("api", "接口地址")
                            .set_rules([Rule.required("接口地址必须填写")])
                            .set_editable(True)
                            .set_help("引擎接口地址，如：`/api/admin/user/index`")
                            .set_width("400px")
                            .only_on_forms(),
                        ],
                    ),
                    field.dependency().set_when(
                        "page_type",
                        3,
                        lambda: [
                            field.text("path", "外链地址")
                            .set_rules([Rule.required("外链地址必须填写")])
                            .set_editable(True)
                            .set_help("访问的外链地址，以`http(s)://`开头")
                            .set_width("400px")
                            .only_on_forms(),
                        ],
                    ),
                    field.dependency().set_when(
                        "page_type",
                        4,
                        lambda: [
                            field.text("path", "路由地址")
                            .set_rules([Rule.required("路由地址必须填写")])
                            .set_editable(True)
                            .set_help("访问的路由地址，如：`user`")
                            .set_width("400px")
                            .only_on_forms(),
                            field.text("url", "iframe地址")
                            .set_rules([Rule.required("iframe地址必须填写")])
                            .set_editable(True)
                            .set_help("访问的iframe地址，以`http(s)://`开头")
                            .set_width("400px")
                            .only_on_forms(),
                        ],
                    ),
                ],
            ),
            field.dependency().set_when(
                "type",
                ">",
                1,
                lambda: [
                    field.text("permission", "权限标识")
                    .set_help("鉴权标识，如：`user:index`")
                    .set_width("400px"),
                ],
            ),
            field.group(
                [
                    field.switch("visible", "显示")
                    .set_true_value("显示")
                    .set_false_value("隐藏")
                    .set_editable(True)
                    .set_default_value(True),
                    field.switch("status", "状态")
                    .set_true_value("正常")
                    .set_false_value("禁用")
                    .set_editable(True)
                    .set_default_value(True),
                ]
            ),
            field.dependency().set_when(
                "type",
                3,
                lambda: [
                    field.transfer("permission_ids", "绑定权限")
                    .set_data_source(permissions)
                    .set_list_style(
                        {
                            "width": "320px",
                            "height": "300px",
                        }
                    )
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
            actions.ChangeStatus(),
            actions.MenuEditDrawer(self),
            actions.Delete(),
        ]

    # 编辑页面显示前回调
    async def before_editing(
        self, request: Request, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        id = request.query_params.get("id", "")
        if id and isinstance(id, str):
            try:
                id_int = int(id)
                permission_ids = []
                permissions = await PermissionService().get_menu_permissions(id_int)
                for v in permissions:
                    permission_ids.append(v.id)
                data["permission_ids"] = permission_ids
            except ValueError:
                pass

        page_type = data.get("page_type", 0)
        if page_type == 2:
            import json

            query = json.loads(data.get("query", "{}"))
            data["api"] = query.get("api")
        elif page_type == 4:
            import json

            query = json.loads(data.get("query", "{}"))
            data["url"] = query.get("url")

        return data

    async def before_saving(self, request, submit_data):
        if submit_data.get("page_type", 0) == 2:
            submit_data["query"] = f'{{"api":"{submit_data.get("api", "")}"}}'
        if submit_data.get("page_type", 0) == 4:
            submit_data["query"] = f'{{"url":"{submit_data.get("url", "")}"}}'

        return submit_data

    # 保存后回调
    async def after_saved(self, request, id, data, result):
        if data.get("permission_ids") is not None:
            await PermissionService().add_menu_permission(id, data["permission_ids"])
