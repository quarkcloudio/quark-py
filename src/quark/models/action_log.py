from tortoise import fields, models


class ActionLog(models.Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField()
    username = fields.CharField(max_length=20, null=True)
    url = fields.CharField(max_length=500)
    remark = fields.CharField(max_length=255)
    ip = fields.CharField(max_length=100)
    type = fields.CharField(max_length=100)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "action_logs"
