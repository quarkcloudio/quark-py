from .models.user import User
from .models.role import Role
from .models.menu import Menu
from .models.position import Position
from .models.department import Department
from .models.config import Config


# 执行安装操作
async def setup_all():

    # 初始化数据
    await User.seeder()
    await Role.seeder()
    await Position.seeder()
    await Menu.seeder()
    await Department.seeder()
    await Config.seeder()
