import json
from typing import Any, Dict, List

from tortoise import Model

from quark import Message, Request, Resource, models, utils
from quark.app import actions
from quark.component.form import field
from quark.component.form.rule import Rule
from quark.services.auth import AuthService
from quark.services.user import UserService


class Account(Resource):
    """
    个人设置
    """

    async def init(self, request: Request):

        # 页面标题
        self.title = "个人设置"

        # 模型
        self.model = models.User

        return self

    # 字段
    async def fields(self, request: Request) -> List[Any]:

        return [
            field.image("avatar", "头像"),
            field.text("nickname", "昵称").set_rules([Rule.required("昵称必须填写")]),
            field.text("email", "邮箱").set_rules([Rule.required("邮箱必须填写")]),
            field.text("phone", "手机号").set_rules([Rule.required("手机号必须填写")]),
            field.radio("sex", "性别")
            .set_options(
                [
                    field.radio_option("男", 1),
                    field.radio_option("女", 2),
                ]
            )
            .set_default_value(1),
            field.password("password", "密码")
            .set_rules(
                [
                    Rule.regexp(r"/^.{6,}$/", "密码不少于六位"),
                    Rule.regexp(r"/.*[A-Z].*/", "至少包含一个大写字母"),
                    Rule.regexp(r"/.*[a-z].*/", "至少包含一个小写字母"),
                    Rule.regexp(r"/.*[0-9].*/", "至少包含一个数字"),
                    Rule.regexp(
                        r"/.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-].*/",
                        "至少包含一个特殊字符",
                    ),
                ]
            )
            .set_help(
                "密码不少于六位，且至少包含一个大写字母、小写字母、数字和特殊字符"
            ),
        ]

    # 行为
    async def actions(self, request: Request) -> List[Any]:
        return [
            actions.FormSubmit(),
            actions.FormReset(),
            actions.FormBack(),
            actions.FormExtraBack(),
        ]

    # 表单显示前回调
    async def before_form_showing(self, request: Request) -> Any:
        admin_info = await AuthService(request).get_current_admin()
        user = await UserService().get_info_by_id(admin_info.id)
        user_dict = user.__dict__.copy()
        user_dict.pop("password", None)  # 安全地移除密码字段
        return user_dict

    # 表单提交处理
    async def form_handle(
        self, request: Request, model: Model, data: Dict[str, Any]
    ) -> Any:
        # 头像处理
        if data.get("avatar"):
            data["avatar"] = json.dumps(data["avatar"], ensure_ascii=False)

        # 加密密码
        if data.get("password"):
            data["password"] = utils.hash_password(data["password"])

        try:
            # 获取登录管理员信息
            admin_info = await AuthService(request).get_current_admin()
            model = await UserService().get_info_by_id(admin_info.id)
            await model.update_from_dict(data)
        except Exception as e:
            return Message.error(str(e))

        return Message.success("操作成功")
