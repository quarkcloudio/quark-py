from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod


class Context:
    """
    模拟 quark.Context 上下文对象
    """

    def __init__(self, path: str, is_detail: bool = True, template: Any = None):
        self.path = path
        self.is_detail_flag = is_detail
        self.template = template

    def path(self) -> str:
        return self.path

    def is_detail(self) -> bool:
        return self.is_detail_flag

    def param(self, key: str) -> str:
        # 示例中简化处理，实际应从 URL 参数中提取
        return "1"  # 假设默认 ID 为 1


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


class Resourcer(ABC):
    """
    模拟 types.Resourcer 接口
    """

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def detail_extra_actions(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def detail_fields_within_components(self, ctx: Context, field_type: Any, data: Dict[str, Any]) -> List[Any]:
        pass

    @abstractmethod
    def detail_actions(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def detail_within_card(
        self,
        ctx: Context,
        title: str,
        extra: Any,
        fields: List[Any],
        actions: List[Any],
        data: Dict[str, Any],
    ) -> CardComponent:
        pass

    @abstractmethod
    def detail_within_tabs(
        self,
        ctx: Context,
        title: str,
        extra: Any,
        fields: List[Any],
        actions: List[Any],
        data: Dict[str, Any],
    ) -> TabsComponent:
        pass


class Template:
    """
    对应 Go 中的 Template 结构体，包含详情页相关的方法
    """

    def detail_value_api(self, ctx: Context) -> str:
        """
        获取详情页数据接口地址
        """
        uri = ctx.path().split("/")
        if uri[-1] == "index":
            return ctx.path().replace("/index", "/detail/values?id=${id}")
        return ctx.path().replace("/detail", "/detail/values?id=${id}")

    def detail_title(self, ctx: Context) -> str:
        """
        获取详情页标题
        """
        resourcer: Resourcer = ctx.template
        title = resourcer.get_title()
        return f"{title}详情"

    def detail_component_render(self, ctx: Context, data: Dict[str, Any]) -> CardComponent:
        """
        渲染详情页组件
        """
        title = self.detail_title(ctx)
        form_extra_actions = self.detail_extra_actions(ctx)
        fields = self.detail_fields_within_components(ctx, None, data)
        form_actions = self.detail_actions(ctx)

        return self.detail_within_card(
            ctx, title, form_extra_actions, fields, form_actions, data
        )

    def detail_within_card(
        self,
        ctx: Context,
        title: str,
        extra: Any,
        fields: List[Any],
        actions: List[Any],
        data: Dict[str, Any],
    ) -> CardComponent:
        """
        在卡片中渲染详情页
        """
        return (
            CardComponent()
            .init()
            .set_title(title)
            .set_header_bordered(True)
            .set_extra(extra)
            .set_body(fields)
        )

    def detail_within_tabs(
        self,
        ctx: Context,
        title: str,
        extra: Any,
        fields: List[Any],
        actions: List[Any],
        data: Dict[str, Any],
    ) -> TabsComponent:
        """
        在标签页中渲染详情页
        """
        return (
            TabsComponent()
            .init()
            .set_tab_panes(fields)
            .set_tab_bar_extra_content(extra)
        )

    def before_detail_showing(self, ctx: Context, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        详情页显示前回调
        """
        return data

    def detail_extra_actions(self, ctx: Context) -> List[Any]:
        """
        详情页右上角自定义区域行为（由模板实现）
        """
        resourcer: Resourcer = ctx.template
        return resourcer.detail_extra_actions(ctx)

    def detail_fields_within_components(self, ctx: Context, field_type: Any, data: Dict[str, Any]) -> List[Any]:
        """
        获取包裹在组件中的详情页字段（由模板实现）
        """
        resourcer: Resourcer = ctx.template
        return resourcer.detail_fields_within_components(ctx, field_type, data)

    def detail_actions(self, ctx: Context) -> List[Any]:
        """
        获取详情页操作按钮（由模板实现）
        """
        resourcer: Resourcer = ctx.template
        return resourcer.detail_actions(ctx)