from pydantic import BaseModel, ConfigDict, Field
from typing import Any, Dict, Optional
import hashlib
import uuid

def to_camel(string: str) -> str:
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

class Component(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra='allow'
    )

    component: str = None
    component_key: str = None
    style: dict = None

    def set_component(self, component: str) -> 'Component':
        self.component = component
        self.set_key(component, crypt=True)
        return self

    def set_key(self, key: Optional[str] = "", crypt: bool = True) -> 'Component':
        if not key:
            key = str(uuid.uuid4())
        if crypt:
            md5_hash = hashlib.md5()
            md5_hash.update(key.encode('utf-8'))
            key = md5_hash.hexdigest()
        self.component_key = key
        return self

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(by_alias=True, exclude_none=True, **kwargs)

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        return self.model_dump(by_alias=True, **kwargs)
