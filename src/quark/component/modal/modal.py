from pydantic import Field, model_validator
from typing import Any, List, Optional
from ..component import Component

class Modal(Component):
    component: str = Field(default="modal")
    title: Any = Field(None, description="标题")
    centered: bool = Field(False, description="垂直居中展示 Modal")
    closable: bool = Field(True, description="是否显示右上角的关闭按钮")
    destroy_on_close: bool = Field(False, alias="destroyOnClose", description="关闭时销毁 Modal 里的子元素")
    focus_trigger_after_close: bool = Field(False, alias="focusTriggerAfterClose", description="设置按钮形状，可选值为 circle、 round 或者不设")
    keyboard: bool = Field(True, description="是否支持键盘 esc 关闭")
    mask: bool = Field(True, description="是否展示遮罩")
    mask_closable: bool = Field(True, alias="maskClosable", description="点击蒙层是否允许关闭")
    open: bool = Field(False, description="对话框是否可见")
    width: int = Field(520, description="宽度")
    z_index: int = Field(1000, alias="zIndex", description="设置 Modal 的 z-index")
    actions: List[Any] = Field([], description="弹窗行为")
    init_api: Optional[Any] = Field(None, alias="initApi", description="数据初始化接口")
    body: Any = Field(None, description="容器控件里面的内容")

    @model_validator(mode="after")
    def init(self):
        self.set_key("modal")
        return self

    def set_style(self, style: Any):
        """Set style."""
        self.style = style
        return self

    def set_title(self, title: Any):
        """标题"""
        self.title = title
        return self

    def set_body(self, body: Any):
        """容器控件里面的内容"""
        self.body = body
        return self

    def set_centered(self, centered: bool):
        """垂直居中展示 Modal"""
        self.centered = centered
        return self

    def set_closable(self, closable: bool):
        """是否显示右上角的关闭按钮"""
        self.closable = closable
        return self

    def set_destroy_on_close(self, destroy_on_close: bool):
        """关闭时销毁 Modal 里的子元素"""
        self.destroy_on_close = destroy_on_close
        return self

    def set_focus_trigger_after_close(self, focus_trigger_after_close: bool):
        """设置按钮形状，可选值为 circle、 round 或者不设"""
        self.focus_trigger_after_close = focus_trigger_after_close
        return self

    def set_keyboard(self, keyboard: bool):
        """是否支持键盘 esc 关闭"""
        self.keyboard = keyboard
        return self

    def set_mask(self, mask: bool):
        """是否展示遮罩"""
        self.mask = mask
        return self

    def set_mask_closable(self, mask_closable: bool):
        """点击蒙层是否允许关闭"""
        self.mask_closable = mask_closable
        return self

    def set_open(self, open_: bool):
        """对话框是否可见"""
        self.open = open_
        return self

    def set_width(self, width: int):
        """宽度"""
        self.width = width
        return self

    def set_z_index(self, z_index: int):
        """设置 Modal 的 z-index"""
        self.z_index = z_index
        return self

    def set_actions(self, actions: List[Any]):
        """弹窗行为"""
        self.actions = actions
        return self

    def set_init_api(self, api: Any):
        """数据初始化接口"""
        self.init_api = api
        return self