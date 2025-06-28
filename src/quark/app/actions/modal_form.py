from typing import List, Dict, Any
from pydantic import BaseModel, Field


class ModalFormAction:
    def __init__(self):
        self.Name = "Test"
        self.Type = "link"
        self.DestroyOnClose = True
        self.api_params = ["id"]
        self.show_only_on_index_table_row = True

    def init(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        # 返回初始化配置
        return {
            "Name": self.Name,
            "Type": self.Type,
            "DestroyOnClose": self.DestroyOnClose,
            "ApiParams": self.api_params,
            "ShowOnlyOnIndexTableRow": self.show_only_on_index_table_row,
        }

    def fields(self, ctx: Dict[str, Any]) -> List[Dict[str, Any]]:
        field = Field()
        return [
            field.Text("id", "ID"),
            {**field.Text("name", "名称"), "rules": ["required: 名称必须填写"]},
        ]

    def data(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        # 这里假设ctx有查询参数
        id_value = ctx.get("query_params", {}).get("id", "")
        return {"id": id_value}

    def handle(self, ctx: Dict[str, Any], query) -> Dict[str, Any]:
        # 这里返回未实现错误
        return {"error": "method not implemented"}
