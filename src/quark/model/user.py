from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from datetime import datetime
from ..db import db
from ..utils.bcrypt import encrypt_password

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('username', name='username_unique'),
        UniqueConstraint('email', name='email_unique'),
        UniqueConstraint('phone', name='phone_unique'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    nickname = Column(String(200), nullable=False)
    sex = Column(Integer, default=1, nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(11), nullable=False)
    password = Column(String(255), nullable=False)
    avatar = Column(String(1000), nullable=True)
    department_id = Column(Integer, nullable=True)
    position_ids = Column(String(1000), nullable=True)
    last_login_ip = Column(String(255), nullable=True)
    last_login_time = Column(DateTime, default=datetime.utcnow)
    wx_openid = Column(String(255), nullable=True)
    wx_unionid = Column(String(255), nullable=True)
    status = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def seeder(cls):
        user = cls(
            username='administrator',
            nickname='超级管理员',
            email='admin@yourweb.com',
            phone='10086',
            password=encrypt_password('123456'),
            sex=1,
            department_id=1,
            status=1,
            last_login_time=datetime.utcnow()
        )

        existing = db.session.query(User).filter_by(username='administrator').first()
        if existing:
            return
        
        db.session.add(user)
        db.session.commit()