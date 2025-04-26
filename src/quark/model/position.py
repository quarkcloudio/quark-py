from sqlalchemy import Column, Integer, String, DateTime, func
from ..db import db

class Position(db.Model):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False)
    sort = Column(Integer, default=0)
    status = Column(Integer, nullable=False, default=1)
    remark = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @staticmethod
    def seeder():
        seeders = [
            Position(name="董事长", sort=0, status=1),
            Position(name="项目经理", sort=0, status=1),
            Position(name="普通员工", sort=0, status=1),
        ]
        for pos in seeders:
            exists = db.session.query(Position).filter_by(name=pos.name).first()
            if not exists:
                db.session.add(pos)
        db.session.commit()

    @staticmethod
    def list():
        """
        获取所有启用状态的职位，返回类似 checkbox.Option 格式的数据
        """
        session = db.Session()
        try:
            positions = session.query(Position).filter_by(status=1).all()
            return [{"label": p.name, "value": p.id} for p in positions]
        except Exception as e:
            return []
        finally:
            session.close()