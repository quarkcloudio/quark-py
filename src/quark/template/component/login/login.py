from pydantic import BaseModel, Field, field_validator
from typing import Any, Dict, List, Optional
import json
from ..component.element import Element

class ActivityConfig(BaseModel):
    title: str = ""
    sub_title: str = ""
    action: Any = None
    style: Dict[str, Any] = Field(default_factory=dict)

class Component(Element):
    api: str = ""
    redirect: str = ""
    logo: Any = None
    title: str = ""
    sub_title: str = ""
    background_image_url: str = None
    activity_config: Optional[ActivityConfig] = None
    values: Dict[str, Any] = Field(default_factory=dict)
    initial_values: Dict[str, Any] = Field(default_factory=dict)
    body: Any = None
    actions: List[Any] = Field(default_factory=list)
    component: str = "login"
    component_key: str = ""

    crypt: bool = Field(default=False, exclude=True)

    @field_validator('component_key', mode="before")
    def set_key(cls, v, values):
        crypt = values.get('crypt', False)
        return v if not crypt else cls._make_hex(v)

    @staticmethod
    def _make_hex(key: str) -> str:
        return key.encode().hex()

    # 设置方法（链式调用）
    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_api(self, api: str):
        self.api = api
        return self

    def set_redirect(self, redirect: str):
        self.redirect = redirect
        return self

    def set_logo(self, logo: Any):
        self.logo = logo
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_sub_title(self, sub_title: str):
        self.sub_title = sub_title
        return self

    def set_background_image_url(self, url: str):
        self.background_image_url = url
        return self

    def set_activity_config(self, config: ActivityConfig):
        self.activity_config = config
        return self

    def set_initial_values(self, initial_values: Dict[str, Any]):
        data = initial_values.copy()

        if isinstance(self.body, list):
            for item in self.body:
                value = self._parse_initial_value(item, initial_values)
                if value is not None:
                    name = getattr(item, "name", "")
                    if name:
                        data[name] = value

        for k, v in data.items():
            if isinstance(v, str) and ("[" in v or "{" in v):
                try:
                    data[k] = json.loads(v)
                except Exception:
                    pass

        self.initial_values = data
        return self

    def set_body(self, body: Any):
        self.body = body
        return self

    def set_actions(self, actions: List[Any]):
        self.actions = actions
        return self

    # 私有方法
    def _parse_initial_value(self, item, initial_values):
        name = getattr(item, "name", "")
        value = getattr(item, "value", None)

        if not name:
            return None

        if hasattr(item, "default_value") and item.default_value is not None:
            value = item.default_value

        if name in initial_values:
            value = initial_values[name]

        return value