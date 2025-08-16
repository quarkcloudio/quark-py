from typing import Any, List

from quark import Request, Resource, models
from quark.app import actions, searches
from quark.component.form import field
from quark.component.form.rule import Rule


class Config(Resource):
    """
    配置管理
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "配置"

        # 模型
        self.model = models.Config

        return self

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("title", "标题")
            .set_rules(
                [
                    Rule.required("标题必须填写")
                ]
            ),
            field.text("name", "名称").set_rules(
                [
                    Rule.required("名称必须填写")
                ]
            )
            .set_creation_rules(
                [
                    Rule.unique("configs", "name", "名称已存在"),
                ]
            )
            .set_update_rules(
                [
                    Rule.unique("configs", "name", "{id}", "名称已存在"),
                ]
            ), 
            field.radio("type", "类型")
            .set_options([
                field.radio_option("文本", "text"),
                field.radio_option("文本域", "textarea"),
                field.radio_option("图片", "picture"),
                field.radio_option("文件", "file"),
                field.radio_option("开关", "switch")
            ])
            .set_default_value("text")
            .only_on_forms(),
            field.number("sort", "排序")
            .set_default_value(0)
            .only_on_forms(),
            field.text("group_name", "分组名称")
            .set_rules(
                [
                    Rule.required("分组名称必须填写")
                ]
            ).only_on_forms(),
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
            searches.Input("title", "标题"),
            searches.Input("name", "名称"),
            searches.Status(),
        ]

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.CreateDrawer(self),
            actions.BatchDelete(),
            actions.BatchDisable(),
            actions.BatchEnable(),
            actions.EditDrawer(self),
            actions.Delete(),
        ]
