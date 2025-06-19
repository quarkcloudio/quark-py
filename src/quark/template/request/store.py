import json
from fastapi import Request


class StoreRequest:
    """
    保存请求处理类
    """

    def handle(self, request: Request, data: dict):

        return "存储成功"
