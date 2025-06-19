from tortoise import fields, models


class AttachmentCategory(models.Model):
    id = fields.IntField(pk=True)
    source = fields.CharField(max_length=100, null=True)
    uid = fields.IntField(default=0)
    title = fields.CharField(max_length=255)
    sort = fields.IntField(default=0)
    description = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "attachment_categories"
