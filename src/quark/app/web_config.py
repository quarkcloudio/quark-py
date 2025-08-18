import json
from typing import Any, Dict, List

from tortoise import Model

from quark import Message, Request, Resource, models
from quark.app import actions
from quark.component.form import field
from quark.component.tabs.tab_pane import TabPane
from quark.models.config import Config
from quark.services.config import ConfigService


class WebConfig(Resource):
    """
    网站配置
    """

    async def init(self, request: Request) -> Any:

        # 页面标题
        self.title = "网站配置"

        # 模型
        self.model = models.Config

        return self

    async def fields(self, request: Request) -> List[Any]:
        # 获取所有分组
        group_names = (
            await Config.filter(status=1)
            .distinct()
            .values_list("group_name", flat=True)
        )

        tab_panes = []
        for group_name in group_names:
            configs = (
                await Config.filter(status=1, group_name=group_name)
                .order_by("sort")
                .values()
            )
            fields_list = []

            for config in configs:
                remark = config.get("remark", "")
                if config["type"] == "text":
                    f = field.text(config["name"], config["title"]).set_extra(remark)
                elif config["type"] == "textarea":
                    f = field.textarea(config["name"], config["title"]).set_extra(
                        remark
                    )
                elif config["type"] == "file":
                    f = (
                        field.file(config["name"], config["title"])
                        .set_extra(remark)
                        .set_button(f"上传{config['title']}")
                    )
                elif config["type"] == "picture":
                    f = (
                        field.image(config["name"], config["title"])
                        .set_extra(remark)
                        .set_button(f"上传{config['title']}")
                    )
                elif config["type"] == "switch":
                    f = (
                        field.switch(config["name"], config["title"])
                        .set_editable(True)
                        .set_true_value("正常")
                        .set_false_value("禁用")
                        .set_default_value(True)
                        .set_extra(remark)
                    )
                else:
                    continue
                fields_list.append(f)

            tab_panes.append(TabPane(title=str(group_name), body=fields_list))

        return tab_panes

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return [
            actions.FormSubmit(),
            actions.FormReset(),
            actions.FormBack(),
            actions.FormExtraBack(),
        ]

    async def before_form_showing(self, request: Request) -> Any:
        configs = await Config.filter(status=1).values()
        data = {}
        for config in configs:
            value = config["value"]
            if config["type"] == "switch":
                data[config["name"]] = value != "0"
            elif config["type"] in ["picture", "file"]:
                if value:
                    try:
                        json_data = json.loads(value)
                        data[config["name"]] = json_data
                    except:
                        data[config["name"]] = value
                else:
                    data[config["name"]] = None
            else:
                data[config["name"]] = value
        return data

    async def form_handle(
        self, request: Request, model: Model, data: Dict[str, Any]
    ) -> Any:
        try:
            for k, v in data.items():
                if isinstance(v, (list, dict)):
                    v = json.dumps(v)
                await Config.filter(name=k).update(value=v)
        except Exception as e:
            return Message.error(str(e))

        # 刷新网站配置
        await ConfigService().refresh()

        return Message.success("操作成功")
