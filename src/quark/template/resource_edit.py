from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod


class Context:
    """
    模拟 quark.Context 上下文对象
    """

    def __init__(self, path: str, is_editing: bool = True, template: Any = None):
        self.path = path
        self.is_editing_flag = is_editing
        self.template = template

    def path(self) -> str:
        return self.path

    def is_editing(self) -> bool:
        return self.is_editing_flag

    def param(self, key: str) -> str:
        # 示例中简化，实际应从 URL 参数中提取
        return "1"  # 假设默认 ID 为 1


class Resourcer(ABC):
    """
    模拟 types.Resourcer 接口
    """

    @abstractmethod
    def form_api(self, ctx: Context) -> str:
        pass

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def form_extra_actions(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def update_fields_within_components(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def form_actions(self, ctx: Context) -> List[Any]:
        pass

    @abstractmethod
    def form_component_render(
        self,
        ctx: Context,
        title: str,
        extra: Any,
        api: str,
        fields: List[Any],
        actions: List[Any],
        data: Dict[str, Any],
    ) -> Any:
        pass


class Template:
    """
    对应 Go 中的 Template 结构体，包含编辑表单相关的方法
    """

    def update_api(self, ctx: Context) -> str:
        """
        获取更新表单的接口地址
        """
        resourcer: Resourcer = ctx.template
        form_api = resourcer.form_api(ctx)
        if form_api:
            return form_api

        uri = ctx.path().split("/")
        if uri[-1] == "index":
            return ctx.path().replace("/index", "/save")

        return ctx.path().replace("/edit", "/save")

    def edit_value_api(self, ctx: Context) -> str:
        """
        编辑页面获取数据接口地址
        """
        uri = ctx.path().split("/")
        if uri[-1] == "index":
            return ctx.path().replace("/index", "/edit/values?id=${id}")

        return ctx.path().replace("/edit", "/edit/values?id=${id}")

    def update_component_render(self, ctx: Context, data: Dict[str, Any]) -> Any:
        """
        渲染编辑页组件
        """
        title = self.form_title(ctx)
        form_extra_actions = self.form_extra_actions(ctx)
        api = self.update_api(ctx)
        fields = self.update_fields_within_components(ctx)
        form_actions = self.form_actions(ctx)

        return ctx.template.form_component_render(
            ctx, title, form_extra_actions, api, fields, form_actions, data
        )

    def before_editing(self, ctx: Context, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        编辑页面显示前回调
        """
        return data

    def form_title(self, ctx: Context) -> str:
        """
        获取表单标题（从模板继承）
        """
        resourcer: Resourcer = ctx.template
        title = resourcer.get_title()
        if ctx.is_editing():
            return f"编辑{title}"
        return title

    def form_extra_actions(self, ctx: Context) -> List[Any]:
        """
        表单页右上角自定义区域行为（由模板实现）
        """
        return ctx.template.form_extra_actions(ctx)

    def update_fields_within_components(self, ctx: Context) -> List[Any]:
        """
        获取包裹在组件中的字段（由模板实现）
        """
        return ctx.template.update_fields_within_components(ctx)

    def form_actions(self, ctx: Context) -> List[Any]:
        """
        获取表单页行为按钮（由模板实现）
        """
        return ctx.template.form_actions(ctx)