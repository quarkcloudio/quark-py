import re

from tortoise.exceptions import IntegrityError
from tortoise.models import QuerySet
from tortoise.transactions import in_transaction

from quark import Message, Request
from quark.models import Permission
from quark.template.action import Action


# 辅助函数：PascalCase转换
def pascal_case(s: str) -> str:
    # 简单实现，将下划线分隔转成PascalCase
    parts = re.split(r"[^a-zA-Z0-9]", s)
    return "".join(word.capitalize() for word in parts if word)


class SyncPermission(Action):
    name = "同步权限"
    reload = "table"
    with_loading = True
    only_on_index = True
    action_type = "ajax"

    async def handle(self, request: Request, query: QuerySet):
        routes = request.app.routes  # 需要过滤对应路由

        # 从数据库查询所有权限名
        existing_names = await Permission.all().values_list("name", flat=True)

        new_permissions = []
        names_set = set(existing_names)

        for route in routes:
            # route.path 和 route.methods 视框架结构而定，假设符合FastAPI标准
            path = getattr(route, "path", "")
            methods = getattr(route, "methods", [])

            if not path.startswith("/api/admin"):
                continue

            for method in methods:
                url = path.replace("/api/admin/", "")
                url = url.replace("/", "_") + "_" + method.lower()

                name = pascal_case(url)

                if name not in names_set and all(
                    p.name != name for p in new_permissions
                ):
                    new_permissions.append(
                        Permission(
                            name=name, method=method, path=path, guard_name="admin"
                        )
                    )

        if not new_permissions:
            return Message.error("无新增权限")

        try:
            async with in_transaction():
                await Permission.bulk_create(new_permissions)
        except IntegrityError as e:
            return Message.error(str(e))

        return Message.success("操作成功")
