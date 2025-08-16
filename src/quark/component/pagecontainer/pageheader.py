from typing import Any, Dict, Optional

from pydantic import Field, model_validator

from ..component import Component


class PageHeader(Component):
    component: str = Field(default="pageHeader")
    avatar: Optional[Any] = Field(None, description="标题栏旁的头像")
    back_icon: Optional[Any] = Field(
        None, description="自定义 back icon ，如果为 false 不渲染 back icon"
    )
    breadcrumb: Optional[Any] = Field(None, description="面包屑的配置")
    breadcrumb_render: Optional[Any] = Field(None, description="自定义面包屑区域的内容")
    extra: Optional[Any] = Field(None, description="操作区，位于 title 行的行尾")
    footer: Optional[Any] = Field(
        None, description="PageHeader 的页脚，一般用于渲染 TabBar"
    )
    ghost: bool = Field(True, description="pageHeader 的类型，将会改变背景颜色")
    sub_title: Optional[str] = Field(None, description="自定义的二级标题文字")
    tags: Optional[Any] = Field(None, description="title 旁的 tag 列表")
    title: Optional[str] = Field(None, description="自定义标题文字")

    @model_validator(mode="after")
    def init(self):
        self.set_key("pageHeader")
        return self

    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_avatar(self, avatar: Any):
        # 设置头像
        self.avatar = avatar
        return self

    def set_back_icon(self, back_icon: Any):
        # 设置 back icon
        self.back_icon = back_icon
        return self

    def set_breadcrumb(self, breadcrumb: Any):
        # 设置面包屑配置
        self.breadcrumb = breadcrumb
        return self

    def set_breadcrumb_render(self, breadcrumb_render: Any):
        # 设置自定义面包屑区域的内容
        self.breadcrumb_render = breadcrumb_render
        return self

    def set_extra(self, extra: Any):
        # 设置操作区
        self.extra = extra
        return self

    def set_footer(self, footer: Any):
        # 设置页脚
        self.footer = footer
        return self

    def set_ghost(self, ghost: bool):
        # 设置 pageHeader 类型
        self.ghost = ghost
        return self

    def set_sub_title(self, sub_title: str):
        # 设置二级标题
        self.sub_title = sub_title
        return self

    def set_tags(self, tags: Any):
        # 设置 tag 列表
        self.tags = tags
        return self

    def set_title(self, title: str):
        # 设置标题
        self.title = title
        return self
