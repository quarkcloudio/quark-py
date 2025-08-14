from typing import Any, Dict

from quark import Request

from ..utils import replace_last
from .resolves_actions import ResolvesActions
from .resolves_fields import ResolvesFields


class ResourceEdit:

    async def update_api(self, request: Request) -> str:
        """
        获取更新表单的接口地址
        """
        form_api = await self.form_api(request)
        if form_api:
            return form_api

        uri = request.url.path.split("/")
        if uri[-1] == "index":
            return replace_last(request.url.path, "/index", "/save")

        return replace_last(request.url.path, "/edit", "/save")

    async def edit_value_api(self, request: Request) -> str:
        """
        编辑页面获取数据接口地址
        """
        uri = request.url.path.split("/")
        if uri[-1] == "index":
            return replace_last(request.url.path, "/index", "/edit/values?id=${id}")

        return replace_last(request.url.path, "/edit", "/edit/values?id=${id}")

    async def update_component_render(
        self, request: Request, data: Dict[str, Any]
    ) -> Any:
        """
        渲染编辑页组件
        """
        title = await self.form_title(request)
        actions = await self.actions(request)
        form_extra_actions = await ResolvesActions(
            request=request, actions=actions
        ).form_extra_actions()
        api = await self.update_api(request)
        fields = ResolvesFields(
            request=request,
            fields=await self.fields(request),
        ).update_fields_within_components()
        form_actions = await ResolvesActions(
            request=request, actions=actions
        ).form_actions()

        return await self.form_component_render(
            request, title, form_extra_actions, api, fields, form_actions, data
        )

    async def before_editing(
        self, request: Request, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        编辑页面显示前回调
        """
        return data
