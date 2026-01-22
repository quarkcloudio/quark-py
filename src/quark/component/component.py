import hashlib
import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict


def to_camel(string: str) -> str:
    parts = string.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


class Component(BaseModel):

    # 组件配置
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="allow",
    )

    def model_dump(self, exclude_none=True, **kwargs):
        """重写 model_dump 方法来默认排除 None 值"""
        return super().model_dump(exclude_none=exclude_none, **kwargs)

    # 组件名称
    component: Optional[str] = None

    # 组件key
    componentkey: Optional[str] = None

    # 组件样式
    style: Optional[dict] = None

    def set_component(self, component: str) -> "Component":
        self.component = component
        self.set_key(component, crypt=True)
        return self

    def set_key(self, key: Optional[str] = "", crypt: bool = True) -> "Component":
        if not key:
            key = str(uuid.uuid4())
        if crypt:
            md5_hash = hashlib.md5()
            md5_hash.update(key.encode("utf-8"))
            key = md5_hash.hexdigest()
        self.componentkey = key
        return self
