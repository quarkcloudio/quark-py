from pydantic import Field, model_validator
from typing import List
from ..component import Component

class Footer(Component):
    component: str = Field(default="footer")
    copyright: str = Field("", description="版权信息")
    links: List[dict] = Field([], description="链接信息")

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: dict):
        """Set style."""
        self.style = style
        return self

    def set_copyright(self, copyright: str):
        """版权信息"""
        self.copyright = copyright
        return self

    def set_links(self, links: List[dict]):
        """版权信息"""
        self.links = links
        return self