from dataclasses import dataclass
from typing import Any, Optional
from flask import jsonify, redirect
from ..template.component.divider.divider import Component as Divider
from ..template.component.login.login import Component as LoginComponent
from ..template.component.tabs.tabs import Component as TabsComponent

@dataclass
class Login:
    index_path: str = ""
    handle_path: str = ""
    captcha_id_path: str = ""
    captcha_path: str = ""
    logout_path: str = ""
    api: str = ""
    redirect: str = ""
    logo: Optional[Any] = None
    title: str = ""
    sub_title: str = ""
    body: Optional[Any] = None

    def __post_init__(self):

        # 登录接口
        self.api =  "/api/admin/login/index/handle"

        # 标题
        self.title = "QuarkGo"

        # 跳转地址
        self.redirect = "/layout/index?api=/api/admin/dashboard/index/index"

        # 子标题
        self.sub_title = "信息丰富的世界里，唯一稀缺的就是人类的注意力"

        return self

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
        return jsonify({"code": 0, "message": "操作成功", "data": {"captchaId": 1}})

    def captcha(self, id):
        return ""

    def fields(self):
        return []

    def handle(self):
        return jsonify({"code": 1, "message": "请实现登录方法"})

    def logout(self):
        return redirect("/", code=302)

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
                    if "field" in component:
                        # 判断是否在创建页面
                        if hasattr(v, "is_shown_on_creation") and v.is_shown_on_creation():
                            # 生成前端验证规则
                            if hasattr(v, "build_frontend_rules"):
                                #v.build_frontend_rules(ctx.path)
                                print("todo")

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
                tab_component = TabsComponent().set_tab_panes(fields).set_centered(True)

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