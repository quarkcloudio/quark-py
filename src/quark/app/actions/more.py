from typing import List, Any
from quark.template.action import Dropdown


class More(Dropdown):
    def __init__(self, name: str = "更多"):
        self.name = name
        self.Arrow = True
        self.Placement = "bottomLeft"
        self.Trigger = ["hover"]
        self.OverlayStyle = {"zIndex": 999}
        self.Type = "link"
        self.Size = "small"
        self.set_only_on_index_table_row(True)

    def set_actions(self, actions: List[Any]) -> Any:
        self.Actions = actions
        return self
