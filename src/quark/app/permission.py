from typing import Any, List

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import Rule, field


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

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("name", "名称").set_rules(
                [
                    Rule.required("名称必须填写"),
                ]
            ),
            field.text("path", "路径").set_rules(
                [
                    Rule.required("路径必须填写"),
                ]
            ),
            field.select("method", "方法")
            .set_options(
                [
                    field.select_option("Any", "Any"),
                    field.select_option("GET", "GET"),
                    field.select_option("HEAD", "HEAD"),
                    field.select_option("OPTIONS", "OPTIONS"),
                    field.select_option("POST", "POST"),
                    field.select_option("PUT", "PUT"),
                    field.select_option("PATCH", "PATCH"),
                    field.select_option("DELETE", "DELETE"),
                ]
            )
            .set_filters(True)
            .set_default_value("GET"),
            field.textarea("remark", "备注"),
        ]

    async def searches(self, request: Request) -> List[Any]:
        """搜索项定义"""
        return [
            searches.Input("name", "名称"),
            searches.Input("path", "路径"),
        ]

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.SyncPermission(),
            actions.CreateModal(self),
            actions.BatchDelete(),
            actions.EditModal(self),
            actions.Delete(),
            actions.FormSubmit(),
            actions.FormReset(),
            actions.FormBack(),
            actions.FormExtraBack(),
        ]
