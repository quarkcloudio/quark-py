from typing import List, Dict
from quark import models, Request, Resource
from quark.app import searches, actions
from quark.component.form import field


class Permission(Resource):
    """
    权限管理
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "权限"

        # 模型
        self.model = models.Permission

        return self

    async def fields(self, request: Request) -> List[Dict]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("name", "名称"),
            field.text("path", "路径"),
            field.select("method", "方法"),
            field.textarea("remark", "备注"),
        ]

    async def searches(self, request: Request) -> List[Dict]:
        """搜索项定义"""
        return [
            searches.Input("name", "名称"),
            searches.Input("path", "路径"),
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
