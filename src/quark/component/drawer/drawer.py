from pydantic import Field, model_validator
from typing import Any, List, Optional
from ..component import Component

class Drawer(Component):
    component: str = Field(default="drawer")
    title: Any = Field(None, description="标题")
    body_style: Any = Field(None, alias="bodyStyle", description="Modal body 样式")
    closable: bool = Field(True, description="是否显示右上角的关闭按钮")
    content_wrapper_style: Any = Field(None, alias="contentWrapperStyle", description="可用于设置 Drawer 包裹内容部分的样式")
    destroy_on_close: bool = Field(False, alias="destroyOnClose", description="关闭时销毁 Modal 里的子元素")
    drawer_style: Any = Field(None, alias="drawerStyle", description="用于设置 Drawer 弹出层的样式")
    footer_style: Any = Field({"textAlign": "right"}, alias="footerStyle", description="抽屉页脚部件的样式")
    height: int = Field(256, description="高度, 在 placement 为 top 或 bottom 时使用")
    keyboard: bool = Field(True, description="是否支持键盘 esc 关闭")
    mask: bool = Field(True, description="是否展示遮罩")
    mask_closable: bool = Field(True, alias="maskClosable", description="点击蒙层是否允许关闭")
    mask_style: Any = Field(None, alias="maskStyle", description="遮罩样式")
    open: bool = Field(False, description="对话框是否可见")
    width: int = Field(256, description="宽度")
    z_index: int = Field(1000, alias="zIndex", description="设置 Modal 的 z-index")
    actions: List[Any] = Field([], description="弹窗行为")
    placement: str = Field("right", description="抽屉的方向, top | right | bottom | left")
    init_api: Optional[Any] = Field(None, alias="initApi", description="数据初始化接口")
    body: Any = Field(None, description="容器控件里面的内容")

    @model_validator(mode="after")
    def init(self):
        self.set_key("drawer")
        return self

    def set_style(self, style: Any):
        self.style = style
        return self

    def set_title(self, title: Any):
        self.title = title
        return self

    def set_body_style(self, style: Any):
        self.body_style = style
        return self

    def set_body(self, body: Any):
        self.body = body
        return self

    def set_closable(self, closable: bool):
        self.closable = closable
        return self

    def set_content_wrapper_style(self, style: Any):
        self.content_wrapper_style = style
        return self

    def set_destroy_on_close(self, destroy_on_close: bool):
        self.destroy_on_close = destroy_on_close
        return self

    def set_drawer_style(self, style: Any):
        self.drawer_style = style
        return self

    def set_footer_style(self, style: Any):
        self.footer_style = style
        return self

    def set_height(self, height: int):
        self.height = height
        return self

    def set_keyboard(self, keyboard: bool):
        self.keyboard = keyboard
        return self

    def set_mask(self, mask: bool):
        self.mask = mask
        return self

    def set_mask_closable(self, mask_closable: bool):
        self.mask_closable = mask_closable
        return self

    def set_mask_style(self, style: Any):
        self.mask_style = style
        return self

    def set_placement(self, placement: str):
        self.placement = placement
        return self

    def set_open(self, open_: bool):
        self.open = open_
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def set_z_index(self, z_index: int):
        self.z_index = z_index
        return self

    def set_actions(self, actions: List[Any]):
        self.actions = actions
        return self

    def set_init_api(self, api: Any):
        self.init_api = api
        return self