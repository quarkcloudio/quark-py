from typing import Any, List
from quark import Auth, Request, cache
from quark.component.form import Rule, field
from quark.component.icon.icon import Icon
from quark.component.message.message import Message
from quark.schemas import LoginData
from quark.services.auth import AuthService


class Index(Auth):

    async def init(self, request: Request):
        self.api = "/api/admin/auth/index/login"
        self.title = "QuarkPy"
        self.redirect = "/layout/index?api=/api/admin/dashboard/index/index"
        return self

    async def fields(self, request: Request) -> List[Any]:
        return [
            (
                field.Text(name="username")
                .set_placeholder("用户名")
                .set_rules([Rule.required("请输入用户名")])
                .set_width("100%")
                .set_size("large")
                .set_prefix(Icon().set_type("ant-design:user-outlined"))
            ),
            (
                field.Password(name="password")
                .set_placeholder("密码")
                .set_rules([Rule.required("请输入密码")])
                .set_width("100%")
                .set_size("large")
                .set_prefix(Icon().set_type("ant-design:lock-outlined"))
            ),
            (
                field.ImageCaptcha(name="captcha")
                .set_captcha_url("/api/admin/auth/index/captcha")
                .set_placeholder("验证码")
                .set_rules([Rule.required("请输入验证码")])
                .set_width("100%")
                .set_size("large")
                .set_prefix(Icon().set_type("ant-design:safety-certificate-outlined"))
            ),
        ]

    async def login(self, request: Request):
        data_json = await request.json()
        try:
            data = LoginData(**data_json)
        except Exception as e:
            return Message.error(str(e))

        # 验证验证码
        cached_captcha = await cache.get(data.captcha["id"])
        if cached_captcha != data.captcha["value"]:
            return Message.error("验证码错误")

        if not data.username or not data.password:
            return Message.error("用户名或密码不能为空")

        try:
            token = await AuthService(request).login(
                data.username, data.password, "admin"
            )
        except Exception as e:
            return Message.error(str(e))

        return Message.success("登录成功", {"token": token})
