from ..models.position import Position
from tortoise.exceptions import DoesNotExist


class PositionService:
    def __init__(self):
        pass

    # 获取列表
    async def get_list(self):
        positions = await Position.all()
        return positions, None

    # 通过ID获取信息
    async def get_info_by_id(self, position_id: int):
        try:
            position = await Position.get(id=position_id, status=1)
            return position, None
        except DoesNotExist:
            return None, ValueError("Position not found")

    # 通过名称获取信息
    async def get_info_by_name(self, name: str):
        try:
            position = await Position.get(name=name, status=1)
            return position, None
        except DoesNotExist:
            return None, ValueError("Position not found")

    # 通过ID判断职位是否已存在
    async def is_exist(self, position_id: int):
        return await Position.exists(id=position_id)

    # 通过名称判断职位是否已存在
    async def is_exist_by_name(self, name: str):
        return await Position.exists(name=name)

    # 插入数据并返回ID
    async def insert_get_id(self, position: Position):
        await position.save()
        return position.id, None

    # 通过ID更新数据
    async def update_by_id(self, position_id: int, data: dict):
        try:
            position = await Position.get(id=position_id)
            for key, value in data.items():
                setattr(position, key, value)
            await position.save()
            return None
        except DoesNotExist:
            return ValueError("Position not found")

    # 通过ID删除记录
    async def delete_by_id(self, position_id: int):
        try:
            position = await Position.get(id=position_id)
            await position.delete()
            return None
        except DoesNotExist:
            return ValueError("Position not found")
