from dataclasses import dataclass, field
from typing import Optional, Any, List
import i18n

@dataclass
class Login:
    api: str = "/api/admin/login/index/handle"
    redirect: str = "/layout/index?api=/api/admin/dashboard/index/index"
    logo: Optional[Any] = None
    title: str = "QuarkPy"
    subtitle: str = "信息丰富的世界里，唯一稀缺的就是人类的注意力"

    # 方法还是照常写
    def get_api(self) -> str:
        return self.api

    def get_redirect(self) -> str:
        return self.redirect

    def get_logo(self) -> Optional[Any]:
        return self.logo

    def get_title(self) -> str:
        return self.title

    def get_subtitle(self) -> str:
        return self.subtitle

    def render(self):
        # 模拟 login.Component 的 JSON 结构
        login_component = {
            "component": "login",
            "api": self.get_api(),
            "redirect": self.get_redirect(),
            "logo": self.get_logo(),
            "title": self.get_title(),
            "subTitle": self.get_subtitle(),
            "body": [
                # 添加字段组件字段结构
                {"component": "inputField", "name": "username", "label": "用户名"},
                {"component": "passwordField", "name": "password", "label": "密码"},
                {"component": "captchaField", "name": "captcha", "label": "验证码"},
            ]
        }
        return login_component