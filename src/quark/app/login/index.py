from dataclasses import dataclass
from quark.template.login import Login
from quark.template.component.form import field, Rule

@dataclass
class Index(Login):

    def __post_init__(self):

        # 登录接口
        self.api =  "/api/admin/login/index/handle"

        # 标题
        self.title = "QuarkGo"

        # 跳转地址
        self.redirect = "/layout/index?api=/api/admin/dashboard/index/index"

        # 子标题
        self.sub_title = "信息丰富的世界里，唯一稀缺的就是人类的注意力"

        return self
    
    def fields(self):
        return [
            (
                field.Text(name="username", label="用户名", required=True).
                set_rules([
                    Rule.required("请输入用户名")
                ]).
                set_width("100%").
                set_size("large")
            ),
            (
                field.Password(name="password", label="密码", required=True).
                set_rules([
                    Rule.required("请输入密码")
                ]).
                set_width("100%").
                set_size("large")
            )
        ]