from dataclasses import dataclass
from typing import List, Any
from quark.template.dashboard import Dashboard

@dataclass
class Index(Dashboard):
    title: str = "仪表盘"

    def cards(self) -> List[Any]:
        return []