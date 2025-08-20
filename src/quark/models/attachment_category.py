from tortoise import fields
from tortoise.models import Model


class AttachmentCategory(Model):
    id = fields.IntField(pk=True)
    source = fields.CharField(max_length=100, null=True)
    uid = fields.IntField(default=0)
    title = fields.CharField(max_length=255)
    sort = fields.IntField(default=0)
    description = fields.CharField(max_length=255, null=True)

    class Meta(Model.Meta):
        table = "attachment_categories"
