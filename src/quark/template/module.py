from ..model import user, role
from ..dal import db

# 执行安装操作
def install():
    # 创建数据库表
    db.Model.metadata.create_all(db.engine)

    # 初始化数据
    user.User.seeder()
    role.Role.seeder()