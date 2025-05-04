from pydantic import model_validator
from typing import Any, Dict, List, Optional
from ..component import Component

class Layout(Component):
    component: str = "layout"
    cache: bool = True
    title: Optional[str] = None
    logo: Optional[Any] = None
    loading: bool = False
    content_style: Optional[Dict[str, str]] = None
    actions: Optional[Any] = None
    layout: Optional[str] = None
    split_menus: bool = None
    content_width: Optional[str] = None
    primary_color: Optional[str] = None
    fixed_header: bool = None
    fix_siderbar: bool = None
    iconfont_url: Optional[str] = None
    locale: Optional[str] = None
    sider_width: Optional[int] = None
    menu: Optional[Any] = None
    right_menus: Optional[List[Any]] = None  # 右上角菜单
    footer: Optional[Any] = None
    body: Optional[Any] = None

    @model_validator(mode="after")
    def init(self):
        self.cache = True
        self.set_key()
        return self

    # Set style.
    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    # 是否缓存layout
    def set_cache(self, cache: bool):
        self.cache = cache
        return self

    # layout 的左上角 的 title
    def set_title(self, title: str):
        self.title = title
        return self

    # layout 的左上角的 logo
    def set_logo(self, logo: Any):
        self.logo = logo
        return self

    # layout 的加载态
    def set_loading(self, loading: bool):
        self.loading = loading
        return self

    # layout 的内容区 style
    def set_content_style(self, content_style: Dict[str, str]):
        self.content_style = content_style
        return self

    # layout 的头部行为
    def set_actions(self, actions: Any):
        self.actions = actions
        return self

    # layout 的布局模式，side：右侧导航，top：顶部导航，mix：混合模式
    def set_layout(self, layout: str):
        self.layout = layout
        return self

    # layout 的内容模式,Fluid：定宽 1200px，Fixed：自适应
    def set_content_width(self, content_width: str):
        self.content_width = content_width
        return self

    # 容器控件里面的内容
    def set_primary_color(self, primary_color: str):
        self.primary_color = primary_color
        return self

    # 是否固定 header 到顶部
    def set_fixed_header(self, fixed_header: bool):
        self.fixed_header = fixed_header
        return self

    # 是否固定导航
    def set_fix_siderbar(self, fix_siderbar: bool):
        self.fix_siderbar = fix_siderbar
        return self

    # 使用 IconFont 的图标配置
    def set_iconfont_url(self, iconfont_url: str):
        self.iconfont_url = iconfont_url
        return self

    # 当前 layout 的语言设置，'zh-CN' | 'zh-TW' | 'en-US'
    def set_locale(self, locale: str):
        self.locale = locale
        return self

    # 侧边菜单宽度
    def set_sider_width(self, sider_width: int):
        self.sider_width = sider_width
        return self

    # 自动分割菜单
    def set_split_menus(self, split_menus: bool):
        self.split_menus = split_menus
        return self

    # 菜单
    def set_menu(self, menu: Any):
        self.menu = menu
        return self

    # 右上角菜单
    def set_right_menus(self, right_menus: List[Any]):
        self.right_menus = right_menus
        return self

    # 页脚
    def set_footer(self, footer: Any):
        self.footer = footer
        return self

    # 内容
    def set_body(self, body: Any):
        self.body = body
        return self