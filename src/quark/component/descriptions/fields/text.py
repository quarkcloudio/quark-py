from pydantic import Field, model_validator
from typing import Any, Dict, Optional
from ...component import Component

class Text(Component):
    component: str = "text"
    label: str = Field("", description="内容的描述")
    tooltip: str = Field("", description="内容的补充描述，hover 后显示")
    ellipsis: bool = Field(False, description="是否自动缩略")
    copyable: bool = Field(False, description="是否支持复制")
    span: int = Field(1, description="列数")
    value_type: str = Field("text", description="值类型")
    value_enum: str = Field("", description="值枚举")
    data_index: str = Field("", description="索引")
    value: Optional[Any] = Field(None, description="设置保存值")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self
    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_label(self, label: str):
        # 设置内容的描述
        self.label = label
        return self

    def set_tooltip(self, tooltip: str):
        # 设置内容的补充描述，hover 后显示
        self.tooltip = tooltip
        return self

    def set_ellipsis(self, ellipsis: bool):
        # 设置是否自动缩略
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        # 设置是否支持复制
        self.copyable = copyable
        return self

    def set_span(self, span: int):
        # 设置列数
        self.span = span
        return self

    def set_value_type(self, value_type: str):
        # 设置值类型
        self.value_type = value_type
        return self

    def set_value_enum(self, value_enum: str):
        # 设置值枚举
        self.value_enum = value_enum
        return self

    def set_data_index(self, data_index: str):
        # 设置索引
        self.data_index = data_index
        return self

    def set_value(self, value: Any):
        # 设置保存值
        self.value = value
        return self