import hashlib
import json
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union
from ..element import Element

@dataclass
class ActivityConfig:
    Title: str = ""
    SubTitle: str = ""
    Action: Any = None
    Style: Dict[str, Any] = field(default_factory=dict)

@dataclass
class LoginComponent(Element):
    Api: str = ""
    Redirect: str = ""
    Logo: Any = None
    Title: str = ""
    SubTitle: str = ""
    BackgroundImageUrl: str = ""
    ActivityConfig: Optional[ActivityConfig] = None
    Values: Dict[str, Any] = field(default_factory=dict)
    InitialValues: Dict[str, Any] = field(default_factory=dict)
    Body: Any = None
    Actions: List[Any] = field(default_factory=list)

    def __post_init__(self):
        self.Component = "login"
        self.set_key("", True)

    def set_style(self, style: Dict[str, Any]):
        self.Style = style
        return self

    def set_api(self, api: str):
        self.Api = api
        return self

    def set_redirect(self, redirect: str):
        self.Redirect = redirect
        return self

    def set_logo(self, logo: Any):
        self.Logo = logo
        return self

    def set_title(self, title: str):
        self.Title = title
        return self

    def set_sub_title(self, subtitle: str):
        self.SubTitle = subtitle
        return self

    def set_background_image_url(self, url: str):
        self.BackgroundImageUrl = url
        return self

    def set_activity_config(self, config: ActivityConfig):
        self.ActivityConfig = config
        return self

    def set_initial_values(self, initial_values: Dict[str, Any]):
        data = initial_values.copy()

        # 模拟解析 body 中字段（如有必要可用类注册机制）
        if isinstance(self.Body, list):
            for item in self.Body:
                value = self._parse_initial_value(item, initial_values)
                if value is not None:
                    name = getattr(item, "Name", "")
                    if name:
                        data[name] = value

        for k, v in data.items():
            if isinstance(v, str):
                if "[" in v or "{" in v:
                    try:
                        data[k] = json.loads(v)
                    except Exception:
                        pass

        self.InitialValues = data
        return self

    def _parse_initial_value(self, item, initial_values):
        name = getattr(item, "Name", "")
        value = getattr(item, "Value", None)

        if not name:
            return None

        if getattr(item, "DefaultValue", None) is not None:
            value = item.DefaultValue

        if name in initial_values:
            value = initial_values[name]

        return value

    def set_body(self, body: Any):
        self.Body = body
        return self

    def set_actions(self, actions: List[Any]):
        self.Actions = actions
        return self
