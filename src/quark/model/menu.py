from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from ..db import db


class Menu(db.Model):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    guard_name = Column(String(100), nullable=False)
    icon = Column(String(100), nullable=True)
    type = Column(Integer, nullable=False)
    pid = Column(Integer, default=0)
    sort = Column(Integer, default=0)
    path = Column(String(255), nullable=True)
    show = Column(Integer, default=1, nullable=False)
    is_engine = Column(Integer, default=0, nullable=False)
    is_link = Column(Integer, default=0, nullable=False)
    status = Column(Integer, default=1, nullable=False)
    # key = Column(String(255))         # <-:false 无需映射设置
    # locale = Column(String(255))      # <-:false
    # hide_in_menu = Column(Boolean)    # <-:false
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Menu {self.name}>"

    @staticmethod
    def seeder():
        seeders = [
            Menu(id=1, name="控制台", guard_name="admin", icon="icon-home", type=1, pid=0, sort=0, path="/dashboard", show=1, is_engine=0, is_link=0, status=1),
            Menu(id=2, name="主页", guard_name="admin", icon="", type=2, pid=1, sort=0, path="/api/admin/dashboard/index/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=3, name="用户管理", guard_name="admin", icon="icon-admin", type=1, pid=0, sort=100, path="/user", show=1, is_engine=0, is_link=0, status=1),
            Menu(id=4, name="用户列表", guard_name="admin", icon="", type=2, pid=3, sort=0, path="/api/admin/user/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=5, name="权限列表", guard_name="admin", icon="", type=2, pid=3, sort=0, path="/api/admin/permission/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=6, name="角色列表", guard_name="admin", icon="", type=2, pid=3, sort=0, path="/api/admin/role/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=7, name="系统配置", guard_name="admin", icon="icon-setting", type=1, pid=0, sort=100, path="/system", show=1, is_engine=0, is_link=0, status=1),
            Menu(id=8, name="设置管理", guard_name="admin", icon="", type=1, pid=7, sort=0, path="/system/config", show=1, is_engine=0, is_link=0, status=1),
            Menu(id=9, name="网站设置", guard_name="admin", icon="", type=2, pid=8, sort=0, path="/api/admin/webConfig/form", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=10, name="配置管理", guard_name="admin", icon="", type=2, pid=8, sort=0, path="/api/admin/config/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=11, name="菜单管理", guard_name="admin", icon="", type=2, pid=7, sort=0, path="/api/admin/menu/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=12, name="操作日志", guard_name="admin", icon="", type=2, pid=7, sort=100, path="/api/admin/actionLog/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=13, name="附件空间", guard_name="admin", icon="icon-attachment", type=1, pid=0, sort=100, path="/attachment", show=1, is_engine=0, is_link=0, status=1),
            Menu(id=14, name="文件管理", guard_name="admin", icon="", type=2, pid=13, sort=0, path="/api/admin/file/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=15, name="图片管理", guard_name="admin", icon="", type=2, pid=13, sort=0, path="/api/admin/image/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=16, name="我的账号", guard_name="admin", icon="icon-user", type=1, pid=0, sort=100, path="/account", show=1, is_engine=0, is_link=0, status=1),
            Menu(id=17, name="个人设置", guard_name="admin", icon="", type=2, pid=16, sort=0, path="/api/admin/account/form", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=18, name="部门列表", guard_name="admin", icon="", type=2, pid=3, sort=0, path="/api/admin/department/index", show=1, is_engine=1, is_link=0, status=1),
            Menu(id=19, name="职位列表", guard_name="admin", icon="", type=2, pid=3, sort=0, path="/api/admin/position/index", show=1, is_engine=1, is_link=0, status=1),
        ]
        for menu in seeders:
            exists = db.session.query(Menu).filter_by(id=menu.id).first()
            if not exists:
                db.session.add(menu)
        db.session.commit()
