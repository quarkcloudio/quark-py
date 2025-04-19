import hashlib
import uuid
import json
from typing import Optional, Dict, Any
from dataclasses import dataclass, field, asdict

@dataclass
class Element:
    componentKey: str = ""
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

        self.componentKey = key
        return self

    def snake_to_camel(self, snake_str):
        parts = snake_str.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])

    def dict_keys_to_camel(self, d):
        return {self.snake_to_camel(k): v for k, v in d.items()}

    def to_json(self):
        return json.dumps(self.dict_keys_to_camel(asdict(self)))