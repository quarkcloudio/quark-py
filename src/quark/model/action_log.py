from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..dal import db

class ActionLog(db.Model):
    __tablename__ = 'action_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, nullable=False)
    username = Column(String(20))
    url = Column(String(500), nullable=False)
    remark = Column(String(255), nullable=False)
    ip = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
