from pydantic import Field
from typing import Any, List
from ..component.element import Element

class Component(Element):
    component: str = Field(default="footer")
    copyright: str = Field("", description="版权信息")
    links: List[dict] = Field([], description="链接信息")

    class Config:
        validate_by_name = True

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