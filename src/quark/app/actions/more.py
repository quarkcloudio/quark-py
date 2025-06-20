from typing import List, Any, Optional


class Dropdown:
    def __init__(self):
        self.Arrow = True
        self.Placement = "bottomLeft"
        self.Trigger = ["hover"]
        self.OverlayStyle = {"zIndex": 999}
        self.Type = "link"
        self.Size = "small"
        self.ShowOnlyOnIndexTableRow = True
        self.Name = "更多"
        self.Actions = []

    def set_only_on_index_table_row(self, val: bool):
        self.ShowOnlyOnIndexTableRow = val
        return self


class MoreAction(Dropdown):
    def __init__(self, *options: Any):
        super().__init__()
        if len(options) == 1:
            self.Name = options[0]
        elif len(options) == 2:
            self.Name = options[0]
            self.Actions = options[1]

    def init(self, ctx: dict) -> dict:
        # 初始化配置
        self.Arrow = True
        self.Placement = "bottomLeft"
        self.Trigger = ["hover"]
        self.OverlayStyle = {"zIndex": 999}
        self.Type = "link"
        self.Size = "small"
        self.set_only_on_index_table_row(True)

        return {
            "Arrow": self.Arrow,
            "Placement": self.Placement,
            "Trigger": self.Trigger,
            "OverlayStyle": self.OverlayStyle,
            "Type": self.Type,
            "Size": self.Size,
            "ShowOnlyOnIndexTableRow": self.ShowOnlyOnIndexTableRow,
            "Name": self.Name,
            "Actions": self.Actions,
        }

    def set_actions(self, actions: List[Any]) -> "MoreAction":
        self.Actions = actions
        return self


# 示例用法
more = MoreAction("更多", [{"Name": "操作1"}, {"Name": "操作2"}])
print(more.init({}))
