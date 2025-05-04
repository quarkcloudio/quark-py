from pydantic import BaseModel
from typing import Any, Optional
from ..component import Component

class Meta(Component):
    title: str = ""
    attribute: str = ""
    data_index: str = ""
    ellipsis: bool = False
    copyable: bool = False
    value_enum: Optional[Any] = None
    value_type: str = ""
    search: bool = False
    actions: bool = False

    def __init__(self, **data):
        super().__init__(**data)
        self.component = "meta"
        self.set_key("DEFAULT_KEY", False)

    # 初始化
    def init(self) -> 'Meta':
        self.component = "meta"
        self.set_key("DEFAULT_KEY", False)
        return self

    # Set style.
    def set_style(self, style: dict[str, Any]) -> 'Meta':
        self.style = style
        return self

    # 设置标题
    def set_title(self, title: str) -> 'Meta':
        self.title = title
        return self

    # 设置字段名称|字段的列名
    def set_attribute(self, attribute: str) -> 'Meta':
        self.data_index = attribute
        self.attribute = attribute
        return self

    # 设置是否自动缩略
    def set_ellipsis(self, ellipsis: bool) -> 'Meta':
        self.ellipsis = ellipsis
        return self

    # 设置是否支持复制
    def set_copyable(self, copyable: bool) -> 'Meta':
        self.copyable = copyable
        return self

    # 设置值的枚举，会自动转化把值当成 key 来取出要显示的内容
    def set_value_enum(self, value_enum: Any) -> 'Meta':
        value_enum_str = {}
        value_enum_int = {}

        if isinstance(value_enum, dict):
            for k, v in value_enum.items():
                if isinstance(k, str):
                    value_enum_str[k] = v
                elif isinstance(k, int):
                    value_enum_int[k] = v

        if value_enum_str:
            self.value_enum = value_enum_str
        if value_enum_int:
            self.value_enum = value_enum_int

        return self

    # 设置值的类型,"money" | "option" | "date" | "dateTime" | "time" | "text"| "index" | "indexBorder"
    def set_value_type(self, value_type: str) -> 'Meta':
        self.value_type = value_type
        return self

    # 在查询表单中不展示此项
    def set_search(self, search: bool) -> 'Meta':
        self.search = search
        return self

    def set_key(self, key: str, crypt: bool):
        # 这里简单处理，可根据实际需求实现
        pass