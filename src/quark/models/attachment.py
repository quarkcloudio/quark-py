from tortoise import fields, models


class Attachment(models.Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField(default=0)
    source = fields.CharField(max_length=255, null=True)
    category_id = fields.IntField(default=0)
    name = fields.CharField(max_length=255)
    type = fields.CharField(max_length=255, null=True)
    sort = fields.IntField(default=0)
    size = fields.BigIntField(default=0)
    ext = fields.CharField(max_length=255, null=True)
    path = fields.CharField(max_length=255)
    url = fields.CharField(max_length=255)
    hash = fields.CharField(max_length=255)
    extra = fields.CharField(max_length=5000, default="", null=False)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "attachments"
