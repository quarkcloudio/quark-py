from typing import Any, Dict, List

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field


class Menu(Resource):
    """
    菜单管理
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "菜单"

        # 模型
        self.model = models.Menu

        return self

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("nickname", "昵称"),
            field.text("username", "用户名"),
            field.password("password", "密码").only_on_forms(),
            field.text("email", "邮箱").set_editable(True),
            field.text("phone", "手机号"),
        ]

    async def searches(self, request: Request) -> List[Any]:
        """搜索项定义"""
        return [
            searches.Input("username", "用户名"),
        ]

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.CreateLink(self.title),
            actions.BatchDelete(),
            actions.EditLink(),
            actions.DeleteSpecial(),
            actions.FormSubmit(),
            actions.FormReset(),
            actions.FormBack(),
            actions.FormExtraBack(),
        ]
