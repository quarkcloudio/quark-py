from typing import List, Dict
import json
from quark import services, models, Request, Resource
from quark.app import searches, actions
from quark.component.form import field
from tortoise.models import QuerySet, Q


class User(Resource):
    """
    用户管理
    """

    async def init(self, request: Request):

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
        return [
            field.id("id", "ID"),
            field.text("nickname", "昵称"),
            field.text("username", "用户名"),
            field.password("password", "密码").only_on_forms(),
            field.text("email", "邮箱").set_editable(True),
            field.text("phone", "手机号"),
        ]

    async def searches(self, request: Request) -> List[Dict]:
        """搜索项定义"""
        return [
            searches.Input("username", "用户名"),
            searches.Input("nickname", "昵称"),
            searches.Status(),
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
