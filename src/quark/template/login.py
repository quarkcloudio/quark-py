from dataclasses import dataclass
from typing import Any, Optional
import uuid
import random
import string
from io import BytesIO
from captcha.image import ImageCaptcha
from flask import send_file, make_response
from ..component.message.message import Message
from ..component.divider.divider import Divider
from ..component.tabs.tabs import Tabs
from ..component.login.login import Login as LoginComponent
from ..cache import cache

@dataclass
class Login:

    # 登录接口
    api: str = "/api/admin/login/index/handle"

    # 登录后跳转地址
    redirect: str = "/layout/index?api=/api/admin/dashboard/index/index"

    # logo
    logo: Optional[Any] = None

    # 标题
    title: str = "QuarkPy"

    # 子标题
    sub_title: str = "信息丰富的世界里，唯一稀缺的就是人类的注意力"

    # 组件
    body: Optional[Any] = None

    def get_api(self) -> str:
        return self.api

    def get_redirect(self) -> str:
        return self.redirect

    def get_logo(self) -> Optional[Any]:
        return self.logo

    def get_title(self) -> str:
        return self.title

    def get_sub_title(self) -> str:
        return self.sub_title

    def captcha_id(self):
        id = str(uuid.uuid4())
        cache.set(id, "uninitialized", timeout=60)
        return Message.success("获取成功", {
            "captchaId": id
        })

    def captcha(self, id):
        value = cache.get(id)
        if value != "uninitialized":
            return Message.error("验证码已过期，请重新获取")
        # 生成随机验证码文本
        captcha_text = ''.join(random.choices(string.digits, k=4))
        cache.set(id, captcha_text, timeout=60)

        # 创建图形验证码对象
        image = ImageCaptcha(width=170, height=50)
        captcha_image = image.generate_image(captcha_text)

        # 保存为 BytesIO
        buffer = BytesIO()
        captcha_image.save(buffer, format='PNG')
        buffer.seek(0)

        # 返回二进制图片流
        response = make_response(send_file(buffer, mimetype='image/png'))
        return response

    def fields(self):
        return []

    def handle(self):
        return Message.error("请实现登录方法")

    def logout(self):
        return Message.success("退出成功", None, "/")

    def fields_within_components(self):

        # 获取字段
        fields = self.fields()

        # 解析创建页表单组件内的字段
        items = self.form_fields_parser(fields)

        return items

    def form_fields_parser(self, fields):
        items = []

        # 解析字段
        if isinstance(fields, list):
            for v in fields:
                if hasattr(v, "body"):
                    # 获取内容值
                    body = v.body

                    # 解析值
                    get_fields = self.form_fields_parser(body)

                    # 更新值
                    v.body = get_fields

                    items.append(v)
                else:
                    component = getattr(v, "component", "")
                    if "Field" in component:
                        # 判断是否在创建页面
                        if hasattr(v, "is_shown_on_creation") and v.is_shown_on_creation():
                            # 生成前端验证规则
                            if hasattr(v, "build_frontend_rules"):
                                v.build_frontend_rules()

                            # 组合数据
                            items.append(v)
                    else:
                        items.append(v)

        return items

    def render(self):

        # 登录接口
        login_api = self.get_api()

        # 登录后跳转地址
        redirect = self.get_redirect()

        # Logo
        logo = self.get_logo()

        # 标题
        title = self.get_title()

        # 子标题
        sub_title = self.get_sub_title()

        # 包裹在组件内的字段
        fields = self.fields_within_components()

        # 解析tabPane组件
        if isinstance(fields, list) and len(fields) > 0:
            component_name = getattr(fields[0], "component", "")

            if component_name == "tabPane":
                tab_component = Tabs().set_tab_panes(fields).set_centered(True)

                # 组件
                component = (
                    LoginComponent().
                        set_api(login_api).
                        set_redirect(redirect).
                        set_logo(logo).
                        set_title(title).
                        set_sub_title(sub_title).
                        set_body(tab_component).
                        to_json(indent=2)
                    )
            else:
                fields = [Divider().set_style({"marginTop": "-15px"})] + fields

                # 组件
                component = (
                    LoginComponent().
                        set_api(login_api).
                        set_redirect(redirect).
                        set_logo(logo).
                        set_title(title).
                        set_sub_title(sub_title).
                        set_body(fields).
                        to_json(indent=2)
                    )
        else:
            fields = [Divider().set_style({"marginTop": "-15px"})] + fields

            # 组件
            component = (
                LoginComponent().
                    set_api(login_api).
                    set_redirect(redirect).
                    set_logo(logo).
                    set_title(title).
                    set_sub_title(sub_title).
                    set_body(fields).
                    to_json()
                )

        return component