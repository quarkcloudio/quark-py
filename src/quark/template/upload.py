from dataclasses import dataclass, field
from typing import Optional, Any, List
import i18n

@dataclass
class Upload:

    # 页面标题
    title: str = ""