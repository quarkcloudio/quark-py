from typing import Any, List

from tortoise.queryset import QuerySet

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field


class File(Resource):
    """
    文件管理
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "文件"

        # 模型
        self.model = models.Attachment

        return self

    async def index_query(self, request: Request) -> QuerySet:
        """
        列表查询
        """
        query = await self.query(request)
        return query.filter(type="FILE")

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("name", "名称"),
            field.text("size", "大小").set_sorter(True),
            field.text("ext", "扩展名"),
            field.datetime("created_at", "上传时间"),
        ]

    async def searches(self, request: Request) -> List[Any]:
        """搜索项定义"""
        return [
            searches.Input("name", "名称"),
            searches.DatetimeRange("created_at", "上传时间"),
        ]

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.BatchDelete(),
            actions.Delete(),
        ]
