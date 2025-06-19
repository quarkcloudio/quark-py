from tortoise import fields
from tortoise.models import Model


class Role(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    data_scope = fields.IntField(default=1)  # 1：全部权限 ...
    guard_name = fields.CharField(max_length=100)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "roles"

    @classmethod
    async def seeder(cls):
        """
        初始化角色数据：普通角色
        """
        if not await cls.filter(name="普通角色").exists():
            await cls.create(name="普通角色", guard_name="admin", data_scope=1)
