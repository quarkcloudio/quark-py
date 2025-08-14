from typing import Any, Dict, List

from quark import Request

from ..component.card.card import Card
from ..component.tabs.tabs import Tabs
from ..utils import replace_last
from .resolves_actions import ResolvesActions
from .resolves_fields import ResolvesFields


class ResourceDetail:

    async def detail_value_api(self, request: Request) -> str:
        """
        获取详情页数据接口地址
        """
        uri = request.url.path.split("/")
        if uri[-1] == "index":
            return replace_last(request.url.path, "/index", "/detail/values?id=${id}")

        return replace_last(request.url.path, "/detail", "/detail/values?id=${id}")

    async def detail_title(self, request: Request) -> str:
        """
        获取详情页标题
        """
        return f"{self.title}详情"

    async def detail_component_render(
        self, request: Request, data: Dict[str, Any]
    ) -> Card:
        """
        渲染详情页组件
        """
        title = await self.detail_title(request)
        actions = await self.actions(request)
        detail_extra_actions = await ResolvesActions(
            request=request, actions=actions
        ).detail_extra_actions()

        detail_actions = await ResolvesActions(
            request=request, actions=actions
        ).detail_actions()

        fields = ResolvesFields(
            request=request,
            fields=await self.fields(request),
        ).detail_fields_within_components(
            None,
            data,
            detail_actions,
        )

        return await self.detail_within_card(
            request, title, detail_extra_actions, fields, detail_actions, data
        )

    async def detail_within_card(
        self,
        request: Request,
        title: str,
        extra: Any,
        fields: List[Any],
        actions: List[Any],
        data: Dict[str, Any],
    ) -> Card:
        """
        在卡片中渲染详情页
        """
        return (
            Card()
            .set_title(title)
            .set_header_bordered(True)
            .set_extra(extra)
            .set_body(fields)
        )

    async def detail_within_tabs(
        self,
        request: Request,
        title: str,
        extra: Any,
        fields: List[Any],
        actions: List[Any],
        data: Dict[str, Any],
    ) -> Tabs:
        """
        在标签页中渲染详情页
        """
        return Tabs().set_tab_panes(fields).set_tab_bar_extra_content(extra)

    async def before_detail_showing(
        self, request: Request, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        详情页显示前回调
        """
        return data
