from tortoise import fields, models
from datetime import datetime
from ..utils import hash_password


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20)
    nickname = fields.CharField(max_length=200)
    sex = fields.IntField(default=1)
    email = fields.CharField(max_length=50)
    phone = fields.CharField(max_length=11)
    password = fields.CharField(max_length=255)
    avatar = fields.CharField(max_length=1000, null=True)
    department_id = fields.IntField(null=True)
    position_ids = fields.CharField(max_length=1000, null=True)
    last_login_ip = fields.CharField(max_length=255, null=True)
    last_login_time = fields.DatetimeField(null=True, default=datetime.now())
    wx_openid = fields.CharField(max_length=255, null=True)
    wx_unionid = fields.CharField(max_length=255, null=True)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "users"
        unique_together = (
            ("username",),
            ("email",),
            ("phone",),
        )

    @classmethod
    async def seeder(cls):
        # 检查是否已存在超级管理员
        existing = await cls.get_or_none(username="administrator")
        if existing:
            return

        await cls.create(
            username="administrator",
            nickname="超级管理员",
            email="admin@yourweb.com",
            phone="10086",
            password=hash_password("123456"),
            sex=1,
            department_id=1,
            status=1,
            last_login_time=datetime.utcnow(),
        )
