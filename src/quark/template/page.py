from dataclasses import dataclass, field
from typing import Optional, Any, List
import i18n

@dataclass
class Page:

    # 页面标题
    title: str = ""