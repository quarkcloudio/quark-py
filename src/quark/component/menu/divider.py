from pydantic import BaseModel

# 模拟 component.Element
class Element(BaseModel):
    component: str = ""
    key: str = ""
    crypt: bool = False

    def set_key(self, key: str, crypt: bool):
        self.key = key
        self.crypt = crypt
        return self

DEFAULT_KEY = "DEFAULT_KEY"
DEFAULT_CRYPT = False

class Divider(BaseModel):
    element: Element
    dashed: bool = False

    # 初始化
    def init(self):
        self.element = Element()
        self.element.component = "menuDivider"
        self.element.set_key(DEFAULT_KEY, DEFAULT_CRYPT)
        return self

    # 子菜单项值
    def set_dashed(self, dashed: bool):
        self.dashed = dashed
        return self