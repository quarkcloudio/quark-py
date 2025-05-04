from pydantic import Field, model_validator
from typing import Any, Dict, Optional
from ..component import Component

class Card(Component):
    component: str = Field(default="card")
    title: str = Field("", description="标题文字")
    sub_title: str = Field("", description="二级标题文字")
    tip: str = Field("", description="标题右侧图标 hover 提示信息")
    extra: Optional[Any] = Field(None, description="右上角自定义区域")
    layout: str = Field("default", description="内容布局，支持垂直居中 default | center")
    loading: bool = Field(False, description="加载中，支持自定义 loading 样式")
    col_span: Optional[Any] = Field(24, description="栅格布局宽度，24 栅格，支持指定宽度 px 或百分比, 支持响应式的对象写法 { xs: 8, sm: 16, md: 24}")
    gutter: Optional[Any] = Field(0, description="栅格布局宽度，24 栅格，支持指定宽度 px 或百分比, 支持响应式的对象写法 { xs: 8, sm: 16, md: 24}")
    split: str = Field("", description="拆分卡片的方向, vertical | horizontal")
    bordered: bool = Field(True, description="是否有边框")
    ghost: bool = Field(False, description="幽灵模式，即是否取消卡片内容区域的 padding 和 卡片的背景颜色")
    header_bordered: bool = Field(True, description="页头是否有分割线")
    collapsible: bool = Field(False, description="页头是否有分割线")
    default_collapsed: bool = Field(False, description="默认折叠, 受控时无效")
    body: Optional[Any] = Field(None, description="卡牌内容")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key("action")
        return self
    
    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_title(self, title: str):
        # 设置标题文字
        self.title = title
        return self

    def set_sub_title(self, sub_title: str):
        # 设置二级标题文字
        self.sub_title = sub_title
        return self

    def set_tip(self, tip: str):
        # 设置标题右侧图标 hover 提示信息
        self.tip = tip
        return self

    def set_extra(self, extra: Any):
        # 设置右上角自定义区域
        self.extra = extra
        return self

    def set_layout(self, layout: str):
        # 设置内容布局
        self.layout = layout
        return self

    def set_loading(self, loading: bool):
        # 设置加载中状态
        self.loading = loading
        return self

    def set_col_span(self, col_span: Any):
        # 设置栅格布局宽度
        self.col_span = col_span
        return self

    def set_gutter(self, gutter: Any):
        # 设置栅格布局宽度
        self.gutter = gutter
        return self

    def set_split(self, split: str):
        # 设置拆分卡片的方向
        self.split = split
        return self

    def set_bordered(self, bordered: bool):
        # 设置是否有边框
        self.bordered = bordered
        return self

    def set_ghost(self, ghost: bool):
        # 设置幽灵模式
        self.ghost = ghost
        return self

    def set_header_bordered(self, header_bordered: bool):
        # 设置页头是否有分割线
        self.header_bordered = header_bordered
        return self

    def set_collapsible(self, collapsible: bool):
        # 设置页头是否有分割线
        self.collapsible = collapsible
        return self

    def set_default_collapsed(self, default_collapsed: bool):
        # 设置默认折叠状态
        self.default_collapsed = default_collapsed
        return self

    def set_body(self, body: Any):
        # 设置卡牌内容
        self.body = body
        return self