from typing import List, Dict, Any
from pydantic import BaseModel, Field


# 模拟 rule.Required 验证器
def required(value: str):
    if not value or value.strip() == "":
        raise ValueError("名称必须填写")
    return value


# 模拟资源字段类
class Field:
    def Text(self, name: str, label: str):
        # 返回字段描述，简化实现
        return {"type": "text", "name": name, "label": label, "rules": []}

    def SetRules(self, rules: List):
        # 假设rules是验证函数列表
        # 这里直接存储规则说明，供前端或验证用
        self.rules = rules
        return self


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


# 使用示例（假设 ctx 是请求上下文字典）
ctx_example = {"query_params": {"id": "123"}}

modal_form_action = ModalFormAction()
print("Init:", modal_form_action.init(ctx_example))
print("Fields:", modal_form_action.fields(ctx_example))
print("Data:", modal_form_action.data(ctx_example))
print("Handle:", modal_form_action.handle(ctx_example, None))
