from pydantic import model_validator
from typing import List, Dict
from quark import models, Request, Resource
from quark.app import searches, actions
from quark.component.form import field


class Position(Resource):
    """
    职位管理
    """

    @model_validator(mode="after")
    def init(self):

        # 页面标题
        self.title = "职位"

        # 模型
        self.model = models.Position

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
