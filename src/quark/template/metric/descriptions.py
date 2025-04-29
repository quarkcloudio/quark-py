from dataclasses import dataclass
from typing import Any
from ...component.descriptions.descriptions import Component as DescriptionsComponent

@dataclass
class Descriptions:
    title: str = None
    col: int = None

    def result(self, value: Any) -> DescriptionsComponent:
        return DescriptionsComponent().set_title(self.title).set_items(value)