from typing import Any, List

from quark import Request, Resource, models, services
from quark.app import actions, searches
from quark.component.form import field
from quark.component.form.rule import Rule
from quark.component.table.table import Expandable


class Department(Resource):
    """
    部门管理
    """

    async def init(self, request: Request):

        self.table.set_expandable(Expandable(default_expanded_row_keys=[1]))

        # 页面标题
        self.title = "部门"

        # 模型
        self.model = models.Department

        # 树表
        self.table_list_to_tree = True

        # 排序字段
        self.index_query_order = "id, sort"

        # 分页
        self.page_size = False

        return self

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        departments = await services.DepartmentService().get_list()

        return [
            field.hidden("id", "ID"),
            field.hidden("pid", "父级ID").only_on_index(),
            field.text("name", "名称").set_rules(
                [
                    Rule.required("部门名称必须填写"),
                    Rule.min(2, "部门名称不能少于2个字符"),
                    Rule.max(100, "部门名称不能超过100个字符"),
                ]
            ),
            field.tree_select("pid", "父节点")
            .set_tree_data(departments, "pid", "name", "id")
            .set_rules(
                [
                    Rule.required("请选择父节点"),
                ]
            )
            .set_default_value(1)
            .only_on_creating(),
            field.dependency().set_when(
                "id",
                "!=",
                1,
                lambda: (
                    field.tree_select("pid", "父节点")
                    .set_tree_data(departments, "pid", "name", "id")
                    .set_rules([Rule.required("请选择父节点")])
                    .set_default_value(1)
                    .only_on_updating()
                ),
            ),
            field.number("sort", "排序").set_editable(True).set_default_value(0),
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
            searches.Status(),
        ]

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.CreateModal(self),
            actions.BatchDelete(),
            actions.BatchDisable(),
            actions.BatchEnable(),
            actions.EditModal(self),
            actions.DeleteSpecial(),
        ]
