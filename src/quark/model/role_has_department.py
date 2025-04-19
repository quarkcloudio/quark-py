from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func
from ..dal import db

class RoleHasDepartment(db.Model):
    __tablename__ = 'role_has_departments'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    role_id = Column(BigInteger, nullable=False)
    department_id = Column(BigInteger, nullable=False)
    guard_name = Column(String(200), default='admin')
    created_at = Column(DateTime)
    updated_at = Column(DateTime, onupdate=func.now())
