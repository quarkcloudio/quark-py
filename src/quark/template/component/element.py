import hashlib
import uuid
from typing import Optional, Dict, Any

class Element:
    def __init__(self):
        self.ComponentKey: str = ""
        self.Component: str = ""
        self.Style: Dict[str, Any] = {}

    def set_component(self, component: str) -> 'Element':
        self.Component = component
        self.set_key(component, crypt=True)
        return self

    def set_key(self, key: Optional[str], crypt: bool = True) -> 'Element':
        if not key:
            key = str(uuid.uuid4())
        if crypt:
            md5_hash = hashlib.md5()
            md5_hash.update(key.encode('utf-8'))
            key = md5_hash.hexdigest()

        self.ComponentKey = key
        return self
