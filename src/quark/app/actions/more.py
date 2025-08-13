from typing import Any, List

from quark.template.action import Dropdown


class More(Dropdown):
    def __init__(self, name: str = "更多"):
        self.name = name
        self.arrow = True
        self.placement = "bottomLeft"
        self.trigger = ["hover"]
        self.overlay_style = {"zIndex": 999}
        self.type = "link"
        self.size = "small"
        self.set_only_on_index_table_row(True)

    def set_actions(self, actions: List[Any]) -> Any:
        self.actions = actions
        return self
