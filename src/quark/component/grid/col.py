from pydantic import Field, model_validator
from typing import Any, Dict, Optional, Union
from ..component import Component

class Col(Component):
    component: str = "col"
    flex: str = Field("", description="布局属性")
    offset: int = Field(0, description="栅格左侧的间隔格数，间隔内不可以有栅格")
    order: int = Field(0, description="栅格顺序")
    pull: int = Field(0, description="栅格向左移动格数")
    push: int = Field(0, description="栅格向右移动格数")
    span: int = Field(0, description="栅格占位格数，为 0 时相当于 display: none")
    xs: Optional[Union[int, Dict[str, Any]]] = Field(None, description="屏幕 < 576px 响应式栅格，可为栅格数或一个包含其他属性的对象")
    sm: Optional[Union[int, Dict[str, Any]]] = Field(None, description="屏幕 ≥ 576px 响应式栅格，可为栅格数或一个包含其他属性的对象")
    md: Optional[Union[int, Dict[str, Any]]] = Field(None, description="屏幕 ≥ 768px 响应式栅格，可为栅格数或一个包含其他属性的对象")
    lg: Optional[Union[int, Dict[str, Any]]] = Field(None, description="屏幕 ≥ 992px 响应式栅格，可为栅格数或一个包含其他属性的对象")
    xl: Optional[Union[int, Dict[str, Any]]] = Field(None, description="屏幕 ≥ 1200px 响应式栅格，可为栅格数或一个包含其他属性的对象")
    xxl: Optional[Union[int, Dict[str, Any]]] = Field(None, description="屏幕 ≥ 1600px 响应式栅格，可为栅格数或一个包含其他属性的对象")
    body: Optional[Any] = Field(None, description="卡牌内容")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_flex(self, flex: str):
        # 设置布局属性
        self.flex = flex
        return self

    def set_offset(self, offset: int):
        # 设置栅格左侧的间隔格数
        self.offset = offset
        return self

    def set_order(self, order: int):
        # 设置栅格顺序
        self.order = order
        return self

    def set_pull(self, pull: int):
        # 设置栅格向左移动格数
        self.pull = pull
        return self

    def set_push(self, push: int):
        # 设置栅格向右移动格数
        self.push = push
        return self

    def set_span(self, span: int):
        # 设置栅格占位格数
        self.span = span
        return self

    def set_xs(self, xs: Union[int, Dict[str, Any]]):
        # 设置屏幕 < 576px 响应式栅格
        self.xs = xs
        return self

    def set_sm(self, sm: Union[int, Dict[str, Any]]):
        # 设置屏幕 ≥ 576px 响应式栅格
        self.sm = sm
        return self

    def set_md(self, md: Union[int, Dict[str, Any]]):
        # 设置屏幕 ≥ 768px 响应式栅格
        self.md = md
        return self

    def set_lg(self, lg: Union[int, Dict[str, Any]]):
        # 设置屏幕 ≥ 992px 响应式栅格
        self.lg = lg
        return self

    def set_xl(self, xl: Union[int, Dict[str, Any]]):
        # 设置屏幕 ≥ 1200px 响应式栅格
        self.xl = xl
        return self

    def set_xxl(self, xxl: Union[int, Dict[str, Any]]):
        # 设置屏幕 ≥ 1600px 响应式栅格
        self.xxl = xxl
        return self

    def set_body(self, body: Any):
        # 设置卡牌内容
        self.body = body
        return self