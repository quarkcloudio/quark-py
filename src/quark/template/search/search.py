from typing import Any, Dict, Optional

from fastapi import Request
from tortoise.models import Model


class Search:
    """基础搜索字段配置类"""

    # 字段名
    column: str = ""

    # 字段标题
    name: str = ""

    # 组件名称
    component: str = "textField"

    # 接口
    api: str = ""

    def __init__(self, column: str = "", name: str = ""):
        self.name = name
        self.column = column

    def get_column(self, search: Any) -> str:
        """
        获取数据库字段名。若未设置 column，则自动从类名推断。
        示例：ProductNameSearch -> product_name
        """
        if not self.column:
            class_name = type(search).__name__
            clean_name = class_name.replace("Search", "")
            return clean_name.lower()
        return self.column

    def get_name(self) -> str:
        """获取字段显示名称"""
        return self.name

    def get_component(self) -> str:
        """获取前端组件名称"""
        return self.component

    def get_api(self) -> str:
        """获取关联 API 接口地址"""
        return self.api

    def get_default(self) -> Any:
        """获取默认值"""
        return True

    def apply(self, request: Request, query: Model, value: Any) -> Model:
        """执行查询逻辑，子类可重写此方法"""
        return query

    def options(self, request: Request) -> Optional[Any]:
        """扩展属性选项"""
        return None

    def load(self, request: Request) -> Dict[str, str]:
        """
        单向联动配置，返回示例：
        {"field": "you_want_load_field", "api": "/api/admin/resource/action/select-options"}
        """
        return {}
