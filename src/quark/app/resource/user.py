from dataclasses import dataclass
from quark.template.resource import Resource
from quark.model.user import User as UserModel


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
