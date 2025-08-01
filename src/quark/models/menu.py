from tortoise import fields, models
from tortoise.transactions import in_transaction


class Menu(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    guard_name = fields.CharField(max_length=100)
    icon = fields.CharField(max_length=100, null=True)
    type = fields.IntField()
    pid = fields.IntField(default=0)
    sort = fields.IntField(default=0)
    path = fields.CharField(max_length=255, null=True)
    show = fields.IntField(default=1)
    is_engine = fields.IntField(default=0)
    is_link = fields.IntField(default=0)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "menus"

    def __str__(self):
        return f"<Menu {self.name}>"

    @staticmethod
    async def seeder():
        menus = [
            {
                "id": 1,
                "name": "控制台",
                "guard_name": "admin",
                "icon": "icon-home",
                "type": 1,
                "pid": 0,
                "sort": 0,
                "path": "/dashboard",
                "show": 1,
                "is_engine": 0,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 2,
                "name": "主页",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 1,
                "sort": 0,
                "path": "/api/admin/dashboard/index/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 3,
                "name": "用户管理",
                "guard_name": "admin",
                "icon": "icon-admin",
                "type": 1,
                "pid": 0,
                "sort": 100,
                "path": "/user",
                "show": 1,
                "is_engine": 0,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 4,
                "name": "用户列表",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 3,
                "sort": 0,
                "path": "/api/admin/user/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 5,
                "name": "权限列表",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 3,
                "sort": 0,
                "path": "/api/admin/permission/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 6,
                "name": "角色列表",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 3,
                "sort": 0,
                "path": "/api/admin/role/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 7,
                "name": "系统配置",
                "guard_name": "admin",
                "icon": "icon-setting",
                "type": 1,
                "pid": 0,
                "sort": 100,
                "path": "/system",
                "show": 1,
                "is_engine": 0,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 8,
                "name": "设置管理",
                "guard_name": "admin",
                "icon": "",
                "type": 1,
                "pid": 7,
                "sort": 0,
                "path": "/system/config",
                "show": 1,
                "is_engine": 0,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 9,
                "name": "网站设置",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 8,
                "sort": 0,
                "path": "/api/admin/webConfig/form",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 10,
                "name": "配置管理",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 8,
                "sort": 0,
                "path": "/api/admin/config/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 11,
                "name": "菜单管理",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 7,
                "sort": 0,
                "path": "/api/admin/menu/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 12,
                "name": "操作日志",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 7,
                "sort": 100,
                "path": "/api/admin/actionLog/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 13,
                "name": "附件空间",
                "guard_name": "admin",
                "icon": "icon-attachment",
                "type": 1,
                "pid": 0,
                "sort": 100,
                "path": "/attachment",
                "show": 1,
                "is_engine": 0,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 14,
                "name": "文件管理",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 13,
                "sort": 0,
                "path": "/api/admin/file/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 15,
                "name": "图片管理",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 13,
                "sort": 0,
                "path": "/api/admin/image/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 16,
                "name": "我的账号",
                "guard_name": "admin",
                "icon": "icon-user",
                "type": 1,
                "pid": 0,
                "sort": 100,
                "path": "/account",
                "show": 1,
                "is_engine": 0,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 17,
                "name": "个人设置",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 16,
                "sort": 0,
                "path": "/api/admin/account/form",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 18,
                "name": "部门列表",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 3,
                "sort": 0,
                "path": "/api/admin/department/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
            {
                "id": 19,
                "name": "职位列表",
                "guard_name": "admin",
                "icon": "",
                "type": 2,
                "pid": 3,
                "sort": 0,
                "path": "/api/admin/position/index",
                "show": 1,
                "is_engine": 1,
                "is_link": 0,
                "status": 1,
            },
        ]

        # 在事务中逐条检查并插入
        async with in_transaction():
            for data in menus:
                if not await Menu.filter(id=data["id"]).exists():
                    await Menu.create(**data)
