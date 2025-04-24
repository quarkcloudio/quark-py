from dataclasses import dataclass
from flask import request
from quark.template.login import Login
from quark.template.component.form import field, Rule
from quark.template.component.icon.icon import Component as Icon
from quark.template.component.message.message import Component as Message
from quark.cache import cache
from quark.service import auth_service

@dataclass
class Index(Login):

    def __post_init__(self):

        # 登录接口
        self.api =  "/api/admin/login/index/handle"

        # 标题
        self.title = "QuarkPy"

        # 跳转地址
        self.redirect = "/layout/index?api=/api/admin/dashboard/index/index"

        # 子标题
        self.sub_title = "信息丰富的世界里，唯一稀缺的就是人类的注意力"

        return self
    
    def fields(self):
        return [
            (
                field.Text(name="username").
                set_placeholder("用户名").
                set_rules([
                    Rule.is_required("请输入用户名")
                ]).
                set_width("100%").
                set_size("large").
                set_prefix(Icon().set_type("icon-user"))
            ),
            (
                field.Password(name="password").
                set_placeholder("密码").
                set_rules([
                    Rule.is_required("请输入密码")
                ]).
                set_width("100%").
                set_size("large").
                set_prefix(Icon().set_type("icon-lock"))
            ),
            (
                field.ImageCaptcha(name="captcha").
                set_captcha_id_url("/api/admin/login/index/captchaId").
                set_captcha_url("/api/admin/login/index/captcha/:id").
                set_placeholder("验证码").
                set_rules([
                    Rule.is_required("请输入验证码")
                ]).
                set_width("100%").
                set_size("large").
                set_prefix(Icon().set_type("icon-safetycertificate"))
            )
        ]
    
    def handle(self):
        data = request.get_json()

        if not data["captcha"]["id"] or not data["captcha"]["value"]:
            return Message.error("验证码不能为空")

        if cache.get(data["captcha"]["id"]) != data["captcha"]["value"]:
            return Message.error("验证码错误")

        if not data["username"] or not data["password"]:
            return Message.error("用户名或密码不能为空")

        try:
            token = auth_service.admin_login(data["username"], data["password"])
        except Exception as e:
            return Message.error(str(e))

        return Message.success("登录成功", {
            "token": token
        })