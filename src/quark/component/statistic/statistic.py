from pydantic import Field, model_validator
from typing import Any, Dict, Optional
from ..component import Component

class Statistic(Component):
    component: str = "statistic"
    decimal_separator: str = Field(".", description="小数点")
    group_separator: str = Field(",", description="千分位标识符")
    precision: int = Field(0, description="数值精度")
    prefix: str = Field("", description="数值的前缀")
    suffix: str = Field("", description="数值的后缀")
    title: str = Field("", description="标题")
    value: int = Field(0, description="数值内容")
    value_style: Dict[str, str] = Field({}, description="数值的样式")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_decimal_separator(self, decimal_separator: str):
        # 设置小数点
        self.decimal_separator = decimal_separator
        return self

    def set_group_separator(self, group_separator: str):
        # 设置千分位标识符
        self.group_separator = group_separator
        return self

    def set_precision(self, precision: int):
        # 设置数值精度
        self.precision = precision
        return self

    def set_prefix(self, prefix: str):
        # 设置数值的前缀
        self.prefix = prefix
        return self

    def set_suffix(self, suffix: str):
        # 设置数值的后缀
        self.suffix = suffix
        return self

    def set_title(self, title: str):
        # 设置标题
        self.title = title
        return self

    def set_value(self, value: int):
        # 设置数值内容
        self.value = value
        return self

    def set_value_style(self, value_style: Dict[str, str]):
        # 设置数值的样式
        self.value_style = value_style
        return self