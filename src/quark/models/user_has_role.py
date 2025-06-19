from tortoise import fields
from tortoise.models import Model


class UserHasRole(Model):
    id = fields.BigIntField(pk=True)
    uid = fields.BigIntField()
    role_id = fields.BigIntField()
    guard_name = fields.CharField(max_length=200, default="admin")
    created_at = fields.DatetimeField(null=True)  # 你原来没设置默认，现在设为可空
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "user_has_roles"
