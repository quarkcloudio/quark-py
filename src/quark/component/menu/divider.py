from pydantic import model_validator
from ..component import Component


class Divider(Component):
    component: str = "menuDivider"
    dashed: bool = False

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    # 子菜单项值
    def set_dashed(self, dashed: bool):
        self.dashed = dashed
        return self
