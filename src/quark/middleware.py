from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware

from quark import Message
from quark.models import ActionLog
from quark.services import ActionLogService, AuthService


# 自定义中间件
class Middleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)
        url_path = request.url.path
        route = request.scope.get("route")
        route_path = route.path if route else url_path

        # 获取登录实例并启动
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

        # 判断是否在登录路由中
        in_login_route = any(v["path"] == route_path for v in login_routes)
        if in_login_route:
            return response

        # 排除非后台路由
        if "api/admin" not in url_path:
            return response

        # 获取管理员信息
        auth_service = AuthService(request)
        try:
            admin_info = await auth_service.get_current_admin()
        except Exception as e:
            return JSONResponse(
                status_code=401,
                content=jsonable_encoder(Message.error(str(e)), exclude_none=True),
            )

        # 权限验证
        if admin_info.id != 1:
            results = []
            for path in [route_path, url_path]:
                try:
                    result = await auth_service.check_permission(path, request.method)
                    results.append(result)
                except Exception as e:
                    return JSONResponse(
                        status_code=500,
                        content=jsonable_encoder(
                            Message.error(str(e)), exclude_none=True
                        ),
                    )

            if not any(results):
                return JSONResponse(
                    status_code=403,
                    content=jsonable_encoder(
                        Message.error("403 Forbidden"), exclude_none=True
                    ),
                )

        # 记录操作日志
        await ActionLogService().insert_get_id(
            ActionLog(
                uid=admin_info.id,
                username=admin_info.username,
                url=url_path,
                ip=request.client.host if request.client else "",
                type="ADMIN",
                remark="",
            )
        )

        return response
