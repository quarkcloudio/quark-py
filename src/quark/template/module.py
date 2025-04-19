from ..model.user import User
from ..model.role import Role
from ..model.position import Position
from ..dal import db

# 执行安装操作
def install():
    # 创建数据库表
    db.Model.metadata.create_all(db.engine)

    # 初始化数据
    User.seeder()
    Role.seeder()
    Position.seeder()