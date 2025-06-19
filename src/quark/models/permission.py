from tortoise import fields
from tortoise.models import Model


class Permission(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=500)
    guard_name = fields.CharField(max_length=100)
    path = fields.CharField(max_length=500)
    method = fields.CharField(max_length=500)
    remark = fields.CharField(max_length=100, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "permissions"
