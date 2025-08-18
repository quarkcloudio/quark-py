from typing import Any, Dict, List

from tortoise import Model

from quark import Request

from ..component.card.card import Card
from ..component.form.form import Form
from ..component.message.message import Message
from ..component.tabs.tabs import Tabs
from ..utils import is_creating, is_editing
from .request.store import StoreRequest
from .resolves_fields import ResolvesFields


class ResourceForm:
    """
    表单相关的方法
    """

    async def form_api(self, request: Request) -> str:
        """
        获取表单提交 API 地址
        """
        return ""

    async def form_title(self, request: Request) -> str:
        """
        获取表单标题
        """
        title = self.title
        if is_creating(request):
            return f"创建{title}"
        elif is_editing(request):
            return f"编辑{title}"
        else:
            return title

    async def form_component_render(
        self,
        request: Request,
        title: str,
        extra: Any,
        api: str,
        fields: Any,
        actions: List[Any],
        data: Dict[str, Any],
    ) -> Any:
        """
        渲染表单组件，支持 Tab 或 Card 两种形式
        """
        if isinstance(fields, list) and len(fields) > 0:
            first_item = fields[0]
            component_type = getattr(first_item, "component", "")
            if component_type == "tabPane":
                return await self.form_within_tabs(
                    request, title, extra, api, fields, actions, data
                )
        return await self.form_within_card(
            request, title, extra, api, fields, actions, data
        )

    async def form_within_card(
        self,
        request: Request,
        title: str,
        extra: Any,
        api: str,
        fields: Any,
        actions: List[Any],
        data: Dict[str, Any],
    ) -> Card:
        """
        在卡片中渲染表单
        """
        form = (
            self.form.set_style({"padding": "24px"})
            .set_api(api)
            .set_actions(actions)
            .set_body(fields)
            .set_initial_values(data)
        )

        return (
            Card()
            .set_title(title)
            .set_header_bordered(True)
            .set_extra(extra)
            .set_body(form)
        )

    async def form_within_tabs(
        self,
        request: Request,
        title: str,
        extra: Any,
        api: str,
        fields: Any,
        actions: List[Any],
        data: Dict[str, Any],
    ) -> Form:
        """
        在标签页中渲染表单
        """
        tabs_component = Tabs().set_tab_panes(fields).set_tab_bar_extra_content(extra)

        return (
            self.form.set_style({"backgroundColor": "#fff", "paddingBottom": "20px"})
            .set_api(api)
            .set_actions(actions)
            .set_body(tabs_component)
            .set_initial_values(data)
        )

    async def before_form_showing(self, request: Request) -> Any:
        """
        表单显示前回调
        """
        return {}

    async def form_handle(
        self, request: Request, model: Model, data: Dict[str, Any]
    ) -> Any:
        """
        表单提交处理
        """

        fields = ResolvesFields(
            request, await self.fields(request)
        ).creation_fields_without_when()

        return await StoreRequest(
            request=request, resource=self, model=model, fields=fields
        ).handle(data)

    async def before_saving(
        self, request: Request, submit_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        保存数据前回调
        """
        return submit_data

    async def after_imported(
        self, request: Request, id_: int, data: Dict[str, Any], result: Any
    ):
        """
        导入数据后回调
        """

    async def after_saved(
        self, request: Request, id: int, data: Dict[str, Any], result: Any
    ):
        """
        保存数据后回调
        """

    async def after_saved_redirect_to(
        self, request: Request, id: int, data: Dict[str, Any]
    ) -> Any:
        """
        保存数据后跳转处理
        """
        redirect_url = "/layout/index?api=" + "/api/admin/{resource}/index"
        redirect_url = redirect_url.replace(
            "{resource}", request.path_params.get("resource", "")
        )

        return Message.success("操作成功", None, redirect_url)
