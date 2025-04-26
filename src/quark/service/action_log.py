from ..db import db
from ..model.action_log import ActionLog

# ActionLogService类
class ActionLogService:
    def __init__(self):
        pass

    def insert_get_id(self, data):
        action_log = ActionLog(
            user_id=data.user_id,
            action=data.action,
            ip=data.ip
        )
        db.session.add(action_log)
        db.session.commit()
        return action_log.id