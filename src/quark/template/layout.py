import time
from typing import Any, Dict, List, Optional

from fastapi import Request
from pydantic import BaseModel, Field

from ..component.action.action import Action
from ..component.footer.footer import Footer
from ..component.layout.layout import Layout as LayoutComponent
from ..services.auth import AuthService
from ..services.user import UserService


class Layout(BaseModel):
    """后台布局"""

    # layout 的左上角 的 title
    title: str = Field(default="QuarkPy")

    # layout 的左上角 的 logo
    logo: Optional[Any] = Field(default=False)

    # layout 的头部行为
    actions: Optional[Any] = Field(default=None)

    # layout 的菜单模式,side：右侧导航，top：顶部导航，mix：混合模式
    layout: str = Field(default="mix")

    # layout 的菜单模式为mix时，是否自动分割菜单
    split_menus: bool = Field(default=False)

    # layout 的内容模式,Fluid：定宽 1200px，Fixed：自适应
    content_width: str = Field(default="Fluid")

    # 主题色,"#1890ff"
    primary_color: str = Field(default="#1890ff")

    # 是否固定 header 到顶部
    fixed_header: bool = Field(default=True)

    # 是否固定导航
    fix_siderbar: bool = Field(default=True)

    # 使用 IconFont 的图标配置
    iconfont_url: str = Field(default="//at.alicdn.com/t/font_1615691_3pgkh5uyob.js")

    # 当前 layout 的语言设置，'zh-CN' | 'zh-TW' | 'en-US'
    locale: str = Field(default="zh-CN")

    # 侧边菜单宽度
    sider_width: int = Field(default=208)

    # 网站版权 time.Now().Format("2006") + " QuarkGo"
    copyright: str = Field(default_factory=lambda: time.strftime("%Y") + " QuarkCloud")

    # 友情链接
    links: List[Dict[str, Any]] = Field(
        default_factory=lambda: [
            {
                "key": "1",
                "title": "QuarkPy",
                "href": "https://github.com/quarkcloudio/quark-py",
            },
            {
                "key": "2",
                "title": "QuarkCloud",
                "href": "http://quarkcloud.io",
            },
            {
                "key": "3",
                "title": "Github",
                "href": "https://github.com/quarkcloudio",
            },
        ]
    )

    # 右上角菜单
    right_menus: List[Any] = Field(
        default_factory=lambda: [
            Action()
            .set_label("个人设置")
            .set_action_type("link")
            .set_type("link", False)
            .set_icon("setting")
            .set_style({"color": "rgb(0 0 0 / 88%)"})
            .set_href("#/layout/index?api=/api/admin/account/form")
            .set_size("small"),
            Action()
            .set_label("退出登录")
            .set_action_type("ajax")
            .set_type("link", False)
            .set_icon("logout")
            .set_style({"color": "rgb(0 0 0 / 88%)"})
            .set_api("/api/admin/logout/index/handle")
            .set_size("small"),
        ]
    )

    async def init(self, request: Request):
        """初始化"""
        return self

    async def get_menus(self, request: Request) -> Any:
        auth_service = AuthService(request)
        user_info = await auth_service.get_current_admin()
        return await UserService().get_menu_list_by_id(user_info.id)

    async def render(self, request: Request) -> Any:
        footer = Footer().set_links(self.links).set_copyright(self.copyright)

        component = (
            LayoutComponent()
            .set_title(self.title)
            .set_logo(self.logo)
            .set_menu(await self.get_menus(request))
            .set_actions(self.actions)
            .set_layout(self.layout)
            .set_split_menus(self.split_menus)
            .set_content_width(self.content_width)
            .set_primary_color(self.primary_color)
            .set_fix_siderbar(self.fix_siderbar)
            .set_fixed_header(self.fixed_header)
            .set_iconfont_url(self.iconfont_url)
            .set_locale(self.locale)
            .set_sider_width(self.sider_width)
            .set_right_menus(self.right_menus)
            .set_footer(footer)
        )

        return component
