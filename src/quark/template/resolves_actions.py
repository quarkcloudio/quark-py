from flask import request
from dataclasses import dataclass
from typing import Any, List, Optional
from .action.action import Action
from ..component.action.action import Action as ActionComponent
from ..component.form.form import Form as FormComponent
from ..component.dropdown.dropdown import Dropdown as DropdownComponent
from ..component.space.space import Space as SpaceComponent

@dataclass
class ResolvesActions:

    # 行为
    actions: Optional[Any] = None

    def set_actions(self, actions) -> 'ResolvesActions':
        """设置行为"""
        self.actions = actions

        return self

    def index_table_actions(self) -> List[Any]:
        """获取列表页顶部工具栏中的动作"""
        items = []
        actions = self._get_actions()

        for action in actions:
            if isinstance(action, Action) and action.shown_on_index():
                items.append(self.build_action(action))

        return self._wrap_in_space(items)

    def index_table_row_actions(self) -> List[Any]:
        """获取列表页行内动作"""
        items = []
        actions = self._get_actions()

        for action in actions:
            if isinstance(action, Action) and action.shown_on_index_table_row():
                items.append(self.build_action(action))

        return items

    def index_table_alert_actions(self) -> List[Any]:
        """获取多选弹出层动作"""
        items = []
        actions = self._get_actions()

        for action in actions:
            if isinstance(action, Action) and action.shown_on_index_table_alert():
                items.append(self.build_action(action))

        return items

    def form_actions(self) -> List[Any]:
        """获取表单页动作"""
        items = []
        actions = self._get_actions()

        for action in actions:
            if isinstance(action, Action) and action.shown_on_form():
                items.append(self.build_action(action))

        return items

    def detail_actions(self) -> List[Any]:
        """获取详情页动作"""
        items = []
        actions = self._get_actions()

        for action in actions:
            if isinstance(action, Action) and action.shown_on_detail():
                items.append(self.build_action(action))

        return items

    def build_action(self, item: Action) -> Any:
        """构建行为组件（支持 link/modal/drawer/dropdown/switch 等）"""
        name = item.get_name()
        with_loading = item.get_with_loading()
        reload = item.get_reload()
        uri_key = item.get_uri_key()
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

        action_component = ActionComponent().set_label(name).set_with_loading(with_loading)

        if reload:
            action_component.set_reload(reload)

        if action_type:
            action_component.set_action_type(action_type)

        if button_type:
            action_component.set_type(button_type)

        if size:
            action_component.set_size(size)

        if icon:
            action_component.set_icon(icon)

        # 特定行为类型渲染
        if action_type == "link":
            href = item.get_href()
            target = item.get_target()
            action_component.set_link(href, target)

        elif action_type == "modal":
            modal_actioner = item
            init_api = self.build_init_api(params, uri_key)
            width = modal_actioner.get_width()
            destroy_on_close = modal_actioner.get_destroy_on_close()
            body = modal_actioner.get_body()
            actions = modal_actioner.get_actions()

            form_component = FormComponent().set_api(api).set_init_api(init_api).set_body(body).set_actions(actions)
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
            drawer_actioner = item
            init_api = self.build_init_api(params, uri_key)
            width = drawer_actioner.get_width()
            destroy_on_close = drawer_actioner.get_destroy_on_close()
            body = drawer_actioner.get_body()
            actions = drawer_actioner.get_actions()

            form_component = FormComponent().set_api(api).set_init_api(init_api).set_body(body).set_actions(actions)
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
            dropdown_actioner = item
            overlay = dropdown_actioner.get_menu()
            overlay_style = dropdown_actioner.get_overlay_style()
            placement = dropdown_actioner.get_placement()
            trigger = dropdown_actioner.get_trigger()
            arrow = dropdown_actioner.get_arrow()

            action_component = DropdownComponent() \
                .set_label(name) \
                .set_menu(overlay) \
                .set_overlay_style(overlay_style) \
                .set_placement(placement) \
                .set_trigger(trigger) \
                .set_arrow(arrow) \
                .set_type(button_type) \
                .set_size(size)

            if icon:
                action_component.set_icon(icon)

        elif action_type == "switch":
            switch_actioner = item
            checked_children = switch_actioner.get_checked_children()
            unchecked_children = switch_actioner.get_unchecked_children()
            field_name = switch_actioner.get_field_name()
            field_value = switch_actioner.get_field_value()

            action_component.set_switch_props(
                field_name=field_name,
                field_value=field_value,
                checked_children=checked_children,
                unchecked_children=unchecked_children
            )

        if confirm_title:
            action_component.set_with_confirm(confirm_title, confirm_text, confirm_type)

        return action_component

    def _get_actions(self) -> List[Any]:
        """抽象方法，子类实现具体行为"""
        return self.actions

    def _wrap_in_space(self, items: List[Any]) -> SpaceComponent:
        """包装在 space 组件中"""
        return SpaceComponent().set_body(items)

    def build_action_api(self, params: List[str], uri_key: str) -> str:
        """构建行为 API 地址"""
        api = request.path
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
        api = request.path
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