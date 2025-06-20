from fastapi import Request
from fastapi.responses import JSONResponse
from tortoise.transactions import in_transaction
from tortoise.exceptions import IntegrityError
from typing import List
from pydantic import BaseModel
import re

# 假设你的Permission模型类似这样
from models import Permission


# 辅助函数：PascalCase转换
def pascal_case(s: str) -> str:
    # 简单实现，将下划线分隔转成PascalCase
    parts = re.split(r"[^a-zA-Z0-9]", s)
    return "".join(word.capitalize() for word in parts if word)


class SyncPermissionAction:
    name = "同步权限"
    reload = "table"
    with_loading = True
    only_on_index = True
    action_type = "ajax"

    async def handle(self, request: Request):
        """
        同步权限逻辑：
        - 获取所有系统路由（此处示例需要你提供）
        - 过滤 /api/admin 开头的路由
        - 转换成权限名称（PascalCase）
        - 去重，和数据库已存在权限比较，新增不存在的权限
        """

        # 获取所有接口路由路径，示例用request.app.routes，具体看你的项目如何获取
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
            return JSONResponse(status_code=400, content={"error": "无新增权限"})

        # 批量写入数据库
        try:
            async with in_transaction():
                await Permission.bulk_create(new_permissions)
        except IntegrityError as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

        return JSONResponse(content={"message": "操作成功"})
