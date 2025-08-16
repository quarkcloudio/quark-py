import re

import inflection
from tortoise.exceptions import IntegrityError
from tortoise.queryset import QuerySet
from tortoise.transactions import in_transaction

from quark import Message, Request
from quark.loader import load_resource_classes
from quark.models import Permission
from quark.template.action import Action


# 辅助函数：PascalCase转换
def pascal_case(path: str, method: str) -> str:
    s = path.replace("/api/admin/", "").replace("/", "_") + "_" + method.lower()
    # 简单实现，将下划线分隔转成PascalCase
    parts = re.split(r"[^a-zA-Z0-9]", s)
    return "".join(word.capitalize() for word in parts if word)


def paser_routes(routes: list, class_type: str) -> list:
    new_permissions = []
    classes = load_resource_classes(class_type)
    for get_class in classes:
        for route in routes:
            path = route["path"].replace(
                "{resource}",
                inflection.camelize(get_class.__name__, False),
            )
            name = pascal_case(path, route["method"])
            new_permissions.append(
                Permission(
                    name=name,
                    method=route["method"],
                    path=path,
                    guard_name="admin",
                )
            )
    return new_permissions


class SyncPermission(Action):
    name = "同步权限"
    reload = "table"
    with_loading = True
    only_on_index = True
    action_type = "ajax"

    async def handle(self, request: Request, query: QuerySet):

        # 需要过滤对应路由
        routes = request.app.routes

        # 从数据库查询所有权限名
        existing_names = await Permission.all().values_list("name", flat=True)

        new_permissions = []
        names_set = set(existing_names)

        for route in routes:
            path = getattr(route, "path", "")
            methods = getattr(route, "methods", [])

            if not path.startswith("/api/admin"):
                continue

            if path not in [
                "/api/admin/dashboard/{resource}/index",
                "/api/admin/layout/{resource}/index",
                "/api/admin/login/{resource}/index",
                "/api/admin/login/{resource}/captchaId",
                "/api/admin/login/{resource}/captcha/{id}",
                "/api/admin/login/{resource}/handle",
                "/api/admin/logout/{resource}/handle",
                "/api/admin/{resource}/index",
                "/api/admin/{resource}/editable",
                "/api/admin/{resource}/create",
                "/api/admin/{resource}/store",
                "/api/admin/{resource}/edit",
                "/api/admin/{resource}/edit/values",
                "/api/admin/{resource}/save",
                "/api/admin/{resource}/import",
                "/api/admin/{resource}/export",
                "/api/admin/{resource}/detail",
                "/api/admin/{resource}/detail/values",
                "/api/admin/{resource}/import/template",
                "/api/admin/{resource}/form",
                "/api/admin/{resource}/action/{uriKey}",
                "/api/admin/{resource}/action/{uriKey}/values",
                "/api/admin/upload/{resource}/getList",
                "/api/admin/upload/{resource}/delete",
                "/api/admin/upload/{resource}/crop",
                "/api/admin/upload/{resource}/handle",
                "/api/admin/upload/{resource}/base64Handle",
            ]:
                for method in methods:
                    name = pascal_case(path, method)
                    if name not in names_set and all(
                        p.name != name for p in new_permissions
                    ):
                        new_permissions.append(
                            Permission(
                                name=name,
                                method=method,
                                path=path,
                                guard_name="admin",
                            )
                        )

        # 仪表盘
        classes = load_resource_classes("Dashboard")
        for get_class in classes:
            path = "/api/admin/dashboard/{resource}/index"
            method = "GET"
            path = path.replace(
                "{resource}",
                inflection.camelize(get_class.__name__.lower(), False),
            )
            name = pascal_case(path, method)
            if name not in names_set and all(p.name != name for p in new_permissions):
                new_permissions.append(
                    Permission(
                        name=name,
                        method=method,
                        path=path,
                        guard_name="admin",
                    )
                )

        # 布局
        classes = load_resource_classes("Layout")
        path = "/api/admin/layout/{resource}/index"
        method = "GET"
        for get_class in classes:
            path = path.replace(
                "{resource}",
                inflection.camelize(get_class.__name__.lower(), False),
            )
            name = pascal_case(path, method)
            if name not in names_set and all(p.name != name for p in new_permissions):
                new_permissions.append(
                    Permission(
                        name=name,
                        method=method,
                        path=path,
                        guard_name="admin",
                    )
                )

        # 登录
        login_routes = [
            {
                "path": "/api/admin/login/{resource}/index",
                "method": "GET",
            },
            {
                "path": "/api/admin/login/{resource}/captchaId",
                "method": "GET",
            },
            {
                "path": "/api/admin/login/{resource}/captcha/{id}",
                "method": "GET",
            },
            {
                "path": "/api/admin/login/{resource}/handle",
                "method": "POST",
            },
            {
                "path": "/api/admin/logout/{resource}/handle",
                "method": "GET",
            },
        ]

        new_permissions += paser_routes(login_routes, "Login")

        # 资源
        resource_routes = [
            {
                "path": "/api/admin/{resource}/index",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/editable",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/create",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/store",
                "method": "POST",
            },
            {
                "path": "/api/admin/{resource}/edit",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/edit/values",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/save",
                "method": "POST",
            },
            {
                "path": "/api/admin/{resource}/import",
                "method": "POST",
            },
            {
                "path": "/api/admin/{resource}/export",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/detail",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/detail/values",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/import/template",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/form",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/action/{uriKey}",
                "method": "GET",
            },
        ]
        new_permissions += paser_routes(resource_routes, "Resource")

        # 上传
        upload_routes = [
            {
                "path": "/api/admin/upload/{resource}/getList",
                "method": "GET",
            },
            {
                "path": "/api/admin/upload/{resource}/delete",
                "method": "GET",
            },
            {
                "path": "/api/admin/upload/{resource}/delete",
                "method": "POST",
            },
            {
                "path": "/api/admin/upload/{resource}/crop",
                "method": "POST",
            },
            {
                "path": "/api/admin/upload/{resource}/handle",
                "method": "POST",
            },
            {
                "path": "/api/admin/upload/{resource}/base64Handle",
                "method": "POST",
            },
        ]
        new_permissions += paser_routes(upload_routes, "Upload")

        # 资源行为
        action_routes = [
            {
                "path": "/api/admin/{resource}/action/{uriKey}",
                "method": "GET",
            },
            {
                "path": "/api/admin/{resource}/action/{uriKey}/values",
                "method": "GET",
            },
        ]
        classes = load_resource_classes("Resource")
        for get_class in classes:
            object = await get_class().init(request)
            actions = await object.actions(request)
            for action in actions:
                uri_key = action.get_uri_key(action)
                action_type = action.get_action_type()
                if action_type == "dropdown":
                    for dropdown_action in action.get_actions():
                        current_uri_key = action.get_uri_key(dropdown_action)
                        for action_route in action_routes:
                            path = action_route["path"]
                            method = action_route["method"]
                            path = path.replace(
                                "{uriKey}",
                                current_uri_key,
                            )
                            path = path.replace(
                                "{resource}",
                                inflection.camelize(get_class.__name__, False),
                            )
                            name = pascal_case(path, method)
                            if name not in names_set and all(
                                p.name != name for p in new_permissions
                            ):
                                new_permissions.append(
                                    Permission(
                                        name=name,
                                        method=method,
                                        path=path,
                                        guard_name="admin",
                                    )
                                )
                else:
                    for action_route in action_routes:
                        path = action_route["path"]
                        method = action_route["method"]
                        path = path.replace(
                            "{uriKey}",
                            uri_key,
                        )
                        path = path.replace(
                            "{resource}",
                            inflection.camelize(get_class.__name__, False),
                        )
                        name = pascal_case(path, method)
                        if name not in names_set and all(
                            p.name != name for p in new_permissions
                        ):
                            new_permissions.append(
                                Permission(
                                    name=name,
                                    method=method,
                                    path=path,
                                    guard_name="admin",
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
