from typing import List, Dict, Any
from quark import Request
from quark.template.action import ModalForm
from quark.component.form import field
from quark.component.message.message import Message


class ModalForm(ModalForm):
    def __init__(self):
        self.name = "Test"
        self.type = "link"
        self.destroy_on_close = True
        self.api_params = ["id"]
        self.set_only_on_index_table_row(True)

    def fields(self, request: Request) -> List[Dict[str, Any]]:
        return [
            field.id("id", "ID"),
            field.text("username", "用户名"),
        ]

    def data(self, request: Request) -> Dict[str, Any]:
        id_value = request.query_params.get("id", "")
        return {"id": id_value}

    def handle(self, request: Request, query) -> Dict[str, Any]:
        return Message.error("method not implemented")
