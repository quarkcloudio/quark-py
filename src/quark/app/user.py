from pydantic import model_validator
from typing import List, Dict
from quark import Request
from quark.template.resource import Resource
from quark.component.form import field
from quark import models
from quark.app import searches
from quark.app import actions


class User(Resource):
    """
    用户管理
    """

    @model_validator(mode="after")
    def init(self):

        # 页面标题
        self.title = "用户"

        # 模型
        self.model = models.User

        return self

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
        ]

    async def actions(self, request: Request) -> List[Dict]:
        """行为定义"""
        return [
            actions.CreateLink(self.title),
            actions.EditLink(),
            actions.FormSubmit(),
            actions.FormReset(),
            actions.FormBack(),
            actions.FormExtraBack(),
        ]
