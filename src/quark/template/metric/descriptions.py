from typing import Any, Optional

from pydantic import BaseModel

from ...component.descriptions.descriptions import Descriptions as DescriptionsComponent


class Descriptions(BaseModel):
    title: Optional[str] = None
    col: Optional[int] = None

    def result(self, value: Any) -> DescriptionsComponent:
        return DescriptionsComponent().set_title(self.title).set_items(value)
