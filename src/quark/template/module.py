from ..db import db
from ..model.user import User
from ..model.role import Role
from ..model.menu import Menu
from ..model.position import Position
from ..model.department import Department
from ..model.permission import Permission
from ..model.user_has_role import UserHasRole
from ..model.role_has_permission import RoleHasPermission
from ..model.role_has_menu import RoleHasMenu
from ..model.role_has_department import RoleHasDepartment
from ..model.menu_has_permission import MenuHasPermission
from ..model.config import Config
from ..model.attachment import Attachment
from ..model.attachment_category import AttachmentCategory
from ..model.action_log import ActionLog

# 执行安装操作
def install():
    
    # 创建数据库表
    db.create_all()

    # 初始化数据
    User.seeder()
    Role.seeder()
    Position.seeder()
    Menu.seeder()
    Department.seeder()
    Config.seeder()