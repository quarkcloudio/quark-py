from ..models.action_log import ActionLog


class ActionLogService:
    def __init__(self):
        pass

    async def insert_get_id(self, data):
        action_log = await ActionLog.create(
            user_id=data.user_id, action=data.action, ip=data.ip
        )
        return action_log.id

    async def count(self):
        return await ActionLog.all().count()
