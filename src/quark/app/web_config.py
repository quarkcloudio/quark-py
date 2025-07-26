from typing import List, Dict
from quark import models, Request, Resource
from quark.app import actions
from quark.component.form import field


class WebConfig(Resource):
    """
    网站配置
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "网站配置"

        # 模型
        self.model = models.Config

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
