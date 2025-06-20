from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist
from tortoise.transactions import in_transaction


class StatusAction:
    def __init__(self):
        self.reload = "table"
        self.checked_children = "正常"
        self.unchecked_children = "禁用"
        self.field_name = "status"
        self.field_value = "1"
        self.only_on_index_table_row = True

    def get_api_params(self):
        return ["id"]

    async def handle(self, request: Request, model_cls):
        # 获取参数
        status = request.query_params.get("status")
        if status is None:
            return JSONResponse(status_code=400, content={"error": "参数错误"})

        id_ = request.query_params.get("id")
        if id_ is None:
            return JSONResponse(status_code=400, content={"error": "缺少id参数"})

        # 解析状态
        if status in ("0", "false"):
            field_status = 0
        else:
            field_status = 1

        try:
            async with in_transaction() as conn:
                obj = await model_cls.filter(id=int(id_)).using_db(conn).first()
                if not obj:
                    return JSONResponse(
                        status_code=404, content={"error": "记录不存在"}
                    )

                obj.status = field_status
                await obj.save(using_db=conn)
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

        return JSONResponse(content={"message": "操作成功"})
