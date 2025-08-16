from typing import Any, List

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field
from quark.component.form.rule import Rule


class Position(Resource):
    """
    职位管理
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "职位"

        # 模型
        self.model = models.Position

        # 排序字段
        self.index_query_order = "id, sort"

        return self

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("name", "名称").set_rules(
                [
                    Rule.required("职位名称必须填写"),
                    Rule.min(2, "职位名称不能少于2个字符"),
                    Rule.max(100, "职位名称不能超过100个字符"),
                ]
            ),
            field.number("sort", "排序").set_editable(True).set_default_value(0),
            field.textarea("remark", "备注"),
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
            actions.Delete(),
        ]
