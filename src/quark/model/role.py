from sqlalchemy import Column, Integer, String, DateTime, func
from ..db import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    data_scope = Column(Integer, nullable=False, default=1)  # 1：全部权限 ...
    guard_name = Column(String(100), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @staticmethod
    def seeder():
        seeders = [
            Role(name='普通角色', guard_name='admin', data_scope=1),
        ]
        for role in seeders:
            exists = db.session.query(Role).filter_by(name=role.name).first()
            if not exists:
                db.session.add(role)
        db.session.commit()