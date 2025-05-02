from dataclasses import dataclass
from typing import Any, Dict, Optional, Union
from quark_go.v3 import Context  # 假设为 Quark-Go 上下文的 Python 实现
from gorm import DB  # 假设为 GORM 的 Python 封装或替代 ORM


@dataclass
class Search:
    """基础搜索字段配置类"""

    column: str = ""
    name: str = ""
    component: str = "textField"
    api: str = ""

    def new(self, ctx: Context) -> "Search":
        """加载初始化数据"""
        self.component = "textField"
        return self

    def init(self, ctx: Context) -> "Search":
        """初始化"""
        return self

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

    def apply(self, ctx: Context, query: DB, value: Any) -> DB:
        """执行查询逻辑，子类可重写此方法"""
        return query

    def options(self, ctx: Context) -> Optional[Any]:
        """扩展属性选项"""
        return None

    def load(self, ctx: Context) -> Dict[str, str]:
        """
        单向联动配置，返回示例：
        {"field": "you_want_load_field", "api": "/api/admin/resource/action/select-options"}
        """
        return {}