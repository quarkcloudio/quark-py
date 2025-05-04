from pydantic import Field, field_validator, model_validator
from typing import Any, List, Optional, Union
from ..component import Component
from ..drawer.drawer import Drawer
from ..modal.modal import Modal

class Action(Component):
    component: str = Field(default="action")
    label: Any = Field(default=None)
    block: bool = Field(default=False)
    danger: bool = Field(default=False)
    disabled: bool = Field(default=False)
    ghost: bool = Field(default=False)
    icon: Union[str, List[str]] = Field(default=None)
    shape: Optional[str] = Field(default=None)
    size: str = Field(default="default")
    type: str = Field(default="default")
    action_type: str = Field(default=None, alias="actionType")
    submit_form: Any = Field(default=None, alias="submitForm")
    href: Optional[str] = Field(default=None)
    target: Optional[str] = Field(default=None)
    modal: Optional[Any] = Field(default=None)
    drawer: Optional[Any] = Field(default=None)
    checked_children: Optional[Any] = Field(default=None, alias="checkedChildren")
    un_checked_children: Optional[Any] = Field(default=None, alias="unCheckedChildren")
    field_name: Optional[Any] = Field(default=None, alias="fieldName")
    field_value: Optional[Any] = Field(default=None, alias="fieldValue")
    confirm_title: str = Field(default="", alias="confirmTitle")
    confirm_text: str = Field(default="", alias="confirmText")
    confirm_type: str = Field(default="", alias="confirmType")
    api: Optional[str] = Field(default=None)
    reload: Optional[str] = Field(default=None)
    with_loading: bool = Field(default=False, alias="withLoading")

    @field_validator('icon')
    def validate_icon(cls, v):
        if isinstance(v, str):
            return f"icon-{v}"
        elif isinstance(v, list):
            return [f"icon-{item}" for item in v]
        return v

    @model_validator(mode="after")
    def init(self):
        self.set_key("action")
        return self

    def set_style(self, style: dict):
        self.style = style
        return self

    def set_label(self, label: Any):
        self.label = label
        return self

    def set_block(self, block: bool):
        self.block = block
        return self

    def set_danger(self, danger: bool):
        self.danger = danger
        return self

    def set_disabled(self, disabled: bool):
        self.disabled = disabled
        return self

    def set_ghost(self, ghost: bool):
        self.ghost = ghost
        return self

    def set_icon(self, icon: Union[str, List[str]]):
        self.icon = self.validate_icon(icon)
        return self

    def set_shape(self, shape: str):
        self.shape = shape
        return self

    def set_type(self, button_type: str, danger: bool):
        self.type = button_type
        self.danger = danger
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_action_type(self, action_type: str):
        self.action_type = action_type
        return self

    def set_submit_form(self, form_key: str):
        self.submit_form = form_key
        return self

    def set_href(self, href: str):
        self.href = href
        return self

    def set_target(self, target: str):
        self.target = target
        return self

    def set_link(self, href: str, target: str):
        self.set_href(href)
        self.set_target(target)
        self.action_type = "link"
        return self

    def set_modal(self, callback):
        component = Modal()
        self.modal = callback(component)
        return self

    def set_drawer(self, callback):
        component = Drawer()
        self.drawer = callback(component)
        return self

    def set_checked_children(self, checked_children: Any):
        self.checked_children = checked_children
        return self

    def set_un_checked_children(self, un_checked_children: Any):
        self.un_checked_children = un_checked_children
        return self

    def set_field_name(self, field_name: Any):
        self.field_name = field_name
        return self

    def set_field_value(self, field_value: Any):
        self.field_value = field_value
        return self

    def set_with_confirm(self, title: str, text: str, confirm_type: str):
        self.confirm_title = title
        self.confirm_text = text
        self.confirm_type = confirm_type
        return self

    def set_api(self, api: str):
        self.api = api
        self.action_type = "ajax"
        return self

    def set_reload(self, reload: str):
        self.reload = reload
        return self

    def set_with_loading(self, loading: bool):
        self.with_loading = loading
        return self