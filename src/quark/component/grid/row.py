from pydantic import Field, model_validator
from typing import Any, Dict, Optional, Union, List
from .col import Col
from ..component import Component

class Row(Component):
    component: str = "row"
    align: str = Field("", description="垂直对齐方式")
    gutter: Optional[Union[int, Dict[str, int], List[int]]] = Field(None, description="栅格间隔")
    justify: str = Field("", description="水平排列方式")
    wrap: bool = Field(True, description="是否自动换行")
    col: Optional[Col] = Field(None, description="设置列")
    body: Optional[Any] = Field(None, description="内容")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_align(self, align: str):
        # 设置垂直对齐方式
        self.align = align
        return self

    def set_gutter(self, gutter: Union[int, Dict[str, int], List[int]]):
        # 设置栅格间隔
        self.gutter = gutter
        return self

    def set_justify(self, justify: str):
        # 设置水平排列方式
        self.justify = justify
        return self

    def set_wrap(self, wrap: bool):
        # 设置是否自动换行
        self.wrap = wrap
        return self

    def set_col(self, col: Col):
        # 设置列
        self.col = col
        return self

    def set_body(self, body: Any):
        # 设置内容
        self.body = body
        return self