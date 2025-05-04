from ..component import Component

class Divider(Component):
    dashed: bool = False

    # 初始化
    def init(self):
        self.element.component = "menuDivider"
        self.element.set_key(DEFAULT_KEY, DEFAULT_CRYPT)
        return self

    # 子菜单项值
    def set_dashed(self, dashed: bool):
        self.dashed = dashed
        return self