import json
from typing import Any, List

from tortoise.queryset import QuerySet

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field
from quark.services.attachment import AttachmentService


class Image(Resource):
    """
    图片管理
    """

    async def init(self, request: Request):

        self.title = "图片"

        # 模型
        self.model = models.Attachment

        return self

    async def index_query(self, request: Request) -> QuerySet:
        """
        列表查询
        """
        query = await self.query(request)
        return query.filter(type="IMAGE")

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text(
                "path",
                "显示",
                lambda row: f"<img src='{AttachmentService().get_image_url(row['id'])}' width=50 height=50 />",
            ),
            field.text("name", "名称").set_ellipsis(True),
            field.text("size", "大小").set_sorter(True),
            field.text(
                "extra", "尺寸", lambda row: self._parse_extra(row.get("extra"))
            ),
            field.text("ext", "扩展名"),
            field.datetime("created_at", "上传时间"),
        ]

    def _parse_extra(self, extra: Any) -> str:
        """解析尺寸字段"""
        if not extra:
            return ""
        try:
            data = json.loads(extra)
            if "width" in data and "height" in data:
                return f"{int(data['width'])}*{int(data['height'])}"
        except Exception:
            pass
        return ""

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
