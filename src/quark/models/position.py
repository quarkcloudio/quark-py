from tortoise import fields
from tortoise.models import Model


class Position(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=500)
    sort = fields.IntField(default=0)
    status = fields.IntField(default=1)
    remark = fields.CharField(max_length=100, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "positions"

    @staticmethod
    async def seeder():
        """
        插入默认职位数据（如果不存在）
        """
        seeders = [
            {"name": "董事长", "sort": 0, "status": 1},
            {"name": "项目经理", "sort": 0, "status": 1},
            {"name": "普通员工", "sort": 0, "status": 1},
        ]

        for data in seeders:
            exists = await Position.filter(name=data["name"]).first()
            if not exists:
                await Position.create(**data)

    @staticmethod
    async def list():
        """
        获取所有启用状态的职位，返回类似 checkbox.Option 格式的数据
        """
        try:
            positions = await Position.filter(status=1).all()
            return [{"label": p.name, "value": p.id} for p in positions]
        except Exception:
            return []
