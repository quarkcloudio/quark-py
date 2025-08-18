from ..models.action_log import ActionLog


class ActionLogService:
    def __init__(self):
        pass

    async def insert_get_id(self, data):
        action_log = await ActionLog.create(
            uid=data.uid, url=data.url, ip=data.ip, type=data.type, remark=data.remark
        )
        return action_log.id

    async def count(self):
        return await ActionLog.all().count()
