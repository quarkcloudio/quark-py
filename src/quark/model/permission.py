from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..dal import db

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False)
    guard_name = Column(String(100), nullable=False)
    path = Column(String(500), nullable=False)
    method = Column(String(500), nullable=False)
    remark = Column(String(100), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())