from tortoise import fields
from tortoise.models import Model
from tortoise.transactions import in_transaction


class Menu(Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    guard_name = fields.CharField(max_length=100)
    permission = fields.CharField(max_length=100)
    icon = fields.CharField(max_length=100, null=True)
    type = fields.IntField()
    page_type = fields.IntField()
    pid = fields.IntField(default=0)
    sort = fields.IntField(default=0)
    path = fields.CharField(max_length=255, null=True)
    query = fields.CharField(max_length=255, null=True)
    component = fields.CharField(max_length=255, null=True)
    visible = fields.IntField(default=1)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta(Model.Meta):
        table = "menus"

    def __str__(self):
        return f"<Menu {self.name}>"

    @staticmethod
    async def seeder():
        menus = [
            {"id": 1, "name": "首页", "guard_name": "admin", "icon": "ant-design:home-outlined", 
             "type": 2, "pid": 0, "sort": 0, "path": "home", 
             "query": "{\"api\":\"/api/admin/dashboard/index/index\"}", "component": "home/index", 
             "visible": 1, "page_type": 1, "status": 1, "permission": ""},
            {"id": 3, "name": "用户管理", "guard_name": "admin", "icon": "ant-design:usergroup-add-outlined", 
             "type": 1, "pid": 0, "sort": 100, "path": "user", "query": "", "component": "", 
             "visible": 1, "page_type": 1, "status": 1, "permission": ""},
            {"id": 4, "name": "用户列表", "guard_name": "admin", "icon": "ant-design:user-add-outlined", 
             "type": 2, "pid": 3, "sort": 0, "path": "user", 
             "query": "{\"api\":\"/api/admin/user/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 5, "name": "权限列表", "guard_name": "admin", "icon": "ant-design:profile-outlined", 
             "type": 2, "pid": 3, "sort": 0, "path": "permission", 
             "query": "{\"api\":\"/api/admin/permission/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 6, "name": "角色列表", "guard_name": "admin", "icon": "ant-design:idcard-outlined", 
             "type": 2, "pid": 3, "sort": 0, "path": "role", 
             "query": "{\"api\":\"/api/admin/role/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 7, "name": "系统配置", "guard_name": "admin", "icon": "ant-design:setting-outlined", 
             "type": 1, "pid": 0, "sort": 100, "path": "system", "query": "", "component": "", 
             "visible": 1, "page_type": 1, "status": 1, "permission": ""},
            {"id": 8, "name": "设置管理", "guard_name": "admin", "icon": "ant-design:appstore-add-outlined", 
             "type": 1, "pid": 7, "sort": 0, "path": "config", "query": "", "component": "", 
             "visible": 1, "page_type": 1, "status": 1, "permission": ""},
            {"id": 9, "name": "网站设置", "guard_name": "admin", "icon": "ant-design:cluster-outlined", 
             "type": 2, "pid": 8, "sort": 0, "path": "webConfig", 
             "query": "{\"api\":\"/api/admin/webConfig/form\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 10, "name": "配置管理", "guard_name": "admin", "icon": "ant-design:tool-outlined", 
             "type": 2, "pid": 8, "sort": 0, "path": "config", 
             "query": "{\"api\":\"/api/admin/config/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 11, "name": "菜单管理", "guard_name": "admin", "icon": "ant-design:menu-outlined", 
             "type": 2, "pid": 7, "sort": 0, "path": "menu", 
             "query": "{\"api\":\"/api/admin/menu/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 12, "name": "操作日志", "guard_name": "admin", "icon": "ant-design:file-done-outlined", 
             "type": 2, "pid": 7, "sort": 100, "path": "actionLog", 
             "query": "{\"api\":\"/api/admin/actionLog/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 13, "name": "附件空间", "guard_name": "admin", "icon": "ant-design:folder-outlined", 
             "type": 1, "pid": 0, "sort": 100, "path": "attachment", "query": "", "component": "", 
             "visible": 1, "page_type": 1, "status": 1, "permission": ""},
            {"id": 14, "name": "文件管理", "guard_name": "admin", "icon": "ant-design:file-outlined", 
             "type": 2, "pid": 13, "sort": 0, "path": "file", 
             "query": "{\"api\":\"/api/admin/file/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 15, "name": "图片管理", "guard_name": "admin", "icon": "ant-design:picture-outlined", 
             "type": 2, "pid": 13, "sort": 0, "path": "image", 
             "query": "{\"api\":\"/api/admin/image/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 16, "name": "我的账号", "guard_name": "admin", "icon": "ant-design:user-outlined", 
             "type": 1, "pid": 0, "sort": 110, "path": "account", "query": "", "component": "", 
             "visible": 1, "page_type": 1, "status": 1, "permission": ""},
            {"id": 17, "name": "个人设置", "guard_name": "admin", "icon": "ant-design:user-switch-outlined", 
             "type": 2, "pid": 16, "sort": 0, "path": "setting", 
             "query": "{\"api\":\"/api/admin/account/form\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 18, "name": "部门列表", "guard_name": "admin", "icon": "ant-design:apartment-outlined", 
             "type": 2, "pid": 3, "sort": 0, "path": "department", 
             "query": "{\"api\":\"/api/admin/department/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 19, "name": "职位列表", "guard_name": "admin", "icon": "ant-design:bars-outlined", 
             "type": 2, "pid": 3, "sort": 0, "path": "position", 
             "query": "{\"api\":\"/api/admin/position/index\"}", "component": "", 
             "visible": 1, "page_type": 2, "status": 1, "permission": ""},
            {"id": 20, "name": "组件调试", "guard_name": "admin", "icon": "ant-design:appstore-outlined", 
             "type": 1, "pid": 0, "sort": 100, "path": "develop", "query": "", "component": "", 
             "visible": 0, "page_type": 1, "status": 1, "permission": ""},
            {"id": 21, "name": "组件开发", "guard_name": "admin", "icon": "ant-design:experiment-outlined", 
             "type": 2, "pid": 20, "sort": 0, "path": "index", "query": "", "component": "develop/index", 
             "visible": 1, "page_type": 1, "status": 1, "permission": ""},
        ]

        # 在事务中逐条检查并插入
        async with in_transaction():
            for data in menus:
                if not await Menu.filter(id=data["id"]).exists():
                    await Menu.create(**data)
