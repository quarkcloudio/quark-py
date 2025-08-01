from typing import Any, Dict, List
from fastapi import Request
from ..component.tabs.tabs import Tabs
from ..component.card.card import Card
from ..utils import replace_last


class ResourceDetail:

    def detail_value_api(self, request: Request) -> str:
        """
        获取详情页数据接口地址
        """
        uri = request.url.path.split("/")
        if uri[-1] == "index":
            return replace_last(request.url.path, "/index", "/detail/values?id=${id}")

        return replace_last(request.url.path, "/detail", "/detail/values?id=${id}")

    def detail_title(self, request: Request) -> str:
        """
        获取详情页标题
        """
        title = self.get_title()
        return f"{title}详情"

    def detail_component_render(self, request: Request, data: Dict[str, Any]) -> Card:
        """
        渲染详情页组件
        """
        title = self.detail_title(request)
        form_extra_actions = self.detail_extra_actions(request)
        fields = self.detail_fields_within_components(request, None, data)
        form_actions = self.detail_actions(request)

        return self.detail_within_card(
            request, title, form_extra_actions, fields, form_actions, data
        )

    def detail_within_card(
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

    def detail_within_tabs(
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

    def before_detail_showing(
        self, request: Request, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        详情页显示前回调
        """
        return data

    def detail_extra_actions(self, request: Request) -> List[Any]:
        """
        详情页右上角自定义区域行为（由模板实现）
        """
        return self.detail_extra_actions(request)

    def detail_fields_within_components(
        self, request: Request, field_type: Any, data: Dict[str, Any]
    ) -> List[Any]:
        """
        获取包裹在组件中的详情页字段（由模板实现）
        """
        return self.detail_fields_within_components(request, field_type, data)

    def detail_actions(self, request: Request) -> List[Any]:
        """
        获取详情页操作按钮（由模板实现）
        """
        return self.detail_actions(request)
