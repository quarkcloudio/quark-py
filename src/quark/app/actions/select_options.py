from quark import Request
from quark.template.action import Action
from quark.component.message.message import Message


class SelectOptions(Action):
    def __init__(self):
        pass

    async def handle(self, request: Request, query) -> any:
        return Message.success("操作成功")
