from dataclasses import dataclass, field
from typing import Optional, Any, List
import i18n

@dataclass
class Login:

    # 页面标题
    title: str = ""

    def index_render(self):
        return "xyz"