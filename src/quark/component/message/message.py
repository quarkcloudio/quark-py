from pydantic import Field, model_validator
from typing import Any, Dict, Optional
from ..component import Component


class Message(Component):
    component: str = Field(default="message")
    class_name: str = Field(default=None)
    type: str = Field(default="success")
    content: Any = Field(default=None)
    duration: int = Field(default=0)
    icon: str = Field(default="")
    style: Optional[Dict[str, Any]] = Field(default=None)
    data: Any = Field(default=None)
    url: str = Field(default="")

    # 返回成功
    @classmethod
    def success(cls, content, data=None, url=""):
        return (
            cls().set_type("success").set_content(content).set_url(url).set_data(data)
        )

    # 返回失败
    @classmethod
    def error(cls, content, url=""):
        return cls().set_type("error").set_content(content).set_url(url)

    @model_validator(mode="after")
    def init(self):
        self.component = "message"
        self.type = "success"
        self.set_key("message", True)

        return self

    # Set ClassName
    def set_class_name(self, class_name: str):
        self.class_name = class_name
        return self

    # Set Type info | success | error | warning | loading
    def set_type(self, message_type: str):
        self.type = message_type
        return self

    # Set style.
    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    # 内容
    def set_content(self, content: Any):
        self.content = content
        return self

    # 自动关闭的延时，单位秒。设为 0 时不自动关闭
    def set_duration(self, duration: int):
        self.duration = duration
        return self

    # Set Icon
    def set_icon(self, icon: str):
        self.icon = icon
        return self

    # 设置返回数据
    def set_data(self, data: Any):
        self.data = data
        return self

    # 设置消息弹出后跳转链接
    def set_url(self, url: str):
        self.url = url
        return self
