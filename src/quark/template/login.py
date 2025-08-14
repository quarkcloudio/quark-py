import random
import string
import uuid
from io import BytesIO
from typing import Any, Optional

from captcha.image import ImageCaptcha
from pydantic import BaseModel, Field

from quark import Message, Request, StreamingResponse

from .. import cache
from ..component.divider.divider import Divider
from ..component.login.login import Login as LoginComponent
from ..component.tabs.tabs import Tabs


class Login(BaseModel):
    """登录组件"""

    # 登录接口
    api: str = Field(default="/api/admin/login/index/handle")

    # 登录后跳转地址
    redirect: str = Field(default="/layout/index?api=/api/admin/dashboard/index/index")

    # Logo
    logo: Optional[Any] = Field(default=None)

    # 标题
    title: str = Field(default="QuarkPy")

    # 子标题
    sub_title: str = Field(default="信息丰富的世界里，唯一稀缺的就是人类的注意力")

    async def init(self, request: Request):
        """初始化"""
        return self

    async def captcha_id(self, request: Request):
        id = str(uuid.uuid4())
        await cache.set(id, "uninitialized", 60)
        return Message.success("获取成功", {"captchaId": id})

    async def captcha(self, request: Request):
        id = request.path_params["id"]
        value = await cache.get(id)
        if value != "uninitialized":
            return Message.error("验证码已过期，请重新获取")

        captcha_text = "".join(random.choices(string.digits, k=4))
        await cache.set(id, captcha_text, 60)

        image = ImageCaptcha(width=170, height=50)
        captcha_image = image.generate_image(captcha_text)

        buffer = BytesIO()
        captcha_image.save(buffer, format="PNG")
        buffer.seek(0)

        return StreamingResponse(buffer, media_type="image/png")

    async def fields(self, request: Request):
        return []

    async def handle(self, request: Request):
        return Message.error("请实现登录方法")

    async def logout(self, request: Request):
        return Message.success("退出成功", None, "/")

    async def fields_within_components(self, request: Request):

        # 获取字段
        fields = await self.fields(request)

        # 解析创建页表单组件内的字段
        items = await self.form_fields_parser(fields, request)

        return items

    async def form_fields_parser(self, fields: Any, request: Request):
        items = []
        path = request.url.path
        # 解析字段
        if isinstance(fields, list):
            for v in fields:
                if hasattr(v, "body"):
                    # 获取内容值
                    body = v.body

                    # 解析值
                    get_fields = await self.form_fields_parser(body, request)

                    # 更新值
                    v.body = get_fields

                    items.append(v)
                else:
                    component = getattr(v, "component", "")
                    if "Field" in component:
                        # 判断是否在创建页面
                        if (
                            hasattr(v, "is_shown_on_creation")
                            and v.is_shown_on_creation()
                        ):
                            # 生成前端验证规则
                            if hasattr(v, "build_frontend_rules"):
                                v.build_frontend_rules(path)

                            # 组合数据
                            items.append(v)
                    else:
                        items.append(v)

        return items

    async def render(self, request: Request):

        # 登录接口
        login_api = self.api

        # 登录后跳转地址
        redirect = self.redirect

        # Logo
        logo = self.logo

        # 标题
        title = self.title

        # 子标题
        sub_title = self.sub_title

        # 包裹在组件内的字段
        fields = await self.fields_within_components(request)

        # 解析tabPane组件
        if isinstance(fields, list) and len(fields) > 0:
            component_name = getattr(fields[0], "component", "")

            if component_name == "tabPane":
                tab_component = Tabs().set_tab_panes(fields).set_centered(True)

                # 组件
                component = (
                    LoginComponent()
                    .set_api(login_api)
                    .set_redirect(redirect)
                    .set_logo(logo)
                    .set_title(title)
                    .set_sub_title(sub_title)
                    .set_body(tab_component)
                )
            else:
                fields = [Divider().set_style({"marginTop": "-15px"})] + fields

                # 组件
                component = (
                    LoginComponent()
                    .set_api(login_api)
                    .set_redirect(redirect)
                    .set_logo(logo)
                    .set_title(title)
                    .set_sub_title(sub_title)
                    .set_body(fields)
                )
        else:
            fields = [Divider().set_style({"marginTop": "-15px"})] + fields

            # 组件
            component = (
                LoginComponent()
                .set_api(login_api)
                .set_redirect(redirect)
                .set_logo(logo)
                .set_title(title)
                .set_sub_title(sub_title)
                .set_body(fields)
            )

        return component
