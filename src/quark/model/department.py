from sqlalchemy import Column, Integer, String, DateTime, func
from ..db import db

class Department(db.Model):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pid = Column(Integer, default=0)
    name = Column(String(500), nullable=False)
    sort = Column(Integer, default=0)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @staticmethod
    def seeder():
        # 查找或插入“夸克云科技”根部门
        root = db.session.query(Department).filter_by(name="夸克云科技", pid=0).first()
        if not root:
            root = Department(name="夸克云科技", pid=0, sort=0, status=1)
            db.session.add(root)
            db.session.commit()
            db.session.refresh(root)

        seeders = [
            Department(name="研发中心", pid=root.id, sort=0, status=1),
            Department(name="营销中心", pid=root.id, sort=0, status=1),
        ]
        for dept in seeders:
            exists = db.session.query(Department).filter_by(name=dept.name, pid=dept.pid).first()
            if not exists:
                db.session.add(dept)

        db.session.commit()
