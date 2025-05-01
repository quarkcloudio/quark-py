from typing import Any, Dict, List, Optional, Union
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Context:
    """模拟 Quark.Context 上下文对象"""
    path: str = ""
    param_values: Dict[str, Any] = None

    def path(self) -> str:
        return self.path

    def cjson_success(self, message: str):
        return {"status": "success", "message": message}

    def cjson_error(self, message: str):
        return {"status": "error", "message": message}

    def param(self, key: str) -> str:
        return self.param_values.get(key, "")


class Actioner(ABC):
    """行为接口"""

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_with_loading(self) -> bool:
        pass

    @abstractmethod
    def get_reload(self) -> bool:
        pass

    @abstractmethod
    def get_uri_key(self) -> str:
        pass

    @abstractmethod
    def get_api(self) -> str:
        pass

    @abstractmethod
    def get_api_params(self) -> List[str]:
        pass

    @abstractmethod
    def get_action_type(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> str:
        pass

    @abstractmethod
    def get_icon(self) -> str:
        pass

    @abstractmethod
    def get_confirm_title(self) -> str:
        pass

    @abstractmethod
    def get_confirm_text(self) -> str:
        pass

    @abstractmethod
    def get_confirm_type(self) -> str:
        pass

    @abstractmethod
    def shown_on_index(self) -> bool:
        pass

    @abstractmethod
    def shown_on_index_table_row(self) -> bool:
        pass

    @abstractmethod
    def shown_on_index_table_alert(self) -> bool:
        pass

    @abstractmethod
    def shown_on_form(self) -> bool:
        pass

    @abstractmethod
    def shown_on_detail(self) -> bool:
        pass

    @abstractmethod
    def shown_on_detail_extra(self) -> bool:
        pass

    @abstractmethod
    def get_href(self, ctx: Context) -> str:
        pass

    @abstractmethod
    def get_target(self, ctx: Context) -> str:
        pass

    @abstractmethod
    def get_width(self) -> int:
        pass

    @abstractmethod
    def get_destroy_on_close(self) -> bool:
        pass

    @abstractmethod
    def get_body(self, ctx: Context) -> Any:
        pass

    @abstractmethod
    def get_actions(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def get_menu(self, ctx: Context) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_overlay_style(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_placement(self) -> str:
        pass

    @abstractmethod
    def get_trigger(self) -> List[str]:
        pass

    @abstractmethod
    def get_arrow(self) -> bool:
        pass

    @abstractmethod
    def get_checked_children(self) -> Union[str, Any]:
        pass

    @abstractmethod
    def get_unchecked_children(self) -> Union[str, Any]:
        pass

    @abstractmethod
    def get_field_name(self) -> str:
        pass

    @abstractmethod
    def get_field_value(self) -> Any:
        pass

    @abstractmethod
    def get_cancel_text(self) -> str:
        pass

    @abstractmethod
    def get_submit_text(self) -> str:
        pass

    @abstractmethod
    def get_api_type(self) -> str:
        pass

    @abstractmethod
    def get_target_blank(self) -> bool:
        pass


class TemplateActionBuilder:
    """
    对应 Go 中的 Template 结构体，处理资源行为逻辑
    """

    def __init__(self):
        self.template = None  # 类型为 Resourcer

    def index_table_actions(self, ctx: Context) -> List[Any]:
        """获取列表页顶部工具栏中的动作"""
        items = []
        actions = self._get_actions(ctx)

        for action in actions:
            if isinstance(action, Actioner) and action.shown_on_index():
                items.append(self.build_action(ctx, action))

        return self._wrap_in_space(items)

    def index_table_row_actions(self, ctx: Context) -> List[Any]:
        """获取列表页行内动作"""
        items = []
        actions = self._get_actions(ctx)

        for action in actions:
            if isinstance(action, Actioner) and action.shown_on_index_table_row():
                items.append(self.build_action(ctx, action))

        return items

    def index_table_alert_actions(self, ctx: Context) -> List[Any]:
        """获取多选弹出层动作"""
        items = []
        actions = self._get_actions(ctx)

        for action in actions:
            if isinstance(action, Actioner) and action.shown_on_index_table_alert():
                items.append(self.build_action(ctx, action))

        return items

    def form_actions(self, ctx: Context) -> List[Any]:
        """获取表单页动作"""
        items = []
        actions = self._get_actions(ctx)

        for action in actions:
            if isinstance(action, Actioner) and action.shown_on_form():
                items.append(self.build_action(ctx, action))

        return items

    def detail_actions(self, ctx: Context) -> List[Any]:
        """获取详情页动作"""
        items = []
        actions = self._get_actions(ctx)

        for action in actions:
            if isinstance(action, Actioner) and action.shown_on_detail():
                items.append(self.build_action(ctx, action))

        return items

    def build_action(self, ctx: Context, item: Actioner) -> Any:
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
            api = self.build_action_api(ctx, params, uri_key)

        action_component = ActionComponent().init().set_label(name).set_with_loading(with_loading)

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
            href = item.get_href(ctx)
            target = item.get_target(ctx)
            action_component.set_link(href, target)

        elif action_type == "modal":
            modal_actioner = item
            init_api = self.build_init_api(ctx, params, uri_key)
            width = modal_actioner.get_width()
            destroy_on_close = modal_actioner.get_destroy_on_close()
            body = modal_actioner.get_body(ctx)
            actions = modal_actioner.get_actions(ctx)

            form_component = FormComponent().init().set_api(api).set_init_api(init_api).set_body(body).set_actions(actions)
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
            init_api = self.build_init_api(ctx, params, uri_key)
            width = drawer_actioner.get_width()
            destroy_on_close = drawer_actioner.get_destroy_on_close()
            body = drawer_actioner.get_body(ctx)
            actions = drawer_actioner.get_actions(ctx)

            form_component = FormComponent().init().set_api(api).set_init_api(init_api).set_body(body).set_actions(actions)
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
            overlay = dropdown_actioner.get_menu(ctx)
            overlay_style = dropdown_actioner.get_overlay_style()
            placement = dropdown_actioner.get_placement()
            trigger = dropdown_actioner.get_trigger()
            arrow = dropdown_actioner.get_arrow()

            action_component = DropdownComponent().init() \
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

    def _get_actions(self, ctx: Context) -> List[Actioner]:
        """抽象方法，子类实现具体行为"""
        template = ctx.template
        return template.actions(ctx)

    def _wrap_in_space(self, items: List[Any]) -> SpaceComponent:
        """包装在 space 组件中"""
        return SpaceComponent().init().set_body(items)

    def build_action_api(self, ctx: Context, params: List[str], uri_key: str) -> str:
        """构建行为 API 地址"""
        api = ctx.path
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

    def build_init_api(self, ctx: Context, params: List[str], uri_key: str) -> str:
        """构建初始化数据 API 地址"""
        api = ctx.path
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


class ActionComponent:
    def __init__(self):
        self.label = ""
        self.with_loading = False
        self.reload = False
        self.api = ""
        self.action_type = ""
        self.type_ = ""
        self.size = ""
        self.icon = ""
        self.confirm_title = ""
        self.confirm_text = ""
        self.confirm_type = ""

    def init(self):
        return self

    def set_label(self, label: str):
        self.label = label
        return self

    def set_with_loading(self, with_loading: bool):
        self.with_loading = with_loading
        return self

    def set_reload(self, reload: bool):
        self.reload = reload
        return self

    def set_api(self, api: str):
        self.api = api
        return self

    def set_action_type(self, action_type: str):
        self.action_type = action_type
        return self

    def set_type(self, type_: str, ghost: bool = False):
        self.type_ = type_
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_icon(self, icon: str):
        self.icon = icon
        return self

    def set_link(self, href: str, target: str):
        self.href = href
        self.target = target
        return self

    def set_modal(self, modal_builder: Callable):
        self.modal_builder = modal_builder
        return self

    def set_drawer(self, drawer_builder: Callable):
        self.drawer_builder = drawer_builder
        return self

    def set_dropdown(self, dropdown_builder: Callable):
        self.dropdown_builder = dropdown_builder
        return self

    def set_switch_props(self, field_name: str, field_value: Any, checked_children: Any, unchecked_children: Any):
        self.field_name = field_name
        self.field_value = field_value
        self.checked_children = checked_children
        self.unchecked_children = unchecked_children
        return self

    def set_with_confirm(self, title: str, text: str, confirm_type: str):
        self.confirm_title = title
        self.confirm_text = text
        self.confirm_type = confirm_type
        return self


class ModalComponent:
    def __init__(self):
        self.title = ""
        self.init_api = ""
        self.width = 520
        self.body = None
        self.actions = []
        self.destroy_on_close = False

    def init(self):
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_init_api(self, init_api: str):
        self.init_api = init_api
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def set_body(self, body: Any):
        self.body = body
        return self

    def set_actions(self, actions: List[Any]):
        self.actions = actions
        return self

    def set_destroy_on_close(self, destroy: bool):
        self.destroy_on_close = destroy
        return self


class DrawerComponent:
    def __init__(self):
        self.title = ""
        self.init_api = ""
        self.width = 520
        self.body = None
        self.actions = []
        self.destroy_on_close = False

    def init(self):
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_init_api(self, init_api: str):
        self.init_api = init_api
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def set_body(self, body: Any):
        self.body = body
        return self

    def set_actions(self, actions: List[Any]):
        self.actions = actions
        return self

    def set_destroy_on_close(self, destroy: bool):
        self.destroy_on_close = destroy
        return self


class DropdownComponent:
    def __init__(self):
        self.label = ""
        self.overlay_style = {}
        self.placement = ""
        self.trigger = []
        self.arrow = False
        self.type_ = ""
        self.size = ""
        self.icon = ""

    def init(self):
        return self

    def set_label(self, label: str):
        self.label = label
        return self

    def set_menu(self, menu: List[Dict[str, Any]]):
        self.menu = menu
        return self

    def set_overlay_style(self, style: Dict[str, Any]):
        self.overlay_style = style
        return self

    def set_placement(self, placement: str):
        self.placement = placement
        return self

    def set_trigger(self, trigger: List[str]):
        self.trigger = trigger
        return self

    def set_arrow(self, enable: bool):
        self.arrow = enable
        return self

    def set_type(self, type_: str, ghost: bool = False):
        self.type_ = type_
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_icon(self, icon: str):
        self.icon = icon
        return self


class FormComponent:
    def __init__(self):
        self.key = ""
        self.style = {}
        self.api = ""
        self.init_api = ""
        self.api_type = "POST"
        self.target_blank = False
        self.body = None
        self.initial_values = {}
        self.label_col = {}
        self.wrapper_col = {}

    def init(self):
        return self

    def set_key(self, key: str, is_hidden: bool):
        self.key = key
        return self

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_api(self, api: str):
        self.api = api
        return self

    def set_init_api(self, init_api: str):
        self.init_api = init_api
        return self

    def set_api_type(self, api_type: str):
        self.api_type = api_type
        return self

    def set_target_blank(self, target_blank: bool):
        self.target_blank = target_blank
        return self

    def set_body(self, body: Any):
        self.body = body
        return self

    def set_initial_values(self, values: Dict[str, Any]):
        self.initial_values = values
        return self

    def set_label_col(self, col: Dict[str, Any]):
        self.label_col = col
        return self

    def set_wrapper_col(self, col: Dict[str, Any]):
        self.wrapper_col = col
        return self


class SpaceComponent:
    def __init__(self):
        self.body = []

    def init(self):
        return self

    def set_body(self, body: List[Any]):
        self.body = body
        return self


class DescriptionsComponent:
    def __init__(self):
        self.body = []

    def init(self):
        return self

    def set_body(self, body: List[Any]):
        self.body = body
        return self