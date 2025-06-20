from fastapi import Request
from fastapi.responses import JSONResponse


class SelectOptionsAction:
    def __init__(self):
        # 可以根据需要初始化属性
        pass

    async def handle(self, request: Request, db_session) -> JSONResponse:
        # 这里 db_session 对应 gorm.DB
        # 你可以在这里执行数据库操作
        # 目前仅返回成功消息

        return JSONResponse(content={"message": "操作成功"})
