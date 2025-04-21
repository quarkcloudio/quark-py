import hashlib
import uuid
import json
from typing import Optional, Dict, Any, Union
from dataclasses import dataclass, field, asdict, is_dataclass

@dataclass
class Element:
    component_key: str = ""
    component: str = ""
    style: Dict[str, Any] = field(default_factory=dict)

    def set_component(self, component: str) -> 'Element':
        self.component = component
        self.set_key(component, crypt=True)
        return self

    def set_key(self, key: Optional[str], crypt: bool = True) -> 'Element':
        if not key:
            key = str(uuid.uuid4())
        if crypt:
            md5_hash = hashlib.md5()
            md5_hash.update(key.encode('utf-8'))
            key = md5_hash.hexdigest()
        self.component_key = key
        return self

    def snake_to_camel(self, snake_str: str) -> str:
        parts = snake_str.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])

    def convert_keys_to_camel(self, obj: Any) -> Any:
        if isinstance(obj, dict):
            return {
                self.snake_to_camel(k): self.convert_keys_to_camel(v)
                for k, v in obj.items()
            }
        elif isinstance(obj, list):
            return [self.convert_keys_to_camel(item) for item in obj]
        elif is_dataclass(obj):
            return self.convert_keys_to_camel(asdict(obj))
        else:
            return obj

    def to_json(self) -> str:
        return json.dumps(self.convert_keys_to_camel(asdict(self)))
