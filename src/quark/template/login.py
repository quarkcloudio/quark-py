from dataclasses import dataclass, field
from typing import Optional, Any, List
from .component.login import login
import i18n

@dataclass
class Login:
    api: str = "/api/admin/login/index/handle"
    redirect: str = "/layout/index?api=/api/admin/dashboard/index/index"
    logo: Optional[Any] = None
    title: str = "QuarkPy"
    sub_title: str = "信息丰富的世界里，唯一稀缺的就是人类的注意力"

    # 方法还是照常写
    def get_api(self) -> str:
        return self.api

    def get_redirect(self) -> str:
        return self.redirect

    def get_logo(self) -> Optional[Any]:
        return self.logo

    def get_title(self) -> str:
        return self.title

    def get_sub_title(self) -> str:
        return self.sub_title

    def render(self):
        login_component = login.Component()
        login_component.set_title(self.get_title())
        login_component.set_sub_title(self.get_sub_title())
        login_component.set_api(self.get_api())
        login_component.set_redirect(self.get_redirect())
        login_component.set_logo(self.get_logo())
  
        return login_component.to_json()