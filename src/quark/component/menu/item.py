from pydantic import model_validator
from typing import Any, Callable, Optional
from ..component import Component
from ..modal.modal import Modal
from ..drawer.drawer import Drawer


class Item(Component):
    component: str = "menuItem"
    title: str = ""
    label: str = ""
    block: bool = False
    danger: bool = False
    disabled: bool = False
    ghost: bool = False
    icon: str = ""
    shape: str = ""
    size: str = "default"
    type: str = "default"
    action_type: str = ""
    submit_form: Optional[Any] = None
    href: str = ""
    target: str = ""
    modal: Optional[Any] = None
    drawer: Optional[Any] = None
    confirm_title: str = ""
    confirm_text: str = ""
    confirm_type: str = ""
    api: str = ""
    reload: str = ""
    with_loading: bool = False

    @model_validator(mode="after")
    def init(self):
        self.set_key("DEFAULT_KEY", False)
        return self

    # Set style.
    def set_style(self, style: dict[str, Any]) -> "Item":
        self.element.style = style
        return self

    # 设置收缩时展示的悬浮标题
    def set_title(self, title: str) -> "Item":
        self.title = title
        return self

    # 设置按钮文字
    def set_label(self, label: str) -> "Item":
        self.label = label
        return self

    # 将按钮宽度调整为其父宽度的选项
    def set_block(self, block: bool) -> "Item":
        self.block = block
        return self

    # 设置危险按钮
    def set_danger(self, danger: bool) -> "Item":
        self.danger = danger
        return self

    # 按钮失效状态
    def set_disabled(self, disabled: bool) -> "Item":
        self.disabled = disabled
        return self

    # 幽灵属性，使按钮背景透明
    def set_ghost(self, ghost: bool) -> "Item":
        self.ghost = ghost
        return self

    # 设置按钮图标
    def set_icon(self, icon: str) -> "Item":
        self.icon = "icon-" + icon
        return self

    # 设置按钮形状，可选值为 circle、 round 或者不设
    def set_shape(self, shape: str) -> "Item":
        self.shape = shape
        return self

    # 设置按钮类型，primary | ghost | dashed | link | text | default
    def set_type(self, button_type: str, danger: bool) -> "Item":
        self.type = button_type
        self.danger = danger
        return self

    # 设置按钮大小，large | middle | small | default
    def set_size(self, size: str) -> "Item":
        self.size = size
        return self

    # 【必填】这是 action 最核心的配置，来指定该 action 的作用类型，支持：ajax、link、url、drawer、dialog、confirm、cancel、prev、next、copy、close。
    def set_action_type(self, action_type: str) -> "Item":
        self.action_type = action_type
        return self

    # 当action 的作用类型为submit的时候，可以指定提交哪个表格，submitForm为提交表单的key值，为空时提交当前表单
    def set_submit_form(self, form_key: Any) -> "Item":
        self.submit_form = form_key
        return self

    # 点击跳转的地址，指定此属性 button 的行为和 a 链接一致
    def set_href(self, href: str) -> "Item":
        self.href = href
        return self

    # 相当于 a 链接的 target 属性，href 存在时生效
    def set_target(self, target: str) -> "Item":
        self.target = target
        return self

    # 设置跳转链接
    def set_link(self, href: str, target: str) -> "Item":
        self.set_href(href)
        self.set_target(target)
        self.action_type = "link"
        return self

    # 弹窗
    def set_modal(self, callback: Callable[[Modal], Any]) -> "Item":
        component = Modal()
        self.modal = callback(component)
        return self

    # 抽屉
    def set_drawer(self, callback: Callable[[Drawer], Any]) -> "Item":
        component = Drawer()
        self.drawer = callback(component)
        return self

    # 设置行为前的确认操作
    def set_with_confirm(self, title: str, text: str, confirm_type: str) -> "Item":
        self.confirm_title = title
        self.confirm_text = text
        self.confirm_type = confirm_type
        return self

    # 执行行为的接口链接
    def set_api(self, api: str) -> "Item":
        self.api = api
        self.action_type = "ajax"
        return self

    # 执行成功后刷新的组件
    def set_reload(self, reload: str) -> "Item":
        self.reload = reload
        return self

    # 是否具有loading
    def set_with_loading(self, loading: bool) -> "Item":
        self.with_loading = loading
        return self
