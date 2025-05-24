from dataclasses import dataclass
from quark.template.resource import Resource
from quark.model.user import User as UserModel
from typing import List, Dict
from quark.component.form import field


@dataclass
class User(Resource):
    """
    用户管理
    """

    def __post_init__(self):

        # 页面标题
        self.title = "用户"

        # 模型
        self.model = UserModel

        return self

    def fields(self) -> List[Dict]:
        """字段定义"""
        return [
            field.id("id", "ID"),
            field.text("username", "用户名"),
            field.password("password", "密码"),
            field.text("email", "邮箱"),
        ]
