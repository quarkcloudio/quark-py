from typing import Any, List

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field


class ActionLog(Resource):
    """
    操作日志管理
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "日志"

        # 模型
        self.model = models.ActionLog

        return self

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("username", "用户信息"),
            field.text("url", "行为"),
            field.text("ip", "IP").set_ellipsis(True),
            field.text("created_at", "发生时间"),
        ]

    async def searches(self, request: Request) -> List[Any]:
        """搜索项定义"""
        return [
            searches.Input("username", "账号"),
            searches.Input("url", "行为"),
            searches.Input("ip", "IP"),
        ]

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.BatchDelete(),
            actions.Delete(),
        ]
