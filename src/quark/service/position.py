from ..db import db
from ..model.position import Position

# PositionService类
class PositionService:
    def __init__(self):
        pass

    # 获取列表
    def get_list(self):
        positions = Position.query.all()
        return positions, None

    # 通过ID获取信息
    def get_info_by_id(self, position_id):
        position = Position.query.filter_by(id=position_id, status=1).first()
        return position, None if position else ValueError("Position not found")

    # 通过名称获取信息
    def get_info_by_name(self, name):
        position = Position.query.filter_by(name=name, status=1).first()
        return position, None if position else ValueError("Position not found")

    # 通过ID判断职位是否已存在
    def is_exist(self, position_id):
        position = Position.query.filter_by(id=position_id).first()
        if position:
            return True
        return False

    # 通过名称判断职位是否已存在
    def is_exist_by_name(self, name):
        position = Position.query.filter_by(name=name).first()
        if position:
            return True
        return False

    # 插入数据并返回ID
    def insert_get_id(self, position):
        db.session.add(position)
        db.session.commit()
        return position.id, None

    # 通过ID更新数据
    def update_by_id(self, position_id, data):
        position = Position.query.filter_by(id=position_id).first()
        if not position:
            return ValueError("Position not found")
        for key, value in data.items():
            setattr(position, key, value)
        db.session.commit()
        return None

    # 通过ID删除记录
    def delete_by_id(self, position_id):
        position = Position.query.filter_by(id=position_id).first()
        if not position:
            return ValueError("Position not found")
        db.session.delete(position)
        db.session.commit()
        return None