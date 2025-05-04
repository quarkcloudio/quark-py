from pydantic import Field, model_validator
from typing import Any, Dict, List, Optional
from ..component import Component

class PageContainer(Component):
    component: str = Field(default="pageContainer")
    content: Any = Field(None, description="内容区")
    extra_content: Optional[Any] = Field(None, description="额外内容区，位于 content 的右侧")
    tab_list: Optional[List[Dict[str, str]]] = Field(None, description="tab 标题列表")
    tab_active_key: Optional[str] = Field(None, description="当前高亮的 tab 项")
    tab_bar_extra_content: Optional[Any] = Field(None, description="tab bar 上额外的元素")
    header: Optional[Any] = Field(None, description="PageHeader 的所有属性")
    ghost: bool = Field(False, description="配置头部区域的背景颜色为透明")
    fixed_header: bool = Field(False, description="固定 pageHeader 的内容到顶部")
    affix_props: Optional[Any] = Field(None, description="固钉的配置，与 antd 完全相同")
    footer: Optional[Any] = Field(None, description="悬浮在底部的操作栏，传入一个数组，会自动加空格")
    body: Optional[Any] = Field(None, description="容器控件里面的内容")
    water_mark_props: Optional[Any] = Field(None, description="配置水印，Layout 会透传给 PageContainer，但是以 PageContainer 的配置优先")
    tab_props: Optional[Any] = Field(None, description="tab 的配置")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key("pageContainer")
        return self

    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_content(self, content: Any):
        # 设置内容区
        self.content = content
        return self

    def set_extra_content(self, extra_content: Any):
        # 设置额外内容区
        self.extra_content = extra_content
        return self

    def set_tab_list(self, tab_list: List[Dict[str, str]]):
        # 设置 tab 标题列表
        self.tab_list = tab_list
        return self

    def set_tab_active_key(self, tab_active_key: str):
        # 设置当前高亮的 tab 项
        self.tab_active_key = tab_active_key
        return self

    def set_tab_bar_extra_content(self, tab_bar_extra_content: Any):
        # 设置 tab bar 上额外的元素
        self.tab_bar_extra_content = tab_bar_extra_content
        return self

    def set_header(self, header: Any):
        # 设置 PageHeader 的所有属性
        self.header = header
        return self

    def set_ghost(self, ghost: bool):
        # 设置头部区域的背景颜色为透明
        self.ghost = ghost
        return self

    def set_fixed_header(self, fixed_header: bool):
        # 设置固定 pageHeader 的内容到顶部
        self.fixed_header = fixed_header
        return self

    def set_affix_props(self, affix_props: Any):
        # 设置固钉的配置
        self.affix_props = affix_props
        return self

    def set_footer(self, footer: Any):
        # 设置悬浮在底部的操作栏
        self.footer = footer
        return self

    def set_body(self, body: Any):
        # 设置容器控件里面的内容
        self.body = body
        return self

    def set_water_mark_props(self, water_mark_props: Any):
        # 设置配置水印
        self.water_mark_props = water_mark_props
        return self

    def set_tab_props(self, tab_props: Any):
        # 设置 tab 的配置
        self.tab_props = tab_props
        return self