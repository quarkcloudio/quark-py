from typing import Any, Dict

from quark import Request

from ..utils import replace_last
from .resolves_actions import ResolvesActions
from .resolves_fields import ResolvesFields


class ResourceCreate:
    """
    创建表单
    """

    async def creation_api(self, request: Request) -> str:
        """
        获取创建表单提交接口地址
        """
        form_api = await self.form_api(request)
        if form_api:
            return form_api

        uri = request.url.path.split("/")
        last_segment = uri[-1]

        if last_segment == "index":
            return replace_last(request.url.path, "/index", "/store")
        elif last_segment == "form":
            return replace_last(request.url.path, "/form", "/store")

        return replace_last(request.url.path, "/create", "/store")

    async def creation_component_render(
        self, request: Request, data: Dict[str, Any]
    ) -> Any:
        """
        渲染创建页面组件
        """
        title = await self.form_title(request)
        actions = await self.actions(request)
        form_extra_actions = await ResolvesActions(
            request=request, actions=actions
        ).form_extra_actions()
        api = await self.creation_api(request)
        fields = ResolvesFields(
            request=request,
            fields=await self.fields(request),
        ).creation_fields_within_components()
        form_actions = await ResolvesActions(
            request=request, actions=actions
        ).form_actions()

        return await self.form_component_render(
            request, title, form_extra_actions, api, fields, form_actions, data
        )

    async def before_creating(self, request: Request) -> Dict[str, Any]:
        """
        创建页面显示前回调
        """
        return {}
