from dataclasses import dataclass
from quark.template.login import Login
from quark.template.component.form import field, Rule

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
                set_size("large")
            ),
            (
                field.Password(name="password").
                set_placeholder("密码").
                set_rules([
                    Rule.is_required("请输入密码")
                ]).
                set_width("100%").
                set_size("large")
            ),
            (
                field.ImageCaptcha(name="captcha").
                set_placeholder("验证码").
                set_rules([
                    Rule.is_required("请输入验证码")
                ]).
                set_width("100%").
                set_size("large")
            )
        ]