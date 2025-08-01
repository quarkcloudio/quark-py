from typing import List, Dict
import json
from quark import services, models, Request, Resource
from quark.app import searches, actions
from quark.component.form import field, Rule
from tortoise.models import QuerySet, Q


class User(Resource):
    """
    用户管理
    """

    async def init(self, request: Request):

        # 部门列表
        departments = await services.DepartmentService().get_list()

        # 部门树
        self.table_tree_bar.set_name("departmentIds").set_tree_data(
            departments, "pid", "id", "name"
        )

        # 页面标题
        self.title = "用户"

        # 模型
        self.model = models.User

        return self

    async def index_query(self, request: Request) -> QuerySet:
        """
        列表查询
        """
        query = await self.query(request)

        # 从请求中获取 departmentIds 参数
        department_ids_param = request.query_params.get("departmentIds")
        if not department_ids_param:
            return query

        try:
            ids: List[int] = json.loads(department_ids_param)
        except json.JSONDecodeError:
            return query

        if not ids:
            return query

        # 拓展 ids 为包含所有子部门 ID
        all_ids = ids.copy()
        for dep_id in ids:
            children_ids = await services.DepartmentService().get_children_ids(dep_id)
            all_ids.extend(children_ids)

        # 去重
        all_ids = list(set(all_ids))

        # 构建筛选条件
        return query.filter(Q(department_id__in=all_ids))

    async def fields(self, request: Request) -> List[Dict]:
        """字段定义"""

        # 获取所有角色
        roles = await services.RoleService().get_list()

        # 获取所有部门
        departments = await services.DepartmentService().get_list()

        # 获取所有职位
        positions = await services.PositionService().get_list()

        return [
            field.id("id", "ID"),
            field.image("avatar", "头像"),
            field.text(
                "username",
                "用户名",
                lambda row: "<a href='#/layout/index?api=/api/admin/user/edit&id="
                + str(row.id)
                + "'>"
                + row.username
                + "</a>",
            )
            .set_rules(
                [
                    Rule.required("用户名必须填写"),
                    Rule.min(6, "用户名不能少于6个字符"),
                    Rule.max(20, "用户名不能超过20个字符"),
                ]
            )
            .set_creation_rules(
                [
                    Rule.unique("users", "username", "用户名已存在"),
                ]
            )
            .set_update_rules(
                [
                    Rule.unique("users", "username", "{id}", "用户名已存在"),
                ]
            ),
            field.text("nickname", "昵称")
            .set_editable(True)
            .set_rules(
                [
                    Rule.required("昵称必须填写"),
                ]
            ),
            field.checkbox("role_ids", "角色").set_options(roles),
            field.tree_select("department_id", "部门")
            .set_tree_data(departments, "pid", "name", "id")
            .only_on_forms(),
            field.checkbox("position_ids", "职位")
            .set_options(positions)
            .only_on_forms(),
            field.text("email", "邮箱")
            .set_editable(True)
            .set_rules(
                [
                    Rule.required("邮箱必须填写"),
                ]
            )
            .only_on_forms(),
            field.text("phone", "手机号")
            .set_rules(
                [
                    Rule.required("手机号必须填写"),
                ]
            )
            .set_creation_rules(
                [
                    Rule.unique("users", "phone", "手机号已存在"),
                ]
            )
            .set_update_rules(
                [
                    Rule.unique("users", "phone", "{id}", "手机号已存在"),
                ]
            ),
            field.radio("sex", "性别")
            .set_options([field.radio_option("男", 1), field.radio_option("女", 2)])
            .set_filters(True)
            .set_default_value(1),
            field.password("password", "密码")
            .set_rules(
                [
                    Rule.regexp(r"/^.{6,}$/", "密码不少于六位"),
                    Rule.regexp(r"/[A-Z]/", "至少包含一个大写字母"),
                    Rule.regexp(r"/[a-z]/", "至少包含一个小写字母"),
                    Rule.regexp(r"/[0-9]/", "至少包含一个数字"),
                    Rule.regexp(
                        r"/[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/", "至少包含一个特殊字符"
                    ),
                ]
            )
            .set_creation_rules(
                [
                    Rule.required("密码必须填写"),
                ]
            )
            .only_on_forms(),
            field.datetime("last_login_time", "最后登录时间").only_on_index(),
            field.switch("status", "状态")
            .set_editable(True)
            .set_true_value("正常")
            .set_false_value("禁用")
            .set_default_value(True),
        ]

    async def searches(self, request: Request) -> List[Dict]:
        """搜索项定义"""
        return [
            searches.Input("username", "用户名"),
            searches.Input("nickname", "昵称"),
            searches.Status(),
            searches.DatetimeRange("created_at", "创建时间"),
        ]

    async def actions(self, request: Request) -> List[Dict]:
        """行为定义"""
        return [
            actions.CreateLink(self.title),
            actions.BatchDelete(),
            actions.EditLink(),
            actions.DeleteSpecial(),
            actions.FormSubmit(),
            actions.FormReset(),
            actions.FormBack(),
            actions.FormExtraBack(),
        ]
