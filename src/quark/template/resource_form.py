from typing import Any, Dict, List, Optional, Union
from abc import ABC, abstractmethod


class Context:
    """
    模拟 quark.Context 上下文对象
    """

    def __init__(
        self,
        param_data: Dict[str, str] = None,
        is_creating: bool = False,
        is_editing: bool = False,
        template: Any = None,
    ):
        self.param_data = param_data or {}
        self.is_creating = is_creating
        self.is_editing = is_editing
        self.template = template

    def param(self, key: str) -> str:
        return self.param_data.get(key, "")

    def is_creating(self) -> bool:
        return self.is_creating

    def is_editing(self) -> bool:
        return self.is_editing

    def cjson_error(self, message: str):
        return {"error": message}

    def cjson_redirect_to(self, message: str, url: str):
        return {"message": message, "redirect": url}


class CardComponent:
    """
    模拟 card.Component 卡片组件
    """

    def __init__(self):
        self.title = ""
        self.header_bordered = False
        self.extra = None
        self.body = None

    def init(self):
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_header_bordered(self, enable: bool):
        self.header_bordered = enable
        return self

    def set_extra(self, extra: Any):
        self.extra = extra
        return self

    def set_body(self, body: Any):
        self.body = body
        return self


class TabsComponent:
    """
    模拟 tabs.Component 标签页组件
    """

    def __init__(self):
        self.tab_panes = []
        self.tab_bar_extra_content = None

    def init(self):
        return self

    def set_tab_panes(self, tab_panes: List[Any]):
        self.tab_panes = tab_panes
        return self

    def set_tab_bar_extra_content(self, content: Any):
        self.tab_bar_extra_content = content
        return self


class FormComponent:
    """
    模拟 form.Component 表单组件
    """

    def __init__(self):
        self.style = {}
        self.api = ""
        self.actions = []
        self.body = None
        self.initial_values = {}

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_api(self, api: str):
        self.api = api
        return self

    def set_actions(self, actions: List[Any]):
        self.actions = actions
        return self

    def set_body(self, body: Any):
        self.body = body
        return self

    def set_initial_values(self, data: Dict[str, Any]):
        self.initial_values = data
        return self


class Resourcer(ABC):
    """
    模拟 types.Resourcer 接口
    """

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_form(self) -> FormComponent:
        pass

    @abstractmethod
    def get_index_path(self) -> str:
        pass


class Template:
    """
    对应 Go 中的 Template 结构体，包含表单相关的方法
    """

    def form_api(self, ctx: Context) -> str:
        """
        获取表单提交 API 地址
        """
        return ""

    def form_title(self, ctx: Context) -> str:
        """
        获取表单标题
        """
        resourcer: Resourcer = ctx.template
        title = resourcer.get_title()
        if ctx.is_creating:
            return f"创建{title}"
        elif ctx.is_editing:
            return f"编辑{title}"
        else:
            return title

    def form_component_render(
        self,
        ctx: Context,
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
                return self.form_within_tabs(ctx, title, extra, api, fields, actions, data)
        return self.form_within_card(ctx, title, extra, api, fields, actions, data)

    def form_within_card(
        self,
        ctx: Context,
        title: str,
        extra: Any,
        api: str,
        fields: Any,
        actions: List[Any],
        data: Dict[str, Any],
    ) -> CardComponent:
        """
        在卡片中渲染表单
        """
        resourcer: Resourcer = ctx.template
        form = (
            resourcer.get_form()
            .set_style({"padding": "24px"})
            .set_api(api)
            .set_actions(actions)
            .set_body(fields)
            .set_initial_values(data)
        )

        return (
            CardComponent()
            .init()
            .set_title(title)
            .set_header_bordered(True)
            .set_extra(extra)
            .set_body(form)
        )

    def form_within_tabs(
        self,
        ctx: Context,
        title: str,
        extra: Any,
        api: str,
        fields: Any,
        actions: List[Any],
        data: Dict[str, Any],
    ) -> FormComponent:
        """
        在标签页中渲染表单
        """
        tabs_component = (
            TabsComponent().init().set_tab_panes(fields).set_tab_bar_extra_content(extra)
        )
        resourcer: Resourcer = ctx.template
        return (
            resourcer.get_form()
            .set_style({"backgroundColor": "#fff", "paddingBottom": "20px"})
            .set_api(api)
            .set_actions(actions)
            .set_body(tabs_component)
            .set_initial_values(data)
        )

    def before_form_showing(self, ctx: Context) -> Dict[str, Any]:
        """
        表单显示前回调
        """
        return {}

    def form_handle(
        self, ctx: Context, query: Any, data: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        表单提交处理
        """
        return StoreRequest().handle(ctx, data)

    def before_saving(
        self, ctx: Context, submit_data: Dict[str, Any]
    ) -> (Dict[str, Any], Optional[Exception]):
        """
        保存数据前回调
        """
        return submit_data, None

    def after_imported(
        self, ctx: Context, id_: int, data: Dict[str, Any], result: Any
    ) -> Optional[Exception]:
        """
        导入数据后回调
        """
        return None

    def after_saved(
        self, ctx: Context, id_: int, data: Dict[str, Any], result: Any
    ) -> Optional[Exception]:
        """
        保存数据后回调
        """
        return None

    def after_saved_redirect_to(
        self, ctx: Context, id_: int, data: Dict[str, Any], err: Optional[Exception]
    ) -> Dict[str, str]:
        """
        保存数据后跳转处理
        """
        if err:
            return ctx.cjson_error(str(err))

        index_path = getattr(ctx.template, "index_path", "/api/admin/:resource/index")
        redirect_url = "/layout/index?api=" + index_path
        redirect_url = redirect_url.replace(":resource", ctx.param("resource"))

        return ctx.cjson_redirect_to("操作成功", redirect_url)


class StoreRequest:
    """
    模拟 requests.StoreRequest 处理表单提交逻辑
    """

    def handle(self, ctx: Context, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        # 实际逻辑可替换为数据库插入
        return data