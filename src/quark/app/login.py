from typing import Any, List
from quark import Login, Request, cache
from quark.component.form import Rule, field
from quark.component.icon.icon import Icon
from quark.component.message.message import Message
from quark.schemas import LoginData
from quark.services.auth import AuthService


class Index(Login):

    async def init(self, request: Request):
        self.api = "/api/admin/login/index/handle"
        self.title = "QuarkPy"
        self.redirect = "/layout/index?api=/api/admin/dashboard/index/index"
        self.sub_title = "信息丰富的世界里，唯一稀缺的就是人类的注意力"
        return self

    async def fields(self, request: Request) -> List[Any]:
        return [
            (
                field.Text(name="username")
                .set_placeholder("用户名")
                .set_rules([Rule.required("请输入用户名")])
                .set_width("100%")
                .set_size("large")
                .set_prefix(Icon().set_type("icon-user"))
            ),
            (
                field.Password(name="password")
                .set_placeholder("密码")
                .set_rules([Rule.required("请输入密码")])
                .set_width("100%")
                .set_size("large")
                .set_prefix(Icon().set_type("icon-lock"))
            ),
            (
                field.ImageCaptcha(name="captcha")
                .set_captcha_id_url("/api/admin/login/index/captchaId")
                .set_captcha_url("/api/admin/login/index/captcha/:id")
                .set_placeholder("验证码")
                .set_rules([Rule.required("请输入验证码")])
                .set_width("100%")
                .set_size("large")
                .set_prefix(Icon().set_type("icon-safetycertificate"))
            ),
        ]

    async def handle(self, request: Request):
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
