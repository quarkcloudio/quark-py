from pydantic import Field, model_validator
from typing import Any, Optional, Union
from .base import Base


class Text(Base):
    component: str = "textField"

    addon_after: Optional[Any] = None
    addon_before: Optional[Any] = None
    allow_clear: bool = False
    bordered: bool = True
    default_value: Optional[Any] = None
    disabled: Optional[Union[bool, str]] = None
    id: str = None
    max_length: int = 200
    show_count: bool = False
    status: str = None
    prefix: Optional[Any] = None
    size: str = None
    suffix: Optional[Any] = None
    type: str = None
    value: Optional[Any] = None
    placeholder: str = "请输入"
    style: dict = Field(default_factory=dict)

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        self.set_width(200)
        return self

    def set_addon_after(self, addon_after: Any):
        self.addon_after = addon_after
        return self

    def set_addon_before(self, addon_before: Any):
        self.addon_before = addon_before
        return self

    def set_allow_clear(self, allow_clear: bool):
        self.allow_clear = allow_clear
        return self

    def set_bordered(self, bordered: bool):
        self.bordered = bordered
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_id(self, id: str):
        self.id = id
        return self

    def set_max_length(self, max_length: int):
        self.max_length = max_length
        return self

    def set_show_count(self, show_count: bool):
        self.show_count = show_count
        return self

    def set_status(self, status: str):
        self.status = status
        return self

    def set_placeholder(self, placeholder: str):
        self.placeholder = placeholder
        return self

    def set_prefix(self, prefix: Any):
        self.prefix = prefix
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_suffix(self, suffix: Any):
        self.suffix = suffix
        return self

    def set_type(self, type: str):
        self.type = type
        return self
