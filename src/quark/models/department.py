from tortoise import fields, models
from tortoise.transactions import in_transaction


class Department(models.Model):
    id = fields.IntField(pk=True)
    pid = fields.IntField(default=0)
    name = fields.CharField(max_length=500)
    sort = fields.IntField(default=0)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "departments"

    @staticmethod
    async def seeder():
        async with in_transaction() as connection:
            root = (
                await Department.filter(name="夸克云科技", pid=0)
                .using_db(connection)
                .first()
            )
            if not root:
                root = await Department.create(
                    name="夸克云科技", pid=0, sort=0, status=1
                )

            # 检查子部门是否存在，不存在则创建
            centers = ["研发中心", "营销中心"]
            for name in centers:
                exists = (
                    await Department.filter(name=name, pid=root.id)
                    .using_db(connection)
                    .exists()
                )
                if not exists:
                    await Department.create(name=name, pid=root.id, sort=0, status=1)
