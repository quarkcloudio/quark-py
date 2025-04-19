from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func
from ..dal import db

class MenuHasPermission(db.Model):
    __tablename__ = 'menu_has_permissions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    menu_id = Column(BigInteger, nullable=False)
    permission_id = Column(BigInteger, nullable=False)
    guard_name = Column(String(200), default='admin')
    created_at = Column(DateTime)
    updated_at = Column(DateTime, onupdate=func.now())
