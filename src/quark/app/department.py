from typing import Dict, List

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field
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
        self.index_query_order = "id,sort"

        # 分页
        self.page_size = False

        return self

    async def fields(self, request: Request) -> List[Dict]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.hidden("pid", "父级ID").only_on_index(),
            field.text("name", "名称"),
            field.number("sort", "排序").set_default_value(0),
            field.switch("status", "状态")
            .set_editable(True)
            .set_true_value("正常")
            .set_false_value("禁用")
            .set_default_value(True),
        ]

    async def searches(self, request: Request) -> List[Dict]:
        """搜索项定义"""
        return [
            searches.Input("name", "名称"),
            searches.Status(),
        ]

    async def actions(self, request: Request) -> List[Dict]:
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
