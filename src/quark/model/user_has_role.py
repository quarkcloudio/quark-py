from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func
from ..dal import db

class UserHasRole(db.Model):
    __tablename__ = 'user_has_roles'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uid = Column(BigInteger, nullable=False)
    role_id = Column(BigInteger, nullable=False)
    guard_name = Column(String(200), default='admin')
    created_at = Column(DateTime)
    updated_at = Column(DateTime, onupdate=func.now())
