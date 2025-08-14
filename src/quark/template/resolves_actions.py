from typing import Any, List, Optional

from quark import Request

from ..component.action.action import Action
from ..component.dropdown.dropdown import Dropdown
from ..component.form.form import Form
from ..component.space.space import Space


class ResolvesActions:

    # 请求
    request: Request = None

    # 行为
    actions: Optional[Any] = None

    def __init__(self, request: Request, actions: Optional[Any] = None):
        self.request = request
        self.actions = actions

    async def index_table_actions(self) -> List[Any]:
        """获取列表页顶部工具栏中的动作"""
        items = []
        for action in self.actions:
            if action.shown_on_index():
                items.append(await self.build_action(action))

        return self._wrap_in_space(items)

    async def index_table_row_actions(self) -> List[Any]:
        """获取列表页行内动作"""
        items = []
        for action in self.actions:
            if action.shown_on_index_table_row():
                items.append(await self.build_action(action))

        return items

    async def index_table_alert_actions(self) -> List[Any]:
        """获取多选弹出层动作"""
        items = []
        for action in self.actions:
            if action.shown_on_index_table_alert():
                items.append(await self.build_action(action))

        return items

    async def form_actions(self) -> List[Any]:
        """获取表单页动作"""
        items = []
        for action in self.actions:
            if action.shown_on_form():
                items.append(await self.build_action(action))

        return items

    async def form_extra_actions(self) -> List[Any]:
        """表单页右上角自定义区域行为"""
        items = []
        for action in self.actions:
            if action.shown_on_form_extra():
                items.append(await self.build_action(action))

        return items

    async def detail_actions(self) -> List[Any]:
        """获取详情页动作"""
        items = []
        for action in self.actions:
            if action.shown_on_detail():
                items.append(await self.build_action(action))

        return items

    async def detail_extra_actions(self) -> List[Any]:
        """详情页右上角自定义区域行为"""
        items = []
        for action in self.actions:
            if action.shown_on_detail_extra():
                items.append(await self.build_action(action))

        return items

    async def build_action(self, item) -> Any:
        """构建行为组件（支持 link/modal/drawer/dropdown/switch 等）"""
        name = item.get_name()
        with_loading = item.get_with_loading()
        reload = item.get_reload()
        uri_key = item.get_uri_key(item)
        api = item.get_api()
        params = item.get_api_params()
        action_type = item.get_action_type()
        button_type = item.get_type()
        size = item.get_size()
        icon = item.get_icon()
        confirm_title = item.get_confirm_title()
        confirm_text = item.get_confirm_text()
        confirm_type = item.get_confirm_type()

        if not api:
            api = self.build_action_api(params, uri_key)

        action_component = (
            Action().set_label(name).set_with_loading(with_loading).set_api(api)
        )

        if reload:
            action_component.set_reload(reload)

        if action_type:
            action_component.set_action_type(action_type)

        if button_type:
            action_component.set_type(button_type, False)

        if size:
            action_component.set_size(size)

        if icon:
            action_component.set_icon(icon)

        # 特定行为类型渲染
        if action_type == "link":
            href = await item.get_href(self.request)
            target = await item.get_target(self.request)
            action_component.set_link(href, target)

        elif action_type == "modal":
            init_api = self.build_init_api(params, uri_key)
            width = item.get_width()
            destroy_on_close = item.get_destroy_on_close()
            body = await item.get_body(self.request)
            actions = await item.get_actions(self.request)

            form_component = Form().set_api(api).set_init_api(init_api).set_body(body)
            form_component.label_col = {"span": 6}
            form_component.wrapper_col = {"span": 18}

            action_component.set_modal(
                lambda m: m.set_title(name)
                .set_width(width)
                .set_body(form_component)
                .set_actions(actions)
                .set_destroy_on_close(destroy_on_close)
            )

        elif action_type == "drawer":
            init_api = self.build_init_api(params, uri_key)
            width = item.get_width()
            destroy_on_close = item.get_destroy_on_close()
            body = await item.get_body(self.request)
            actions = await item.get_actions(self.request)

            form_component = Form().set_api(api).set_init_api(init_api).set_body(body)
            form_component.label_col = {"span": 6}
            form_component.wrapper_col = {"span": 18}

            action_component.set_drawer(
                lambda d: d.set_title(name)
                .set_width(width)
                .set_body(form_component)
                .set_actions(actions)
                .set_destroy_on_close(destroy_on_close)
            )

        elif action_type == "dropdown":
            overlay = await item.get_menu(self.request)
            overlay_style = item.get_overlay_style()
            placement = item.get_placement()
            trigger = item.get_trigger()
            arrow = item.get_arrow()

            action_component = (
                Dropdown()
                .set_label(name)
                .set_menu(overlay)
                .set_overlay_style(overlay_style)
                .set_placement(placement)
                .set_trigger(trigger)
                .set_arrow(arrow)
                .set_size(size)
                .set_type(button_type)
            )

            if icon:
                action_component.set_icon(icon)

        elif action_type == "switch":
            checked_children = item.get_checked_children()
            unchecked_children = item.get_unchecked_children()
            field_name = item.get_field_name()
            field_value = item.get_field_value()

            action_component.set_field_name(field_name).set_field_value(
                field_value
            ).set_checked_children(checked_children).set_un_checked_children(
                unchecked_children
            )

        if confirm_title:
            action_component.set_with_confirm(confirm_title, confirm_text, confirm_type)

        return action_component

    def _wrap_in_space(self, items: List[Any]) -> Space:
        """包装在 space 组件中"""
        return Space().set_body(items)

    def build_action_api(self, params: List[str], uri_key: str) -> str:
        """构建行为 API 地址"""
        api = self.request.url.path
        api_paths = api.split("/")

        new_api = api
        if len(api_paths) <= 2:
            return ""

        last_segment = api_paths[-1]
        if last_segment == "index":
            new_api = api.replace("/index", f"/action/{uri_key}", 1)
        elif last_segment == "create":
            new_api = api.replace("/create", f"/action/{uri_key}", 1)
        elif last_segment == "edit":
            new_api = api.replace("/edit", f"/action/{uri_key}", 1)
        elif last_segment == "detail":
            new_api = api.replace("/detail", f"/action/{uri_key}", 1)
        elif last_segment == "form":
            last_path = api_paths[-2]
            new_api = api.replace(f"{last_path}/form", f"action/{uri_key}", 1)

        # 添加查询参数
        params_uri = ""
        for param in params:
            params_uri += f"{param}=${{{param}}}&"

        if params_uri:
            new_api = f"{new_api}?{params_uri.rstrip('&')}"

        return new_api

    def build_init_api(self, params: List[str], uri_key: str) -> str:
        """构建初始化数据 API 地址"""
        api = self.request.url.path
        api_paths = api.split("/")

        new_api = api
        if len(api_paths) <= 2:
            return ""

        last_segment = api_paths[-1]
        if last_segment == "index":
            new_api = api.replace("/index", f"/action/{uri_key}/values", 1)
        elif last_segment == "create":
            new_api = api.replace("/create", f"/action/{uri_key}/values", 1)
        elif last_segment == "edit":
            new_api = api.replace("/edit", f"/action/{uri_key}/values", 1)
        elif last_segment == "detail":
            new_api = api.replace("/detail", f"/action/{uri_key}/values", 1)
        elif last_segment == "form":
            last_path = api_paths[-2]
            new_api = api.replace(f"{last_path}/form", f"action/{uri_key}/values", 1)

        # 添加查询参数
        params_uri = ""
        for param in params:
            params_uri += f"{param}=${{{param}}}&"

        if params_uri:
            new_api = f"{new_api}?{params_uri.rstrip('&')}"

        return new_api
