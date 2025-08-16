from tortoise.queryset import QuerySet

from quark import Message, Request
from quark.template.action import Action


class SelectOptions(Action):
    def __init__(self):
        pass

    async def handle(self, request: Request, query: QuerySet):
        return Message.success("操作成功")
