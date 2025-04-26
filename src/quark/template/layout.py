from dataclasses import dataclass, field
from typing import Optional, Any, List
import i18n

@dataclass
class Layout:

    # 页面标题
    title: str = ""

    def render(self):
        return {
            "title": self.title
        }