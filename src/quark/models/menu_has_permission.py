from tortoise import models, fields


class MenuHasPermission(models.Model):
    id = fields.BigIntField(pk=True)
    menu_id = fields.BigIntField()
    permission_id = fields.BigIntField()
    guard_name = fields.CharField(max_length=200, default="admin")
    created_at = fields.DatetimeField(auto_now_add=True, null=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "menu_has_permissions"
