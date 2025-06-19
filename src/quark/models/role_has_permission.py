from tortoise import fields
from tortoise.models import Model


class RoleHasPermission(Model):
    id = fields.BigIntField(pk=True)
    role_id = fields.BigIntField()
    permission_id = fields.BigIntField()
    guard_name = fields.CharField(max_length=200, default="admin")
    created_at = fields.DatetimeField(null=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "role_has_permissions"
