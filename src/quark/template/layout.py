from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import time
from ..service.auth import AuthService
from ..service.user import UserService
from ..component.action.action import Component as ActionComponent
from ..component.footer.footer import Component as FooterComponent
from ..component.layout.layout import Component as LayoutComponent

@dataclass
class Layout:
    
    # layout 的左上角 的 title
    title: str = "QuarkPy"

    # layout 的左上角 的 logo
    logo: Optional[Any] = False

    # layout 的头部行为
    actions: Optional[Any] = None

    # layout 的菜单模式,side：右侧导航，top：顶部导航，mix：混合模式
    layout: str = "mix"

    # layout 的菜单模式为mix时，是否自动分割菜单
    split_menus: bool = False

    # layout 的内容模式,Fluid：定宽 1200px，Fixed：自适应
    content_width: str = "Fluid"

    # 主题色,"#1890ff"
    primary_color: str = "#1890ff"

    # 是否固定 header 到顶部
    fixed_header: bool = True

    # 是否固定导航
    fix_siderbar: bool = True

    # 使用 IconFont 的图标配置
    iconfont_url: str = "//at.alicdn.com/t/font_1615691_3pgkh5uyob.js"

    # 当前 layout 的语言设置，'zh-CN' | 'zh-TW' | 'en-US'
    locale: str = "zh-CN"

    # 侧边菜单宽度
    sider_width: int = 208

    # 网站版权 time.Now().Format("2006") + " QuarkPy"
    copyright: str = time.strftime("%Y") + " QuarkCloud"

    # 友情链接
    links: List[Dict[str, Any]] = field(default_factory=lambda: [
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
        ])
    
    # 右上角菜单
    right_menus: List[Any] = field(default_factory=lambda: [
            ActionComponent().set_label("个人设置").
            set_action_type("link").
            set_type("link", False).
            set_icon("setting").
            set_style({"color": "rgb(0 0 0 / 88%)"}).
            set_href("#/layout/index?api=/api/admin/account/form").
            set_size("small"),

            ActionComponent().set_label("退出登录").
            set_action_type("ajax").
            set_type("link", False).
            set_icon("logout").
            set_style({"color": "rgb(0 0 0 / 88%)"}).
            set_api("/api/admin/logout/index/handle").
            set_size("small"),
        ])

    def get_title(self) -> str:
        return self.title

    def get_logo(self) -> Optional[Any]:
        return self.logo

    def get_actions(self) -> Optional[Any]:
        return self.actions

    def get_layout(self) -> str:
        return self.layout

    def get_split_menus(self) -> bool:
        return self.split_menus

    def get_content_width(self) -> str:
        return self.content_width

    def get_primary_color(self) -> str:
        return self.primary_color

    def get_fixed_header(self) -> bool:
        return self.fixed_header

    def get_fix_siderbar(self) -> bool:
        return self.fix_siderbar

    def get_iconfont_url(self) -> str:
        return self.iconfont_url

    def get_locale(self) -> str:
        return self.locale

    def get_sider_width(self) -> int:
        return self.sider_width

    def get_copyright(self) -> str:
        return self.copyright

    def get_links(self) -> List[Dict[str, Any]]:
        return self.links

    def get_right_menus(self) -> List[Any]:
        return self.right_menus

    def get_menus(self) -> Any:
        auth_service = AuthService()
        admin_info = auth_service.get_admin()

        # 获取管理员菜单
        user_service = UserService()
        return user_service.get_menu_list_by_id(admin_info.id)

    def render(self) -> Any:

        # 获取 layout 的左上角 的 title
        title = self.get_title()

        # 获取 layout 的左上角 的 logo
        logo = self.get_logo()

        # 获取 layout 的头部行为
        actions = self.get_actions()

        # 获取 layout 的菜单模式,side：右侧导航，top：顶部导航，mix：混合模式
        layout_mode = self.get_layout()

        # 获取 layout 的菜单模式为mix时，是否自动分割菜单
        split_menus = self.get_split_menus()

        # 获取 layout 的内容模式,Fluid：定宽 1200px，Fixed：自适应
        content_width = self.get_content_width()

        # 获取主题色,"#1890ff"
        primary_color = self.get_primary_color()

        # 获取是否固定导航
        fix_siderbar = self.get_fix_siderbar()

        # 获取是否固定 header 到顶部
        fixed_header = self.get_fixed_header()

        # 获取使用 IconFont 的图标配置
        iconfont_url = self.get_iconfont_url()

        # 获取当前 layout 的语言设置，'zh-CN' | 'zh-TW' | 'en-US'
        locale = self.get_locale()

        # 侧边菜单宽度
        sider_width = self.get_sider_width()

        # 获取管理员菜单
        get_menus = self.get_menus()

        # 网站版权 time.Now().Format("2006") + " QuarkPy"
        copyright = self.get_copyright()

        # 友情链接
        links = self.get_links()

        # 右上角菜单
        right_menus = self.get_right_menus()

        # 页脚
        footer = (
            FooterComponent().
                set_copyright(copyright).
                set_links(links)
            )

        component = (
            LayoutComponent().
                set_title(title).
                set_logo(logo).
                set_menu(get_menus).
                set_actions(actions).
                set_layout(layout_mode).
                set_split_menus(split_menus).
                set_content_width(content_width).
                set_primary_color(primary_color).
                set_fix_siderbar(fix_siderbar).
                set_fixed_header(fixed_header).
                set_iconfont_url(iconfont_url).
                set_locale(locale).
                set_sider_width(sider_width).
                set_right_menus(right_menus).
                set_footer(footer).to_json()
            )

        return component