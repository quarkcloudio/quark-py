from pydantic import BaseModel, ConfigDict
from typing import Any, Dict
import hashlib
import uuid


def to_camel(string: str) -> str:
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


class Element(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra='allow'
    )

    def set(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(by_alias=True, **kwargs)

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        return self.model_dump(by_alias=True, **kwargs)
